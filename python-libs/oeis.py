
from itertools import count

#________________________________________________________________________

def promote_id_anchors(text):
    """
    Return a new string where each occurrence of a sequence ref `Aoooooo` replaced as `<a>` tag.
    """
    
    import re
    return re.compile('(?P<id>A\d{6,6})').sub(r'<a href="http://oeis.org/\g<id>">\g<id></a>', text)

        
def merge_splitted_text(lst):
    """
    Returns a new list where each splitted text in `lst` is joined into a single line of text.
    """

    merged = []

    i = 0
    while i < len(lst):

        if '(Start)' in lst[i] or '(start)' in lst[i]:
            j = i+1
            while j < len(lst) and not ('(End)' in lst[j] or '(end)' in lst[j]): j += 1
            joiner = "\n       - "
            #joiner = "\n<br>"
            merged.append(joiner.join(lst[i:j if j >= len(lst) or lst[j] == '(End)' else j+1])
                          .replace('(Start)', '').replace('(start)', '')
                          .replace('(End)', '').replace('(end)', ''))
            i = j+1
        else:
            merged.append(lst[i])
            i += 1

    return merged
    
#________________________________________________________________________

class head_builder:

    def __call__(self, doc):
        head = r"<div align='center'><b><a href='http://oeis.org/A{:06d}'>A{:06d}</a></b>: <i>{}</i><br></div>".format(
                doc['number'], doc['number'], doc['name'], ) + "\n\nby {}".format(doc['author'])
        return head
        
class keyword_builder:
    
    def __call__(self, doc):
        keyword = "\n_Keywords_: `{}`".format(doc['keyword'])
        return keyword
        
class ListData:

    def __call__(self, caller, doc):

        seq = doc['data'].split(',')[:caller.upper_limit]
        array_template = r'''
$$
\begin{env}{{c|{nel}}}
n & {nat} \\
\hline
{id}(n) & {seq}
\end{env}
$$
'''.format(env="{array}",
           nel='c'*len(seq), 
           nat=" & ".join([str(i) for i in range(int(doc['offset'].split(',')[0]), len(seq))]),
           id="A{:06d}".format(doc['number']), 
           seq = " & ".join(seq))

        return array_template
        

class TableData:

    def __call__(self, caller, doc):

        seq = doc['data'].split(',')#[:caller.upper_limit]
        n, k = caller.upper_limit

        rows = r'\\'.join([' & '.join([str(i)] + [seq[index] if j <= i else '' for j in range(k) for index in [i*(i+1)//2 + j] if index < len(seq)]) for i in range(n)])

        array_template = r'''
$$
\begin{env}{{c|{nel}}}
n, k & {nat} \\
\hline
{rows}
\end{env}
$$
'''.format(env="{array}",
           nel='c' * (k+1), 
           nat=" & ".join([str(i) for i in range(int(doc['offset'].split(',')[0]), k)]),
           rows=rows)

        return array_template

class data_builder:
    
    def __init__(self, upper_limit, representation):
        self.upper_limit = upper_limit
        self.representation = representation
    
    def __call__(self, doc):

        data = "\n_Data_:\n{}".format(self.representation(self, doc))
        return data
    
class content_builder:
    
    def __init__(self, filter_pred):
        self.filter_pred = filter_pred
    
    def __call__(self, content):
        mapped = map(lambda pair: pair[1],
                     filter(lambda pair: self.filter_pred(pair[0], pair[1].lower()), 
                            zip(count(), map(promote_id_anchors, merge_splitted_text(content)))))
        return list(mapped)
    

class comment_builder(content_builder):
    
    def __call__(self, doc):
        
        if 'comment' not in doc: return ""
        
        comments = super(comment_builder, self).__call__(doc['comment'])
        return ("\n_Comments_:\n   - " + "\n   - ".join(comments)) if comments else ""

class formula_builder(content_builder):
    
    def __call__(self, doc):
        
        if 'formula' not in doc: return ""
        
        formulae = super(formula_builder, self).__call__(doc['formula'])
        return ("\n_Formulae_:\n   - " + "\n   - ".join(formulae)) if formulae else ""
    
class xref_builder(content_builder):
    
    def __call__(self, doc):
        
        if 'xref' not in doc: return ""
        
        xrefs = super(xref_builder, self).__call__(doc['xref'])
        return ("\n_Cross references_:\n   - " + "\n   - ".join(xrefs)) if xrefs else ""

class link_builder(content_builder):
    
    def __call__(self, doc):
        
        if 'link' not in doc: return ""
        
        links = super(link_builder, self).__call__(doc['link'])
        return ("\n_Links_:\n   - " + "\n   - ".join(links)) if links else ""

class reference_builder(content_builder):
    
    def __call__(self, doc):
        
        if 'reference' not in doc: return ""
        
        references = super(reference_builder, self).__call__(doc['reference'])
        return ("\n_References_:\n   - " + "\n   - ".join(references)) if references else ""

#________________________________________________________________________
    
def pretty_print(doc, 
                 head=None,
                 keyword=None, 
                 data_upper_limit=20,
                 data_representation=ListData(), 
                 comment=lambda i, c: True,
                 formula=lambda i, c: True,
                 xref=lambda i, c: True,
                 link=lambda i, c: "broken link" not in c,
                 reference=lambda i, c: True,):
    
    builders = [head_builder(), 
                keyword_builder(), 
                data_builder(upper_limit=data_upper_limit, representation=data_representation), 
                comment_builder(filter_pred=comment), 
                formula_builder(filter_pred=formula), 
                xref_builder(filter_pred=xref),
                link_builder(filter_pred=link), 
                reference_builder(filter_pred=reference)]
    
    descr = "\n".join([builder(doc) for builder in builders])
    return descr


def oeis_search(id=None, seq=None, query="", start=0, table=False, xref=[], **kwds):

    # the following imports are too specific to appear at the top of the module.
    from requests import get
    from IPython.display import Markdown

    
    query_components = [] # a list of query components, as strings to be joined later

    if id: query_components .append("id:A{:06d}".format(id))
    elif seq: query_components .append((", " if isinstance(seq, list) else " ").join(map(str,seq)))
    else: query_components.append(query) 

    if table: query_components .append("keyword:tabl")
    for r in xref: query_components .append("xref:A{:06d}".format(id))
    for k,v in kwds.items(): query_components .append("{}:{}".format(k,v))

    payload = {"fmt": "json", "start": start, "q": ' '.join(query_components)}
    
    try:
        doc_result = get("https://oeis.org/search", params=payload,)
        doc = doc_result.json()
    except:
        raise
        return lambda **pp_kwds: Markdown("<hr>__Connection Error__<hr>")
    
    def searchable(**pp_kwds):
        results_description = "_Results for query: <a href='{url}'>{url}</a>_<br><hr>".format(url=doc_result.url)
        inner_results = [pretty_print(result, data_representation=TableData() if table else ListData(), **pp_kwds) 
                            for result in doc['results']]
        return Markdown(results_description + "\n<hr>".join(inner_results))
    
    return searchable
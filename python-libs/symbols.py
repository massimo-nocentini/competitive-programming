
def lower_greek_symbols(plain_string=True):
    """
    Returns an iterable of *lower* Greek symbols. 
    
    Built by Vim's `:help digraph-table@en` command.
    """
    return 'αβγδεζηθικλμνξοπρςστυφχψω'

def capital_greek_symbols():
    """
    Returns an iterable of *capital* Greek symbols. 
    
    Built by Vim's `:help digraph-table@en` command.
    """
    return "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

def latin_symbols():
    """
    Returns an iterable of Latin symbols. 
    
    Built by Vim's `:help digraph-table@en` command.
    """
    return "ḂḃḆḇḊḋḎḏḐḑḞḟḠḡḢḣḦḧḨḩḰḱḴḵḺḻḾḿṀṁṄṅṈṉṔṕṖṗṘṙṞṟṠṡṪṫṮṯṼṽẀẁẂẃẄẅẆẇẊẋẌẍẎẏẐẑẔẕẖẗẘẙẢảẺẻẼẽỈỉỎỏỦủỲỳỶỷỸỹ"

def light_box_drawings():
    """
    Return an iterable of *light* box symbols.

    Built by Vim's `:help digraph-table@en` command.
    """
    return "─│├┤┬┴┼┌┐└┘"

    

/*
    Taken from here:
    http://stackoverflow.com/questions/801740/c-how-to-draw-a-binary-tree-to-the-console
*/

int _print_t(tnode *tree, int is_left, int offset, int depth, char s[20][255])
{
    char b[20];
    int width = 5;

    if (!tree) return 0;

    sprintf(b, "(%03d)", tree->val);

    int left  = _print_t(tree->left,  1, offset,                depth + 1, s);
    int right = _print_t(tree->right, 0, offset + left + width, depth + 1, s);

#ifdef COMPACT
    for (int i = 0; i < width; i++)
        s[depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (int i = 0; i < width + right; i++)
            s[depth - 1][offset + left + width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';

    } else if (depth && !is_left) {

        for (int i = 0; i < left + width; i++)
            s[depth - 1][offset - width/2 + i] = '-';

        s[depth - 1][offset + left + width/2] = '.';
    }
#else
    for (int i = 0; i < width; i++)
        s[2 * depth][offset + left + i] = b[i];

    if (depth && is_left) {

        for (int i = 0; i < width + right; i++)
            s[2 * depth - 1][offset + left + width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset + left + width + right + width/2] = '+';

    } else if (depth && !is_left) {

        for (int i = 0; i < left + width; i++)
            s[2 * depth - 1][offset - width/2 + i] = '-';

        s[2 * depth - 1][offset + left + width/2] = '+';
        s[2 * depth - 1][offset - width/2 - 1] = '+';
    }
#endif

    return left + width + right;
}

int print_t(tnode *tree)
{
    char s[20][255];
    for (int i = 0; i < 20; i++)
        sprintf(s[i], "%80s", " ");

    _print_t(tree, 0, 0, 0, s);

    for (int i = 0; i < 20; i++)
        printf("%s\n", s[i]);
}

//------------------------------------------------------------------------------
Output:

                           .----------------------(006)-------.                 
                      .--(001)-------.                   .--(008)--.            
                 .--(-02)       .--(003)-------.       (007)     (009)          
       .-------(-06)          (002)       .--(005)                              
  .--(-08)--.                           (004)                                   
(-09)     (-07)                     
or

                                                  (006)                         
                           +------------------------+---------+                 
                         (001)                              (008)               
                      +----+---------+                   +----+----+            
                    (-02)          (003)               (007)     (009)          
                 +----+         +----+---------+                                
               (-06)          (002)          (005)                              
       +---------+                        +----+                                
     (-08)                              (004)                                   
  +----+----+                                                                   
(-09)     (-07)                                                       

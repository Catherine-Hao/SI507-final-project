def printTree(tree, prefix = '', bend = '', answer = ''):
    """Recursively print a Movie Recommendation tree in a human-friendly form.
       TREE is the tree (or subtree) to be printed.
       PREFIX holds characters to be prepended to each printed line.
       BEND is a character string used to print the "corner" of a tree branch.
       ANSWER is a string giving "Yes" or "No" for the current branch."""
    text, left, right = tree
    if left is None  and  right is None:
        print(f'{prefix}{bend}{answer}The movie is {text}')
    else:
        print(f'{prefix}{bend}{answer}{text}')
        if bend == '+-':
            prefix = prefix + '| '
        elif bend == '`-':
            prefix = prefix + '  '
        printTree(left, prefix, '+-', "Yes: ")
        printTree(right, prefix, '`-', "No:  ")


# The {movie} should be substituted with the title of the recommended movie.
Tree = \
    ("Do you have preference for the movie's cerificate?"  ,
        ("Do you have preference for the movie's genre?" ,
            ("Do you have preference for the released year of the movie?",
                ("Do you have preference for the movie's rating?" ,
                    ("Do you have preference for the movie's director?" , 
                        ("Do you have preference for the movie's cast?",
                            ("Do you have preference for the movie's runtime?",
                                ("{movie_runtime}", None, None),
                                ("{movie_no_preference}", None, None)),
                            ("{movie_cast}", None, None)),
                        ("{movie_director}", None, None)),
                    ("{movie_rating}", None, None)),
                ("{movie_year}", None, None)),
            ("{movie_genre}", None, None)),
        ("{movie_certificate}", None, None))
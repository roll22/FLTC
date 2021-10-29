import re

reservedWords = ['Number',
                 'Boolean',
                 'if',
                 'fi',
                 'then',
                 'else',
                 'while',
                 'repeat',
                 'break',
                 'continue',
                 'true',
                 'false',
                 'main',
                 'in',
                 'out',
                 ]
reservedOperatorsSeparators = \
    ['+',
     '-',
     '*',
     '/',
     '%',
     '=',
     '==',
     '!=',
     '>=',
     '<=',
     '>',
     '<',
     '>>',
     '<<',
     '[',
     ']',
     '{',
     '}',
     '(',
     ')',
     ';',
     ':',
     ' ',
     '"',
     "'",
     "and",
     "or",
     "not", ]


def is_identifier(token):
    try:
        # it is an identifier
        if token == re.search("([A-Za-z_]+[A-Za-z_0-9]{0,254}){1,255}", token).group():
            return True
    except Exception:
        pass
    return False


def is_constant(token):
    try:
        # it is a string
        if token == re.search("('.*')", token).group():
            return "STRING"
    except Exception:
        pass

    try:
        # it is a number
        if token == re.search("([-]?[0-9]{0,254})", token).group():
            return "NUMBER"
    except Exception:
        pass


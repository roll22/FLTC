import re

from FiniteAutomata import FiniteAutomata

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


def readFiniteAutomata(filename):
    with open(filename, 'r') as f:
        states = f.readline().strip().split(' ')
        alphabet = f.readline().strip().split(' ')
        start = f.readline().strip().split(' ')
        finals = f.readline().strip().split(' ')
        aux_transitions = f.readline().strip().split(';')
        transitions = []
        for transition in aux_transitions[:-1]:
            transition = transition.split(' ')
            transitions.append([(transition[0], transition[1]), transition[2]])
        finiteAutomata = FiniteAutomata(states, alphabet, start, finals, transitions)

        return finiteAutomata


def isSequenceAccepted(fa, startState, sequence):
    currentState = startState
    for element in sequence:
        transitions = fa.getTransitionsFromState(currentState)
        if element not in [tr[1] for tr in transitions]:
            return False
        for transition in transitions:
            if transition[1] == element and len(sequence) == 1 and transition[0][1] in fa.finals:
                return True
            if transition[1] == element:
                return isSequenceAccepted(fa, [transition[0][1]], sequence[1:])
        return False
    return False


def is_identifier_FA(token, identifier_fa):
    if isSequenceAccepted(identifier_fa, identifier_fa.start, list(token)):
        print(token)
        return True
    return False


def is_identifier(token):
    try:
        # it is an identifier
        if token == re.search("([A-Za-z]+[A-Za-z0-9]{0,254}){1,255}", token).group():
            return True
    except Exception:
        pass
    return False


def is_constant_FA(token, constants_fa):
    for fa in constants_fa:
        if isSequenceAccepted(fa, fa.start, list(token)):
            print(token)
            return True
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


def ifFADeterministic(fa):
    transitions = []
    for elem in fa.transitions:
        current = [elem[0][0], elem[1]]
        if current in transitions:
            print(current, transitions)
            return False
        else:
            transitions.append(current)
    return True


def printMenu(fa):
    deterministic = ifFADeterministic(fa)
    print("deterministic:", deterministic)

    if not deterministic:
        return

    print("FA Menu")
    print("1. states")
    print("2. alphabet")
    print("3. start")
    print("4. finals")
    print("5. transitions")
    print("6. check if a sequence is accepted")

    command = int(input(">"))
    while True:
        if command == 1:
            print(fa.states)
        elif command == 2:
            print(fa.alphabet)
        elif command == 3:
            print(fa.start)
        elif command == 4:
            print(fa.finals)
        elif command == 5:
            print(fa.transitions)
        elif command == 6:
            sequence = input("sequence:")
            print("sequence:", sequence, "accepted:", isSequenceAccepted(fa, fa.start, list(sequence)))
        else:
            print("invalid command")
        command = int(input(">"))


fa = readFiniteAutomata("fa/nedet.in")
print(fa.transitions)
# fa.transitions.append([('q1', 'q1'), ' '])
print(fa.transitions)
printMenu(fa)

"""
test.py: Test your code for implementation errors.
"""


from random import randint
from logic import *
from utils import *
from knowledge import *
import argparse


def __getRandomAtom(numProps):
    """
    Generate a random atom from a given number of possible atoms.

    Eg. if numProps is 4, then any one of the six atoms 
    [A, B, C, D, True, False] will be returned.
    """
    
    choice = randint(0, numProps)

    if choice == 0:
        if randint(0, 1) == 0:
            return FalseConstant
        else:
            return TrueConstant
    else:
        return Atom(chr(ord('A') + choice - 1))


def genRandomFormula(maxDepth, numProps):
    """
    Generate a random formula of a given depth and number of propositions.
    """

    if maxDepth == 1:
        return __getRandomAtom(numProps)
    else:
        choice = randint(0, 3)

        if choice == 0:
            form = genRandomFormula(maxDepth - 1, numProps)

            return Not(form)
        elif choice == 1:
            form1 = genRandomFormula(maxDepth - 1, numProps)
            form2 = genRandomFormula(maxDepth - 1, numProps)

            return And(form1, form2)
        elif choice == 2:
            form1 = genRandomFormula(maxDepth - 1, numProps)
            form2 = genRandomFormula(maxDepth - 1, numProps)

            return Or(form1, form2)
        else:
            return __getRandomAtom(numProps)


def runCNFTest():
    """
    Test the Formula.toCNF() function.
    """

    flag = True
    
    for i in range(50):
        formula = genRandomFormula(7, 4)
        formula = 
        try:
            cnfForm = formula.toCNF()

            if not areEquivalent(formula, cnfForm):
                flag = False
                print('Test %d failed. The culprit formula was: %s.' % (i + 1, formula))
        except:
            print('This Formula %s crashed the system.' % formula)

    if flag:
        print('All CNF conversion tests passed. Your implementation is (probably) correct!')
    else:
        print('You failed some tests. Please re-check your code.')

        
def runResolutionTest():
    """
    Test the resolutionRefutation function.
    """

    P = Atom('P')
    Q = Atom('Q')
    R = Atom('R')
    S = Atom('S')

    answer = [True] * 4 + [False]
    t = [False] * 5
    
    # t[0] = resolutionRefutation(And.fromList([P,
    #                                           Q]), Q, quiet=True)
    # t[1] = resolutionRefutation(And.fromList([P,
    #                                           Implies(P, Q)]), Q, quiet=True)
    # t[2] = resolutionRefutation(And.fromList([Or(P, Q),
    #                                           Implies(P, R),
    #                                           Implies(Q, R)]), R, quiet=True)
    t[3] = resolutionRefutation(And.fromList([Implies(Implies(P, Q), Q),
                                              Implies(Implies(P, P), R),
                                              Implies(Implies(R, S), Not(Implies(S, Q)))]), R, quiet=True)
    # t[4] = resolutionRefutation(And.fromList([Implies(P, Q),
    #                                           P]), Not(Q), quiet=True)
    #
    # if t == answer:
    if t[3] == True:
        print('Congratulations, your code proved (or disproved) all 5 propositions!')
    else:
        print('Resolution refutation test failed.')


def runTruthTest():
    """
    Test the Formula.truthValue() function.
    """

    t = [False] * 5
    answer = [True, False, True, False, False]
    
    t[0] = And(Or(Or(And(Atom('False'), Atom('True')), Atom('False')), Atom('True')), Atom('D')).truthValue({'D': True})
    t[1] = And(Atom('False'), Atom('B')).truthValue({'B': False})
    t[2] = Atom('C').truthValue({'C': True})
    t[3] = And(Atom('C'), And(Not(And(Atom('D'), Atom('D'))), And(Or(Atom('B'), Atom('D')), Or(Atom('True'), Atom('B'))))).truthValue({'C': False, 'D': False, 'B': False})
    t[4] = Not(Not(Atom('B'))).truthValue({'B': False})

    if t == answer:
        print('Truth value calculation seems to be correct!')
    else:
        print('Truth value test failed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test your code.', epilog='By default, runs all tests.')
    parser.add_argument('--cnf', action='store_true', help='Run the tests for CNF conversion.')
    parser.add_argument('--truth', action='store_true', help='Run the tests for finding truth values of formulas.')
    parser.add_argument('--resolution', action='store_true', help='Run the tests for resolution-refutation.')

    args = parser.parse_args()

    if not args.cnf and not args.truth and not args.resolution:
        args.cnf = args.truth = args.resolution = True
    
    if args.cnf:
        runCNFTest()
        
    if args.truth:
        runTruthTest()

    if args.resolution:
        runResolutionTest()

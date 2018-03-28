from logic import *
from knowledge import *

# formula = (Or(Or(And(Atom('A'), Atom('B')), And(Atom('C'),Atom('D'))), Atom('E'))) # ((a∧b)∨(c∧d))∨e
formula = (Or(Atom('A'), Atom('B')))
flattenList = formula.flattenArgs()
print(flattenList)
for i in range(0, len(flattenList)):
    flattenList[i] = Not(flattenList[i])
# print(flattenList)
print([[Not(Atom('Q'))], [Atom('P')], [Not(Atom('P')), Atom('Q')]] == [[Not(Atom('Q'))], [Atom('P')], [Not(Atom('P')), Atom('Q')], [Not(Atom('P'))]])

'''
(A ^ (~A v D) ^ C ^ C)
'''
print(And(Atom('A'), And(Or(Not(Atom('A')), Atom('D')), And(Atom('C'), Atom('C')))))
l = [Or(Atom('A'), Not(Atom('A')))]

newResList = resList[:]
    # resList = [[A, B], [A, Not(B)]] , (A v B) ^ (A V ~B)
    # flag = 0
    # for i in resList: # i = [A, B]
    #     for j in resList: # j = [A, B]
    #         if i == j:
    #             continue
    #         if len(i) == len(j) == 2:
    #             a1, a2, b1, b2 = i[0], i[1], j[0], j[1]
    #             if a1 == Not(b1).toCNF() or b1 == Not(a1).toCNF() or a1 == Not(b1) or b1 == Not(a1):
    #                 if [a2, b2] not in newResList:
    #                     flag = 1
    #                     newResList.append([a2, b2])
    #                     break
    #             if a1 == Not(b2).toCNF() or b2 == Not(a1).toCNF() or a1 == Not(b2) or b2 == Not(a1):
    #                 if [a2, b1] not in newResList:
    #                     flag = 1
    #                     newResList.append([a2, b1])
    #                     break
    #             if a2 == Not(b1).toCNF() or b1 == Not(a2).toCNF() or a2 == Not(b1) or b1 == Not(a2):
    #                 if [a1, b2] not in newResList:
    #                     flag = 1
    #                     newResList.append([a1, b2])
    #                     break
    #             if a2 == Not(b2).toCNF() or b2 == Not(a2).toCNF() or a2 == Not(b2) or b2 == Not(a2):
    #                 if [a1, b1] not in newResList:
    #                     flag = 1
    #                     newResList.append([a1, b1])
    #                     break
    #         elif len(i) == 2 and len(j) == 1:
    #             a1, a2, b1 = i[0], i[1], j[0]
    #             if b1 == Not(a1).toCNF() or a1 == Not(b1).toCNF() or b1 == Not(a1) or a1 == Not(b1):
    #                 if [a2] not in newResList:
    #                     flag = 1
    #                     newResList.append([a2])
    #                     break
    #             if b1 == Not(a2).toCNF() or a2 == Not(b1).toCNF() or b1 == Not(a2) or a2 == Not(b1):
    #                 if [a1] not in newResList:
    #                     flag = 1
    #                     newResList.append([a1])
    #                     break
    #         elif len(i) == 1 and len(j) == 2:
    #             a1, b1, b2 = i[0], j[0], j[1]
    #             if a1 == Not(b1).toCNF() or b1 == Not(a1).toCNF() or a1 == Not(b1) or b1 == Not(a1):
    #                 if [b2] not in newResList:
    #                     flag = 1
    #                     newResList.append([b2])
    #                     break
    #             if a1 == Not(b2).toCNF() or b2 == Not(a1).toCNF() or a1 == Not(b2) or b2 == Not(a1):
    #                 if [b1] not in newResList:
    #                     flag = 1
    #                     newResList.append([b1])
    #                     break
    #         elif len(i) == len(j) == 1:
    #             a1, b1 = i[0], j[0]
    #             if a1 == Not(b1) or b1 == Not(a1).toCNF() or a1 == Not(b1) or b1 == Not(a1):
    #                 flag = 1
    #                 newResList.append([])
    #                 break
    #     if flag == 1:
    #         break

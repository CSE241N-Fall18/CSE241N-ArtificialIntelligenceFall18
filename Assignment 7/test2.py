from graph import *
from search import *
from util import *
import traceback
import argparse
#import random
#random.seed(1)

def testSearch():
    searchFunctions = [("Hill climbing", searchHillClimbing),
                       ("Beam", searchBeam),
                       ("Best first", searchBestFirst),
                       ("A*", searchAStar)
                      ]

    for i in range(4000):
        g, start, goal = randomGridSearch(30, 30)
        #print('Test %d' % (i + 1))

        for (name, f) in searchFunctions:
            try:
                if name=="Hill climbing":
                    path1 = f(g, start, goal)

                    if goal not in path1:
                        # print('%s - path not found.' % name)
                        # print('Sart: %s, goal: %s' % (start, goal))
                        # print(g)
                        path1={}
                    else:
                        node = goal
                        #print('%s - path found with cost %d.' % (name, len(path1) - 1))
                if name=="Beam":
                    path2 = f(g, start, goal)

                    if goal not in path2:
                        # print('%s - path not found.' % name)
                        # print('Sart: %s, goal: %s' % (start, goal))
                        # print(g)
                        path2={}
                    else:
                        node = goal
                        #print('%s - path found with cost %d.' % (name, len(path2) - 1))
                if name=="Best first":
                    path3 = f(g, start, goal)

                    if goal not in path3:
                        # print('%s - path not found.' % name)
                        # print('Sart: %s, goal: %s' % (start, goal))
                        # print(g)
                        path3={}
                    else:
                        node = goal
                        #print('%s - path found with cost %d.' % (name, len(path3) - 1))
                if name=="A*":
                    path4 = f(g, start, goal)

                    if goal not in path4:
                        # print('%s - path not found.' % name)
                        # print('Sart: %s, goal: %s' % (start, goal))
                        # print(g)
                        path4={}
                    else:
                        node = goal
                        #print('%s - path found with cost %d.' % (name, len(path4) - 1))
                    if(len(path4)>len(path3) or len(path4)>len(path2) or len(path4)>len(path1)):
                        if(len(path4) ==0 or len(path3)==0 or len(path2)==0 or len(path1)==0):
                            continue
                        print(len(path1))
                        print(len(path2))
                        print(len(path3))
                        print(len(path4))
                        print(path4)
                        print()



            except:
                traceback.print_exc()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test your code.', epilog='Runs all tests.')
    parser.parse_args()

    testSearch()



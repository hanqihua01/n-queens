from z3 import *

def solveNQueens(n):
    '''a function to solve n-queens problem'''
    # initialize map
    map = []
    for i in range(n):
        map.append([])
        for j in range(n):
            map[i].append(Bool('map['+str(i)+']['+str(j)+']'))
    # set constrains
    s = Solver()
    for i in range(n):
        s.add(Or(map[i])) # at least one true in each row
        for j in range(n):
            for k in range(n): # set row and column constrains
                if i != k:
                    s.add(Implies(map[i][j], Not(map[k][j]))) # row constrains
                if j != k:
                    s.add(Implies(map[i][j], Not(map[i][k]))) # column constrains
            tempi = i - 1
            tempj = j - 1
            while(tempi >= 0 and tempj >= 0):
                s.add(Implies(map[i][j], Not(map[tempi][tempj])))
                tempi -= 1
                tempj -= 1
            tempi = i - 1
            tempj = j + 1
            while(tempi >= 0 and tempj < n):
                s.add(Implies(map[i][j], Not(map[tempi][tempj])))
                tempi -= 1
                tempj += 1
            tempi = i + 1
            tempj = j - 1
            while(tempi < n and tempj >= 0):
                s.add(Implies(map[i][j], Not(map[tempi][tempj])))
                tempi += 1
                tempj -= 1
            tempi = i + 1
            tempj = j + 1
            while(tempi < n and tempj < n):
                s.add(Implies(map[i][j], Not(map[tempi][tempj])))
                tempi += 1
                tempj += 1
    # output
    if s.check() == sat:
        print(s.model())

solveNQueens(5)
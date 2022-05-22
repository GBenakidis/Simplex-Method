import numpy as np

def positive_array(arr):
    for x in arr:
        if x < 0:
            return False
    return True


def check_positive_restrictions(p):
    for i in range(0, len(p)):
        for j in range(0, len(p[i])):
            if(p[i][j] < 0):
                print('Found a negative number!')
                exit()
    print('Every number was positive!\n')


def typicalForm(r, I):
    return np.hstack((r, I))


def identity_array(size):
    return np.identity(size)


def P_array_creator(r):
    p = np.array([])
    for i in range(0, len(r)):
        p = np.append(p, r[i][len(r[i])-1])
    
    return p


def Restrictions_P_var_remover(r):
    return r[:, :-1]


def max_z_typicalForm(m, N):
    return np.pad(m, (0, N), 'constant')


def zj_ci_creator(m):
    p = np.array([])
    for i in range(0, len(m)):
        p = np.append(p, -abs(m[i]))
    return p

def arrayPrinter(max_z_typical,flow_chart_with_identity_array,zj_ci,P):
    print('MaxZ Typical Form:')
    print(max_z_typical)
    print('\nFlow chart with identity:')
    print(flow_chart_with_identity_array)
    print('\nzj-ci array:')
    print(zj_ci)
    print('\nP:')
    print(P)
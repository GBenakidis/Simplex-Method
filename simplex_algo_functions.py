import numpy as np

def found_negative(p):
    return any(p < 0)

def pivot_fun(fi, zj_ci, P):
    snc = np.where(zj_ci < 0)[0]
    if len(snc) == 0:
        return None  # No negative values in zj_ci, terminate
    
    pivotCol = snc[0]
    
    theta_values = [P[i] / fi[i][pivotCol] if fi[i][pivotCol] > 0 else float('inf') for i in range(len(P))]
    spother_row = np.argmin(theta_values)
    
    pivot = fi[spother_row][pivotCol]
    
    return pivot, spother_row, pivotCol

def rowDivider(fi, divider, row):
    fi[row] = fi[row] / divider

def multiSubRow(fi, multier, new_row, starting_row):
    fi[new_row] -= multier * fi[starting_row]

def multiSumRow(fi, multier, new_row, starting_row):
    fi[new_row] += multier * fi[starting_row]

def otherPivot(fi, row, col):
    return fi[row][col]

import numpy as np

def simplex_algo(flow_chart_with_identity_array, P):
    fi = flow_chart_with_identity_array.copy()
    zj_ci = np.dot(fi.T, P) - P

    roundCounter = 0
    lastP = 0
    baseSaver = []

    while np.any(zj_ci < 0):
        roundCounter += 1
        print('================= REPETITION: ' + str(roundCounter) + '==========')
        pivot_info = pivot_fun(fi, zj_ci, P)
        
        if pivot_info is None:
            print('No negative values in zj_ci. Terminating.')
            break
        
        pivotNum, pivotRow, pivotCol = pivot_info
        baseSaver.append(pivotCol + 1)

        # Pivot row operations
        pivot_vector = fi[pivotRow] / pivotNum
        fi[pivotRow] = pivot_vector
        P[pivotRow] /= pivotNum

        # Other row operations
        pivot_row_vector = fi[pivotRow]
        for row in range(len(fi)):
            if row == pivotRow:
                continue
            other_pivot = fi[row, pivotCol]
            multier = other_pivot / pivotNum
            if multier > 0:
                fi[row] -= multier * pivot_row_vector
                P[row] -= multier * P[pivotRow]
            elif multier < 0:
                fi[row] += -multier * pivot_row_vector
                P[row] += -multier * P[pivotRow]

        # Update zj_ci
        lastP -= zj_ci[pivotCol] * P[pivotRow]
        zj_ci -= zj_ci[pivotCol] * pivot_row_vector

    print('\n\nSo we end up with the optimal solution:')
    for i in range(len(baseSaver)):
        variable_index = int(baseSaver[i])
        variable_value = P[i]
        print(f'x{variable_index} = {variable_value}')

    print('\nNumber of repetitions:', roundCounter)
    return lastP

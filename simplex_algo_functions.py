import numpy as np


def found_negative(p):
    for i in range(0, len(p)):
        if(p[i] < 0):
            return True
    return False


def smaller_negative_num_column(zc):
    n = np.where(zc == np.amin(zc))
    return n


def pivot_finder(fi, col, row):
    return fi[int(row)][int(col)]


def smallestPositiveNumLoc(t):
    min = t[0]
    loc = 0
    for i in range(0, len(t)):
        if(t[i]<=min):
            min = t[i]
            loc = i
    return loc


def pivot_vector_creator(pivotNum, fi_row_len):
    v = np.array([])
    for i in range(0, fi_row_len):
        v = np.append(v, pivotNum)
    return v


def rowDivider(fi, divider, row):
    fi[row] = fi[row]/divider
    return fi


def multiSubRow(fi, multier, new_row, starting_row):
    fi[new_row]=fi[new_row]-(multier*fi[starting_row])
    return fi


def multiSumRow(fi, multier, new_row, starting_row):
    fi[new_row] = fi[new_row]+(multier*fi[starting_row])
    return fi


def nextRow(row):
    if(row == 0):
        return 1
    else:
        return 0


def otherPivot(fi, row, col):
    return fi[row][col]


def printArrays(fi, zj_ci, P, lastP):
    print('\nTo fi einai:')
    print(fi)
    print('\nTo zj-cj einai:')
    print(zj_ci)
    print('\nTo P einai')
    print(P)
    print(lastP)


def theta_creator(fi, P, snc):
    theta = np.array([])
    print('\nCalculating theta values for each row:')
    for i in range(0, len(P)):
        print('--- FOR ROW: ' + str(i))
        print('P[i] is ' + str(P[i]))
        print('fi is ' + str(fi[i][snc]))
        k = P[i]/fi[i][snc]
        print('The theta value is: ' + str(k))
        theta = np.append(theta, k)
    return theta
    

def pivot_fun(fi, zj_ci, P):
    print('\n==== Obtain pivot =====')

    # Find smaller negative in zj-ci and return COLUMN
    snc = smaller_negative_num_column(zj_ci)
    print(
        '\nPosition of smaller negative number in zj-ci is at column : ' + str(snc[0]))

    # Create and calculate theta array from 'flow_chart_with_identity_array' array and P array, and return it
    theta = theta_creator(fi, P, snc)
    print('\nTheta array is: ')
    print(theta)

    # From theta array obtain smaller positive number and return ROW number
    # spother_row: smaller positive num row
    spother_row = smallestPositiveNumLoc(theta)
    print('\nPosition of smaller positive number in theta is at row : ' + str(spother_row))
    print('Firts: ' + str(theta[0]))

    # With row number(spother_row) and column number(snc), target the correct element in 'flow_chart_with_identity_array' array which will be our pivot
    pivot = pivot_finder(fi, snc[0], spother_row)
    print('So our pivot is: ' + str(pivot))

    pivotInfo = [pivot, spother_row, snc[0]]
    return pivotInfo


def updateMinusP(P, other_pivotRow, pivot, pivotRow):
    return P[other_pivotRow]-(pivot*P[pivotRow])


def updatePlusP(P, other_pivotRow, pivot, pivotRow):
    return P[other_pivotRow]+(pivot*P[pivotRow])

def simplex_algo(fi, zj_ci, P):
    roundCounter = 0
    lastP = 0
    baseSaver = np.array([])
    while(found_negative(zj_ci)):
        roundCounter += 1
        print('================= REPETITION: ' + str(roundCounter) + '==========')
        pivotInfo = pivot_fun(fi, zj_ci, P)
        pivotNum = pivotInfo[0]
        pivotRow = int(pivotInfo[1])
        pivotCol = int(pivotInfo[2])
        baseSaver = np.append(baseSaver, pivotCol+1)
        print('\n==== Do calculations per row =====')
        # From 'flow_chart_with_identity_array' array, to pivot's row, divide with pivot all the row
        # Creating pivot as an vector to divide row
        pivot_vector = pivot_vector_creator(pivotNum, len(fi[0]))
        fi = rowDivider(fi, pivot_vector, pivotRow)
        P[pivotRow] = P[pivotRow]/pivotNum
        print('\n-- Calculation for row: ' + str(pivotRow) + ' --')
        printArrays(fi, zj_ci, P, lastP)

        # From 'flow_chart_with_identity_array' array, to the other row, multi with pivot's under number the 'pivot's row'
        # and sub the current row
        other_row = nextRow(pivotRow)
        other_pivot = otherPivot(fi, other_row, pivotCol)
        other_pivot_vector = pivot_vector_creator(other_pivot, len(fi[0]))

        if(other_pivot>0):
            fi = multiSubRow(fi, other_pivot_vector, other_row, pivotRow)
            P[other_row] = updateMinusP(P, other_row, other_pivot, pivotRow)
        else:
            fi = multiSumRow(fi, other_pivot_vector, other_row, pivotRow)
            P[other_row] = updatePlusP(P, other_row, other_pivot, pivotRow)

        print('\n-- Calculation for row: ' + str(other_row) + ' --')
        printArrays(fi, zj_ci, P, lastP)

        # From 'zj_ci' array, multi with pivot's under number
        lastP = lastP - (zj_ci[pivotCol]*P[pivotCol])
        zj_ci = zj_ci - (zj_ci[pivotCol]*fi[pivotRow])
        
        print('\n-- Calculation for row: 3' + ' --')
        printArrays(fi, zj_ci, P, lastP)
        baseSaver = np.append(baseSaver, P[pivotRow])
        

    # Returning array with most efficient variables
    print('\n\nSo we end up with optimal solution:')
    x1_index = np.where(baseSaver == 1)
    if(x1_index[0] != -1):
        print('x'+str(baseSaver[int(x1_index[0])]) + '=' + str(baseSaver[x1_index[0]+1]))
    else:
        print('x1=0')

    x2_index = np.where(baseSaver == 2)
    if(x2_index[0] != -1):
        print('x'+str(baseSaver[int(x2_index[0])]) + '=' + str(baseSaver[x2_index[0]+1]))
    else:
        print('x2=0')

    x3_index = np.where(baseSaver == 3)
    if(x3_index[0] != -1):
        print('x'+str(baseSaver[int(x3_index[0])]) + '=' + str(baseSaver[x3_index[0]+1]))
    else:
        print('x3=0')
    print('\nNumber of repetitions: ' + str(roundCounter))
    return lastP

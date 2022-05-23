import numpy as np


def found_negative(p):
    for i in range(0, len(p)):
        if(p[i] < 0):
            return True
    return False


def smaller_negative_num_column(zc):
    n = np.where(zc == np.amin(zc))
    return n


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

def pivot_fun(fi, zj_ci, P):
    print('\n==== Obtain pivot =====')
    # TODO-PIVOT 1
    # Find smaller negative in zj-ci and return COLUMN
    snc = smaller_negative_num_column(zj_ci)
    print('\nPosition of smaller negative number in zj-ci is at column : ' + str(snc[0]))

    # TODO-PIVOT 2
    # Create and calculate theta array from 'flow_chart_with_identity_array' array and P array, and return it
    theta = theta_creator(fi, P, snc)
    print('\nTheta array is: ')
    print(theta)

    # TODO-PIVOT 3
    # From theta array obtain smaller positive number and return ROW number
    # spnr: smaller positive num row
    spnr = smallestPositiveNumLoc(theta)
    print('\nPosition of smaller positive number in theta is at row : ' + str(spnr))
    print('Firts: ' + str(theta[0]))

    # TODO-PIVOT 4
    # With row number(spnr) and column number(snc), target the correct element in 'flow_chart_with_identity_array' array which will be our pivot
    pivot = pivot_finder(fi, snc[0], spnr)
    print('So our pivot is: ' + str(pivot))

    pivotInfo = [pivot, spnr, snc[0]]
    return pivotInfo


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


def simplex_algo(fi, zj_ci, P):
    roundCounter = 1
    lastP = 0
    while(found_negative(zj_ci)):
        print('================= REPETITION: ' + str(roundCounter))
        pivotInfo = pivot_fun(fi, zj_ci, P)
        pivotNum = pivotInfo[0]
        pivotRow = int(pivotInfo[1])
        pivotCol = int(pivotInfo[2])

        print('\n==== Do calculations per row =====')
        # TODO-CALCS 1
        # From 'flow_chart_with_identity_array' array, to pivot's row, divide with pivot all the row
        # Creating pivot as an vector to divide row
        pv = pivot_vector_creator(pivotNum, len(fi[0]))
        fi = rowDivider(fi, pv, pivotRow)
        P[pivotRow] = P[pivotRow]/pivotNum
        print('\n-- Calculation for row: ' + str(pivotRow))
        printArrays(fi, zj_ci, P, lastP)

        # TODO-CALCS 2
        # From 'flow_chart_with_identity_array' array, to the other row, multi with pivot's under number the 'pivot's row'
        # and sub the current row
        nr = nextRow(pivotRow)
        op = otherPivot(fi, nr, pivotCol)
        opv = pivot_vector_creator(op, len(fi[0]))
        print('The next row we will divide is: ' + str(nr))
        print('The next pivot is: ' + str(op) + '\n')
        if(op>0):
            fi = multiSubRow(fi, opv, nr, pivotRow)
            P[nr]=P[nr]-(op*P[pivotRow])
        else:
            fi = multiSumRow(fi, opv, nr, pivotRow)
            P[nr]=P[nr]+(op*P[pivotRow])
        print('\n-- Calculation for row: ' + str(nr))
        printArrays(fi, zj_ci, P, lastP)

        # TODO-CALCS 3
        # From 'zj_ci' array, multi with pivot's under number
        lastP = lastP - (zj_ci[pivotCol]*P[pivotCol])
        zj_ci = zj_ci - (zj_ci[pivotCol]*fi[pivotRow])
        
        print('\n-- Calculation for row: 3')
        printArrays(fi, zj_ci, P, lastP)
        roundCounter+=1

    # Returning array with most efficient variables

    return lastP

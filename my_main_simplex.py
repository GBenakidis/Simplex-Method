import numpy as np
from main_transformations import process_restrictions, typicalForm, arrayPrinter
from simplex_algo_functions import check_positive_restrictions, simplex_algo

def main():
    max_z = np.array([20, 25, 15])
    restrictions = np.array([1.5, 2, 1, 16], [4, 3, 2, 20])
    
    # Check if there are negative numbers in restrictions
    check_positive_restrictions(restrictions)

    P, R, extra_vars_add = process_restrictions(restrictions, max_z)
    flow_chart_with_identity_array = typicalForm(R, extra_vars_add)
    arrayPrinter(max_z, flow_chart_with_identity_array, P)
    
    max_z_value = simplex_algo(flow_chart_with_identity_array, P)
    print('\nMaxZ = ' + str(max_z_value))

if __name__ == "__main":
    main()

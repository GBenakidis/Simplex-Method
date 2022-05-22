from main_transformations import *
from simplex_algo_functions import *
import numpy as np

def main():
    max_z = np.array([20, 25, 20])
    restrictions = np.array([[0.2, 0.3, 0.2, 8], [0.4, 0.4, 0.5, 15]])
    check_positive_restrictions(restrictions)

    P = P_array_creator(restrictions)
    R = Restrictions_P_var_remover(restrictions)
    typical_form_number_of_variables = len(restrictions) + len(max_z)

    # Size of identity array should be the total number of variables the typical form has
    # minus the total number of variables for restrictions
    extra_vars_add = typical_form_number_of_variables - (len(restrictions[0]) - 1)

    I = identity_array(extra_vars_add)
    max_z_typical = max_z_typicalForm(max_z, extra_vars_add)
    zj_ci = zj_ci_creator(max_z_typical)
    flow_chart_with_identity_array = typicalForm(R, I)
    
    print(max_z_typical)
    print(flow_chart_with_identity_array)
    print(zj_ci)
    print(P)
    simplex_algo(flow_chart_with_identity_array, zj_ci, P)


if __name__ == "__main__":
    main()

import numpy as np

def process_restrictions(restrictions, max_z):
    # Extract P and R arrays from restrictions
    P = restrictions[:, -1]
    R = restrictions[:, :-1]
    
    typical_form_number_of_variables = len(restrictions) + len(max_z)
    
    # Calculate the number of extra variables to add
    extra_vars_add = typical_form_number_of_variables - len(R[0])
    
    return P, R, extra_vars_add

def typicalForm(R, extra_vars_add):
    identity_matrix = np.identity(extra_vars_add)
    return np.hstack((R, identity_matrix))

def arrayPrinter(max_z, flow_chart_with_identity_array, P):
    print('MaxZ:')
    print(max_z)
    print('\nFlow chart with identity:')
    print(flow_chart_with_identity_array)
    print('\nP:')
    print(P)

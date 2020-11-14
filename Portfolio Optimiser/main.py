import dimod
from dimod.reference.samplers import ExactSolver

hi_dict = {}
J_i_j = {}

Cov_Ri_Rj = [[]]
A = []
B = 1000

Number_of_data = 100
theta_1 = 0.33
theta_2 = 0.33
theta_3 = 0.33

gamma = theta_3*B**2

for i in range(Number_of_data):
    hi_dict['Z{}'.format(i+1)] = -0.5*(theta_2*Cov_Ri_Rj[i][i]+
                                       theta_3*A[i]**2 -
                                       theta_1*E[i]-
                                       2*B*theta_3*A[i])
    for j in range(i+1, Number_of_data):
        J_i_j['Z{}'.format(i+1),
              'Z{}'.format(j+1)] = -0.25*(theta_2*Cov_Ri_Rj[i][j]+
                                          theta_3*A[i]*A[j])

BQM = dimod.BinaryQuadraticModel(hi_dict,
                                     J_i_j,
                                     gamma, 'BINARY')
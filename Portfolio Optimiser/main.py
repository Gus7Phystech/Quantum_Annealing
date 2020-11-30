import dimod
from dimod.reference.samplers import ExactSolver
from sklearn import preprocessing
import numpy as np

stock_names = ['GAZP.ME', 'TSLA', 'BP', 'AAPL', 'GOOG', 'SBER.ME']


hi_dict = {}
J_i_j = {}


Cov_Ri_Rj = [[0.1730411793895688, 0.16848257055484364, 0.01601183080811324, 0.2132821791154161, 0.07183115371768098, 0.08243603669609552], [0.16848257055484364, 2.1080099999691955, -0.12127125120858186, 0.7907527175589656, 0.2181229832512204, 0.12827505799400826], [0.01601183080811324, -0.12127125120858186, 0.05705202617391969, -0.03935822797108192, 0.006344259090761413, 0.02272925895947395], [0.2132821791154161, 0.7907527175589656, -0.03935822797108192, 0.47482264631017784, 0.14510454764404163, 0.12424599285022221], [0.07183115371768098, 0.2181229832512204, 0.006344259090761413, 0.14510454764404163, 0.0523807141972014, 0.046996721188596026], [0.08243603669609552, 0.12827505799400826, 0.02272925895947395, 0.12424599285022221, 0.046996721188596026, 0.05679540879334264]]
E = [17.95, 40.85, 1.88, 11.92, 177.70, 24.11]
for i in range(6):
    E[i] *= 3
Ex = preprocessing.normalize([E])
for i in range(6):
    E[i] = Ex[0][i]/10*3

A = [179.5, 408.5, 18.79, 119.26, 1777.02, 241.05]
Ax = preprocessing.normalize([A])
A = Ax[0]
B = 2

Number_of_data = 6
theta_1 = 0.33
theta_2 = 0.33
theta_3 = 0.33

gamma = theta_3*B**2

for i in range(Number_of_data):
    hi_dict['Z{}'.format(i+1)] = 0.5*(theta_2*Cov_Ri_Rj[i][i]+
                                       theta_3*A[i]**2 -
                                       theta_1*E[i]-
                                       2*B*theta_3*A[i])
    for j in range(i+1, Number_of_data):
        J_i_j['Z{}'.format(i+1),
              'Z{}'.format(j+1)] = 0.25*(theta_2*Cov_Ri_Rj[i][j]+
                                          theta_3*A[i]*A[j])

BQM = dimod.BinaryQuadraticModel(hi_dict,
                                     J_i_j,
                                     gamma, 'BINARY')
sampler = ExactSolver()
sampled = sampler.sample(BQM)

print(sampled)

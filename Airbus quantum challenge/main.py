import dimod
from dimod.reference.samplers import ExactSolver
import xlrd

book = xlrd.open_workbook('containers.xlsx')
sheet = book.sheet_by_index(0)

t = []
m = []
for i in range(15):
    t.append(sheet.cell(i+1, 1).value)
    m.append(sheet.cell(i+1, 2).value)
for i in range(15):
    t.append(sheet.cell(i + 1, 4).value)
    m.append(sheet.cell(i + 1, 5).value)

h_a_dict = {}
J_a_b_dict = {}

L = 100
N = 20
n = 30

W_p = 40 # *10**3
W_e = 120 # *10**3

x_cg_e = -0.05*L
x_cg_min = -0.1*L
x_cg_max = 0.2*L
x_cg_t = 0.1*L
S_0_max = 22*10**3


for i in range(n):
    for k in range(N):
        j = -int(N/2-0.5) + k
        h_a_dict['Z{}_{}'.format(i, j)] = -2*W_p*m[i] + m[i]**2 - 2*N*t[i] + t[i]**2 + W_e*(x_cg_e - x_cg_max)*m[i]*(L/N*j-x_cg_min) + \
            W_e*(x_cg_e - x_cg_min)*m[i]*(L/N*j-x_cg_max) + m[i]**2*(L/N*j - x_cg_min)*(L/N*j - x_cg_max) + \
            2*W_e*(x_cg_e - x_cg_t)*m[i]*(L/N*j-x_cg_t) + m[i]**2*(L/N*j-x_cg_t)**2 + t[i] + 1
        for i_1 in range(n):
            for k_1 in range(N):
                j_1 = -int(N/2-0.5) + k_1
                J_a_b_dict['Z{}_{}'.format(i, j),
                           'Z{}_{}'.format(i_1, j_1)] = 2*m[i]*m[i_1] + 2*t[i]*t[i_1] + 2*m[i]*m[i_1]*(L/N*j-x_cg_min)*(L/N*j_1-x_cg_max) + \
                    2*m[i]*m[i_1]*(L/N*j-x_cg_t)*(L/N*j_1-x_cg_t)

gamma = W_p**2 + N**2 + W_e**2*(x_cg_e - x_cg_min)*(x_cg_e - x_cg_max) + W_e**2*(x_cg_e - x_cg_t)**2 - N - n

BQM = dimod.BinaryQuadraticModel(h_a_dict, J_a_b_dict, gamma, 'BINARY')

sampler = ExactSolver()
sampled = sampler.sample(BQM)

print(sampled)

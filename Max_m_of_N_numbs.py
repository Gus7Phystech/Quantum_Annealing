import math
import random

import dimod
from dimod.reference.samplers import ExactSolver


'''
func maxsubset(in_array, m) gets array and lenght of needed subarray with maximum sum.
It returns required subarray

hand_test() right after the start applies maxsubset and prints the answer unless you type 'exit' 
'''

def sample_BQM(BQM):
    '''
    :param BQM: BQM model
    :return: simplified model
    '''
    sampler = ExactSolver()
    return sampler.sample(BQM)


def max_subset(in_array, m):
    '''
        o(n) - we take the subset with the minimum of energy

        :param N: lenght of in_array
        :param in_array: array of integers
        :param m: number of needed numbers

        :return: ans - answer for the problem
    '''
    N = len(in_array)
    # filling BQM
    #minimising (|x_1|+...+|x_N|)*(m-(q_1+q_2+...+q_N))^2 - (x_1*q_1+...+x_N*q_N)
    #remembering q_i^2 = q_i

    sum_of_abs_x_i = 0 #const
    for i in range(N):
        sum_of_abs_x_i += abs(in_array[i])

    dict_q_i = {}
    dict_q_i_q_j = {}
    BQM_const = sum_of_abs_x_i*m**2
    for i in range(N):
        dict_q_i['q{}'.format(i + 1)] = (1 - 2*m)*sum_of_abs_x_i - in_array[i] #(q_i^2 - 2*m*q_i)
        for j in range(i+1, N):
            dict_q_i_q_j[('q{}'.format(i + 1), 'q{}'.format(j + 1))] = 2*sum_of_abs_x_i

    BQM = dimod.BinaryQuadraticModel(dict_q_i,
                                     dict_q_i_q_j,
                                     BQM_const, 'BINARY')
    sampled_BQM = sample_BQM(BQM)

    #forming the answer
    ans = []  # here will be the answer
    for i in range(N):
        if sampled_BQM.first.sample['q{}'.format(i + 1)] == 1:  # if we took x_i from model
            ans.append(in_array[i])  # write in answer.

    # return subset
    return ans

def hand_test():
    while 1:
        try:
            in_array = list(map(int, input("Please, input an array to find a maximum subset (type 'exit' to exit): ").split()))  # input
            m = int(input("lenght of needed subset: "))
        except:
            break

        print(*max_subset(in_array, m))
        print()

if __name__ == '__main__':
    hand_test()
import random

import dimod
from dimod.reference.samplers import ExactSolver

#
#public variables:
Max_of_N_BQM = 0
Max_of_N_dict = {}

def create_rand_set(m_elem, m_len):
    a = []
    for i in range(random.randint(1, m_len)):
        a.append(random.randint(-m_elem, m_elem))
    return a


def auto_test():
    for i in range(10):
        arr = create_rand_set(10, 15)
        print("Given", arr)
        given_ans = apply_func(arr)
        print("Ans by alg", given_ans)
        right_ans_1 = [i for i in arr if i >= 0]
        right_ans_2 = [i for i in arr if i > 0]
        print("Right ans", right_ans_1, right_ans_2)
        print(sorted(given_ans) == sorted(right_ans_1) or sorted(given_ans) == sorted(right_ans_2))
        print()


def sample_BQM(BQM):
    '''
    :param BQM: BQM model
    :return: simplified model
    '''
    sampler = ExactSolver()
    return sampler.sample(BQM)


def max_of_N_numbers(dict_of_x_i, sampled_max, N):
    '''
    o(n) - we take the subset with the minimum of energy

    :param dict_of_x_i: encryption of BQM
    :param sampled_max: sample of BQM model
    :param N: number of given numbers

    :return: subset - answer for the problem
    '''
    ans = [] # here will be the answer
    min_set = sampled_max.slice(0, 1) #minimum of energy
    for i in range(N):
        if min_set.first.sample['x{}'.format(i+1)] == 1: #if we took x_i from model
            ans.append((-1)*dict_of_x_i['x{}'.format(i+1)])   # write in answer. In dict each x was put with an opposite sign

    # return subset
    return ans


def apply_func(in_array):
    '''
    :param in_array: input array
    :return: subarray answer
    '''
    for i in range(len(in_array)):
        Max_of_N_dict['x{}'.format(i+1)] = (-1)*in_array[i] #we need maximum, but this way we'll check the minimum of energy
    Max_of_N_BQM = dimod.BinaryQuadraticModel(Max_of_N_dict, #our binary model
                  {},
                  1, 'BINARY')

    #samplifying model
    sampled_model = sample_BQM(Max_of_N_BQM)
    print(sampled_model)
    return max_of_N_numbers(Max_of_N_dict, sampled_model, len(in_array))


def hand_test():
    while 1:
        try:
            in_array = list(map(int, input("Please, input an array to find a maximum subset (type 'exit' to exit): ").split()))  # input
        except:
            break
        # filling dictionary 'x_i' =  - in_array[i], where x_i in BQM will be 0 or 1,
        # so we'll take or not to take in_array[i] in our subarray
        for i in range(len(in_array)):
            Max_of_N_dict['x{}'.format(i + 1)] = (-1) * in_array[
                i]  # we need maximum, but this way we'll check the minimum of energy
        Max_of_N_BQM = dimod.BinaryQuadraticModel(Max_of_N_dict,  # our binary model
                                                  {},
                                                  1, 'BINARY')

        # samplifying model
        sampled_model = sample_BQM(Max_of_N_BQM)
        print(sampled_model)
        # answer
        print(*max_of_N_numbers(Max_of_N_dict, sampled_model, len(in_array)))

if __name__ == '__main__':
    if 'h' == input("auto or hand test? (a/h): "):
        hand_test()
    else:
        auto_test()

import dimod
from dimod.reference.samplers import ExactSolver

#
#constant BQM model:
CNOT_BQM = dimod.BinaryQuadraticModel({'x1': 1.0, 'x2': 1.0, 'x3': 1.0, 'y': -2.0},
                  {('x1', 'x2'): -1.0, ('x1', 'x3'): -1.0, ('x2', 'x3'): -1.0},
                  0, 'BINARY')


def inp(message):
    '''
    :param message: message to user
    :return: input variables
    '''
    l = list(map(int, input(message).split()))
    try:
        return l[0], l[1]
    except:
        print("Error: wrong input")


def sample_BQM(BQM):
    '''
    :param BQM: BQM model
    :return: simplified model
    '''
    sampler = ExactSolver()
    return sampler.sample(BQM)


def cnot_gate(input_x1, input_x2, sampled_cnot):
    '''
    O(n) - we pass through rows in simplified model and checking for matches with our two vars.
    When found a match - we analyse what the answer should be.

    :param input_x1: first variable in gate
    :param input_x2: second variable in gate
    :param sampled_not: simplified model
    :return: answer: input_x1 CNOT input_x2 == 1 or 0
    '''
    sliced_set = sampled_cnot.slice(0, 1) #first row

    # x1,2 from model
    comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']

    i = 1 #num of current row
    while comparing_x1 != input_x1 or comparing_x2 != input_x2: #work untill it is a match
        try:
            sliced_set = sampled_cnot.slice(i, i+1)
            comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']
        except (IOError, Exception) as err:
            print("I can't apply CNOT gate to the x and y")
            break
        i += 1

    #if it's a match and y from model is 1 then x3
    if sliced_set.first.sample['y'] == 1:
        return sliced_set.first.sample['x3']


if __name__ == '__main__':
    sampled_model = sample_BQM(CNOT_BQM) #sampling model
    print(sampled_model)
    #input
    in_x, in_y = inp("Please, input an x and y (with a gap between, x - control) to apply CNOT gate: ")
    #answer
    print(cnot_gate(in_x, in_y, sampled_model))

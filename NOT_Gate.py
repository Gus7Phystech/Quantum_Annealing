import dimod
from dimod.reference.samplers import ExactSolver

#
#constant  model:
NOT_BQM = dimod.BinaryQuadraticModel({'x1': -1.0, 'x2': -1.0},
                  {('x2', 'x1'): 2.0},
                  1, 'BINARY')


def sample_BQM(BQM):
    '''
    :param BQM: BQM model
    :return: simplified model
    '''
    sampler = ExactSolver()
    return sampler.sample(BQM)


def not_gate(input_x, sampled_not):
    '''
    o(n) - we compare given variable to the first from model. When match we stop and give the answer
    Answer is the second variable from the model

    :param input_x: given variable
    :param sampled_not: BQM model
    :return: NOT input_x
    '''
    sliced_set = sampled_not.slice(0, 1) #first row
    comparing_x = sliced_set.first.sample['x1'] #x1 from model
    i = 1 #num of current row
    while comparing_x != input_x: #work untill it is a match
        try:
            sliced_set = sampled_not.slice(i, i+1)
            comparing_x = sliced_set.first.sample['x1']
        except (IOError, Exception) as err:
            print("I can't apply NOT gate to the x")
            break
        i += 1
    
    # return second variable
    return sliced_set.first.sample['x2']


if __name__ == '__main__':
    sampled_model = sample_BQM(NOT_BQM) #sampling model
    #input
    in_x = int(input("Please, input an x to apply NOT gate: "))
    #answer
    print(not_gate(in_x, sampled_model))
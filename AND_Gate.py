import dimod
from dimod.reference.samplers import ExactSolver

#
#constant BQM model:
AND_BQM = dimod.BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
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


def and_gate(input_x1, input_x2, sampled_not):
    '''
    O(n) - we pass through rows in simplified model and checking for matches with our two vars.
    When found a match - we analyse the what the answer should be.

    :param input_x1: first variable in gate
    :param input_x2: second variable in gate
    :param sampled_not: simplified model
    :return: answer: input_x1 AND input_x2 == True or False
    '''
    sliced_set = sampled_not.slice(0, 1) #first row

    # x1,2 from model
    comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']

    i = 1 #num of current row
    while comparing_x1 != input_x1 or comparing_x2 != input_x2: #work untill it is a match
        try:
            sliced_set = sampled_not.slice(i, i+1)
            comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']
        except (IOError, Exception) as err:
            print("I can't apply AND gate to the x and y")
            break
        i += 1

    #if energy is minimal and y1 from model is 1 then True
    if sliced_set.first.sample['y1'] == 1 and \
        sliced_set.data_vectors['energy'][0] == sampled_not.lowest().data_vectors['energy'][0]:
        return True
    else:
        return False


if __name__ == '__main__':
    sampled_model = sample_BQM(AND_BQM) #sampling model
    #input
    in_x, in_y = inp("Please, input an x and y (with a gap between) to apply AND gate: ")
    #answer
    print(and_gate(in_x, in_y, sampled_model))
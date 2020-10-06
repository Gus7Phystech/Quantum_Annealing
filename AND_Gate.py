import dimod
from dimod.reference.samplers import ExactSolver

#
#constant  model:
AND_BQM = dimod.BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
                  0, 'BINARY')

def inp(message):
    l = list(map(int, input(message).split()))
    try:
        return l[0], l[1]
    except:
        print("Error: wrong input")


def sample_BQM(BQM):
    sampler = ExactSolver()
    return sampler.sample(BQM)


def and_gate(input_x1, input_x2, sampled_not):
    sliced_set = sampled_not.slice(0, 1)
    comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']
    i = 1
    #while min(comparing_x1, comparing_x2) != min(input_x1, input_x2) or \
    #        max(comparing_x1, comparing_x2) != max(input_x1, input_x2):
    while comparing_x1 != input_x1 or comparing_x2 != input_x2:
        try:
            sliced_set = sampled_not.slice(i, i+1)
            comparing_x1, comparing_x2 = sliced_set.first.sample['x1'], sliced_set.first.sample['x2']
        except (IOError, Exception) as err:
            print("I can't apply AND gate to the x and y")
            break
        i += 1
    if sliced_set.first.sample['y1'] == 1 and \
        sliced_set.data_vectors['energy'][0] == sampled_not.lowest().data_vectors['energy'][0]:
        return True
    else:
        return False


if __name__ == '__main__':
    sampled_model = sample_BQM(AND_BQM) #sampling model
    #print(sampled_model)
    in_x, in_y = inp("Please, input an x and y (with a gap between) to apply AND gate: ")
    print(and_gate(in_x, in_y, sampled_model))
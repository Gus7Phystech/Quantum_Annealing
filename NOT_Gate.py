import dimod
from dimod.reference.samplers import ExactSolver

#
#constant  model:
NOT_BQM = dimod.BinaryQuadraticModel({'x1': -1.0, 'x2': -1.0},
                  {('x2', 'x1'): 2.0},
                  1, 'BINARY')


def sample_BQM(BQM):
    sampler = ExactSolver()
    return sampler.sample(BQM)


def not_gate(input_x, sampled_not):
    sliced_set = sampled_not.slice(0, 1)
    comparing_x = sliced_set.first.sample['x1']
    i = 1
    while comparing_x != input_x:
        try:
            sliced_set = sampled_not.slice(i, i+1)
            comparing_x = sliced_set.first.sample['x1']
        except (IOError, Exception) as err:
            print("I can't apply NOT gate to the x")
            break
        i += 1
    return sliced_set.first.sample['x2']


if __name__ == '__main__':
    sampled_model = sample_BQM(NOT_BQM) #sampling model
    #print(sampled_model)
    in_x = int(input("Please, input an x to apply NOT gate: "))
    print(not_gate(in_x, sampled_model))
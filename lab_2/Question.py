import copy
import numpy

def get_sub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

class Question:
    def __init__(self, find_max: bool, main_func: list, constrains: list):
        if find_max:
            self.main_func = main_func
        else:
            self.main_func = [-i for i in main_func]
        self.constrains = constrains

    def print_question(self):
        line = ""
        for i in range(len(self.main_func)):
            if self.main_func[i] > 0:
                line += "+ " + str(self.main_func[i])+"*X"+get_sub(str(i+1))+" "
            elif self.main_func[i] < 0:
                line += "- "+str(abs(self.main_func[i]))+"*X"+get_sub(str(i+1))+" "
        line += "--> max"
        print(line[1:])
        for constraint in self.constrains:
            line = ""
            for i in range(len(constraint)-2):
                if constraint[i] > 0:
                    line += "+ " + str(constraint[i]) + "*X" + get_sub(str(i + 1)) + " "
                elif constraint[i] < 0:
                    line += "- " + str(abs(constraint[i])) + "*X" + get_sub(str(i + 1)) + " "
            print(line[1:] + str(constraint[-2])+" "+str(constraint[-1]))

    def solve(self):
        full_list = [[0]+[-i for i in self.main_func]+[0]*(len(self.constrains)+2)]

        for i in range(len(self.constrains)):
            constraint = [0]+self.constrains[i][:-2] + [0]*(len(self.constrains)+2) + [self.constrains[i][-1]]
            constraint[i+len(self.main_func)+1] = 1
            if self.constrains[-2] == "<=":
                constraint[-2] = 1
            else:
                constraint[-2] = -1
            full_list += [constraint]
        print(full_list)

        full_list = numpy.array(full_list)
        while full_list[0, 1:full_list.shape[1]-2].min() < 0:
            pivot_column = full_list[:, full_list[:, ].argmin()]
            for i in range(len(self.constrains)):
                full_list[i+1][-1] = full_list[i+1][-2] / pivot_column[i+1]
            ratios = full_list[1:][-1]



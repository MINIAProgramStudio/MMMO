import copy


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
            for i in range(len(constraint)-1):
                if constraint[i] > 0:
                    line += "+ " + str(constraint[i]) + "*X" + get_sub(str(i + 1)) + " "
                elif constraint[i] < 0:
                    line += "- " + str(abs(constraint[i])) + "*X" + get_sub(str(i + 1)) + " "
            print(line[1:] + "= "+str(constraint[-1]))

    def solve(self):
        x_1 = [i[0] for i in self.constrains]
        counter = 0
        while not x_1[counter]:
            counter += 1
        new_constrains = []
        for constraint in self.constrains[:counter]:
            deviation = constraint[0]/self.constrains[counter][0]
            for i in range(len(constraint)):
                constraint[i] -= deviation*self.constrains[counter]
            new_constrains.append(constraint)
        new_constrains.append(self.constrains[counter])
        for constraint in self.constrains[counter+1:]:
            deviation = constraint[0]/self.constrains[counter][0]
            for i in range(len(constraint)):
                constraint[i] -= deviation*self.constrains[counter][i]
            new_constrains.append(constraint)
        self.constrains = new_constrains

        def x_1(args):
            x = new_constrains[counter][1:]
            for i in range(new_constrains[counter][1:]):
                i+=1
                x -= new_constrains[counter][i]*args[i]

        
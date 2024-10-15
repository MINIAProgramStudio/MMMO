import copy


def get_sub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

class Question:
    def __init__(self, find_max: bool, main_func: list, constrains: list, constrains_op: list):
        if not find_max:
            self.main_func = main_func
        else:
            self.main_func = [-i for i in main_func]
        self.constrains = constrains
        self.original_length = len(main_func)

    def print_question(self):
        line = ""
        for i in range(len(self.main_func)):
            if self.main_func[i] > 0:
                line += "+ " + str(self.main_func[i])+"*X"+get_sub(str(i+1))+" "
            elif self.main_func[i] < 0:
                line += "- "+str(abs(self.main_func[i]))+"*X"+get_sub(str(i+1))+" "
        line += "--> min"
        print(line[1:])
        for constraint in self.constrains:
            line = ""
            for i in range(len(constraint)-2):
                if constraint[i] > 0:
                    line += "+ " + str(constraint[i]) + "*X" + get_sub(str(i + 1)) + " "
                elif constraint[i] < 0:
                    line += "- " + str(abs(constraint[i])) + "*X" + get_sub(str(i + 1)) + " "
            print(line[1:] + str(constraint[-2])+" "+str(constraint[-1]))

    def prepare(self):
        # Вільний доданок має бути невід'ємним
        for i in range(len(self.constrains)):
            if self.constrains[i][-1]<0:
                self.constrains[i] = [-a for a in self.constrains[i]]

        # Зведення нерівностей з <=
        for i in range(len(self.constrains)):
            if self.constrains[i][-2] == "<=":
                self.main_func.append(0)
                for j in range(len(self.constrains)):
                    self.constrains[j].insert(-2, 0)
                self.constrains[-3] = 1
                self.constrains[i][-2] = "="
                self.marked[i] = True

        # Зведення нерівностей з >=
        for i in range(len(self.constrains)):
            if self.constrains[i][-2] == "<=":
                self.main_func.append(0)
                for j in range(len(self.constrains)):
                    self.constrains[j].insert(-2, 0)
                self.constrains[-3] = -1
                self.constrains[i][-2] = "="
                self.marked[i] = True

        #




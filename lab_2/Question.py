import copy
import scipy

def get_sub(x):
    normal = "0123456789+-=()"
    sub_s = "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

class Question:
    def __init__(self, find_max: bool, main_func: list, constrains: list):
        if not find_max:
            self.main_func = main_func
        else:
            self.main_func = [-i for i in main_func]
        for i in range(len(constrains)):
            if constrains[i][-2] == ">=":
                constrains[i][:-2] = [-j for j in constrains[i][:-2]]
                constrains[i][-1] = -constrains[i][-1]
                constrains[i][-2] = "<="
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

    def solve(self):
        eq_a = []
        eq_b = []
        ub_a = []
        ub_b = []
        for c in self.constrains:
            if c[-2] == "=":
                eq_a.append(c[:-2])
                eq_b.append(c[-1])
            else:
                ub_a.append(c[:-2])
                ub_b.append(c[-1])
        if ub_a and eq_a:
            result = scipy.optimize.linprog(self.main_func,ub_a,ub_b,eq_a,eq_b,method = "simplex")
        elif ub_a:
            result = scipy.optimize.linprog(self.main_func, ub_a, ub_b, method="simplex")
        elif eq_a:
            result = scipy.optimize.linprog(self.main_func, A_eq = eq_a, b_eq = eq_b, method="simplex")
        return result

    def print_solution(self):
        xs = self.solve()["x"]
        for x in range(len(xs)):
            print("X"+get_sub(str(x+1)) + " = "+ str(xs[x]))
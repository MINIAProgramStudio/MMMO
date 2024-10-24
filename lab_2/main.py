from Question import Question



var_3 = Question(True,
                 [2, 3, 0, -1, 0, 0],
                 [[2, -1, 0, -2, 1, 0, "=", 16,],
                  [3, 2, 1, -3, 0, 0, "=", 18],
                  [-1, 3, 0, 4, 0, 1, "=", 24]])

var_3.print_question()
print()
var_3.solve()
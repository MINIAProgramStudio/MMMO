import pandas
import math

def cor_val(x,y, depth = None):
    if depth is None:
        depth = len(x)
    x = x[:depth]
    y = y[:depth]
    sum_both = 0
    sum_x = 0
    sum_y = 0
    x_mean = 0
    try:
        x_mean = x.mean()
    except:
        for x_i in x:
            x_mean+=x_i
        x_mean = x_mean/len(x)
    y_mean = 0
    try:
        y_mean = x.mean()
    except:
        for y_i in y:
            y_mean += y_i
        y_mean = y_mean / len(x)

    for i in range(len(x)):
        x_part = x[i]-x_mean
        y_part = y[i]-y_mean
        sum_both += x_part*y_part
        sum_x += x_part**2
        sum_y += y_part**2
    sum_x = math.sqrt(sum_x)
    sum_y = math.sqrt(sum_y)
    result = sum_both/(sum_x*sum_y)
    if math.isnan(result):
        result = 0
    return result

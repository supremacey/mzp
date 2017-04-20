"""
    Collection of Euler methods and their improvements
"""
def euler(val_x, val_y, step, fun):
    """
        Euler's, Euler-Cauchy or the point-slope method.
    """
    return val_y + step * fun(val_x, val_y)

def heun(val_x, val_y, step, fun):
    """
        Heun's method
        or predictor-corector method
        or explicit trapezoid method
    """
    K1 = fun(val_x, val_y)  # slope at the beginning of the interval 
    y_end = val_y + step * K1
    K2 = fun(val_x+step, y_end)  # slope at the end of interval
    return val_y + step * (K1 + K2)/2 

def midpnt(val_x, val_y, step, fun):
    """
        Midpoint Euler's method
    """
    y1_2 = euler(val_x, val_y, step/2, fun)
    return val_y + step * fun(val_x+step/2, y1_2)


def back(val_x, val_y, step, fun):
    """
        Backward Euler's method
    """
    pred = euler(val_x, val_y, step, fun)
    return val_y + step * fun(val_x+step, pred)

def rk4(val_x, val_y, step, fun):
    K1 = fun(val_x,           val_y)
    K2 = fun(val_x + step/2,  val_y + step/2 * K1/2)
    K3 = fun(val_x + step/2,  val_y + step/2 * K2/2)
    K4 = fun(val_x + step,    val_y + step * K3)
    return val_y + step * 1/6 * (K1 + 2*(K2 + K3) + K4)

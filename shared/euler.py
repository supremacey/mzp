"""
    Collection of Euler methods and their improvements
"""
def euler(h, val_x, val_y, fun):
    """
        Euler's, Euler-Cauchy or the point-slope method.
    """
    return val_y + h * fun(val_x, val_y)

def heun(h, val_x, val_y, fun)):
    """
        Heun's method
        or predictor-corector method
        or explicit trapezoid method
    """
    y0 = euler(h, val_x, val_y, fun)
    y1 = euler(h, val_x+h, y0, fun)
    return val_y + h * (y0+y1)/2 

def midpnt(h, val_x, val_y, fun)):
    """
        Midpoint Euler's method
    """
    y1_2 = euler(h/2, val_x, val_y, dun)
    return val_y + h * fun(val_x+h/2, y1_2)


def back(h, val_x, val_y, fun)):
    """
        Backward Euler's method
    """
    pred = euler(h, val_x, val_y, fun)
    return val_y + h * fun(val_x+h, pred)


import numpy as np 
import matplotlib.pyplot as plt

def linReg(x,y):
    """
    Calculate the parameters of a simple linear regression model.

    Parameters:
    x (array-like): Independent variable values.
    y (array-like): Dependent variable values.

    Returns:
    alpha (float): Intercept of the regression line.
    beta (float): Slope of the regression line.
    r (float): Correlation coefficient.

    Formula:
    beta = (n * Sxy - Sx * Sy) / (n * Sxx - Sx^2)
    alpha = (Sy - beta * Sx) / n
    r = (n * Sxy - Sx * Sy) / sqrt((n * Sxx - Sx^2) * (n * Syy - Sy^2))
    
    where:
    n = number of data points
    Sx = sum of x
    Sxx = sum of x^2
    Sxy = sum of x*y
    Sy = sum of y
    Syy = sum of y^2

    Note:
    This function assumes that the input data x and y have the same length.

    Example:
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 4, 5, 6]
    alpha, beta, r = linReg(x, y)
    """

    n=float(len(x))
    x=np.array(x)
    y=np.array(y)
    Sx=np.sum(x)
    Sxx=np.sum(x*x)
    Sxy=np.sum(x*y)
    Sy=np.sum(y)
    Syy=np.sum(y*y)

    beta=(n*Sxy - Sx*Sy)/(n*Sxx-Sx*Sx)
    alpha = (Sy-beta*Sx)/n

    r=(n*Sxy-Sx*Sy)/np.sqrt( (n*Sxx-Sx*Sx) * (n*Syy-Sy*Sy) )
    return alpha, beta , r

x=np.arange(0,5,0.1)
y= 3.0 - 2.* x + np.random.normal(0,1,len(x))
alpha, beta, r = linReg(x,y)

yp=beta*x+alpha


for i in range(len(x)):
    plt.plot([x[i],x[i]],[y[i],yp[i]],'r')
plt.plot(x,y,'sk')
plt.plot(x,yp,'b')
plt.title(f"y={beta:.2f}*x+{alpha:.2f},    corr-coef={r:.2f}")
plt.show()

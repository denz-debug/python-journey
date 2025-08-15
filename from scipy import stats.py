import matplotlib.pyplot as plt
from scipy import stats

x = [38,37.6,36,37.2,37] 
y = [5,3,8,2,1]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
     return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
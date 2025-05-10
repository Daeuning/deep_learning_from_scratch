import numpy as np
import matplotlib.pylab as plt

def step_function_v1(x):
  if x > 0:
    return 1
  else:
    return 0
  
def step_function_v2(x):
  y = x > 0
  return y.astype(int)

def step_function_v3(x):
  return np.array(x > 0, dtype = int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function_v3(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


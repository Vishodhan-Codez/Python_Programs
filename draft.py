import numpy as np
import matplotlib.pyplot as plt
heights = np.linspace(140, 200, 100)
a = 0.5  
b = 10   
noise = np.random.normal(0, 5, size=heights.shape) 
weights = a * heights + b + noise
plt.scatter(heights, weights, label='Data with noise')
plt.plot(heights, a * heights + b, color='red', label='Ideal line (no noise)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.show()

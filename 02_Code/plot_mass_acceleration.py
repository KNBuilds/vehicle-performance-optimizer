import matplotlib.pyplot as plt
import numpy as np

force = 3000
masses = np.array([500, 750, 1000, 1250, 1500])

accelerations = force / masses

plt.plot(masses, accelerations, marker="o")

plt.xlabel("Vehicle Mass (kg)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Effect of Vehicle Mass on Acceleration")

plt.grid(True)
plt.show()

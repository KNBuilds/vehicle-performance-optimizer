import numpy as np

force = 3000
masses = np.array([500, 750, 1000, 1250, 1500])

accelerations = force / masses

print("Masses:", masses)
print("Accelerations:", accelerations)

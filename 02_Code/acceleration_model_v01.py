def calculate_acceleration(force, mass):
    return force / mass


force = 3000

vehicle_masses = [500, 750, 1000, 1250, 1500]

for mass in vehicle_masses:
    acceleration = calculate_acceleration(force, mass)
    print("Mass:", mass, "kg | Acceleration:", acceleration, "m/s²")
    

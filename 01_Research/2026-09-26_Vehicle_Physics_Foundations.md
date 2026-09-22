# Vehicle Physics Foundations

Date: September 21, 2026

## 1. Distance

Equation:
d = vt

Variables:
d = distance travelled
v = velocity/speed
t = time

Units: 
Distance: metres (m)
Speed: metres per second (m/s)
Time: seconds (s)

Engineering application:
Used to calculate how far a vehicle travels when its speed is constant over a given period of time. It can be used in basic vehicle performance calculations and is a foundation for more advanced motion modelling.
---

## 2. Power-to-Mass Ratio

Equation:
P/m

Variables:
P = power
m = vehicle mass

Units:
Power: watts (W)
Mass: kilograms (kg)
Power-to-mass ratio: watts per kilogram (W/kg)

Engineering application:
Used to compare the amount of power available relative to vehicle mass. A higher power-to-mass ratio generally indicates greater acceleration potential, although real vehicle performance is also affected by factors such as traction, gearing, aerodynamic drag and drivetrain losses.

---

## 3. Weight

Equation:
W = mg

Variables:
W = weight/gravitational force
m = mass
g = gravitational acceleration

Units:
Weight: newtons (N)
Mass: kilograms (kg)
Gravitational acceleration: metres per second squared (m/s²) For Earth:g≈9.81 m/s2

Engineering application:
Used to calculate the gravitational force acting on a vehicle. Vehicle weight affects tyre loading, normal force, braking, traction and other vehicle dynamics calculations.
---

## 4. Speed

Equation:
v = d/t

Variables:
v = speed
d = distance travelled
t = time

Units:
Speed: metres per second (m/s)
Distance: metres (m)
Time: seconds (s)

Engineering application:
Used to determine the average speed of a vehicle over a given distance and time. Speed is important for analysing acceleration, braking, aerodynamic drag, lap times and vehicle performance.

---

## 5. Acceleration

Equation:
a = (vf - vi)/t

Variables:
a = acceleration
vf = final velocity
vi = initial velocity
t = time taken for the velocity to change

Units:
Acceleration: metres per second squared (m/s²)
Velocity: metres per second (m/s)
Time: seconds (s)

Engineering application:
Used to determine how quickly a vehicle's velocity changes. Acceleration is important when analysing vehicle launch performance, straight-line performance and vehicle dynamics.

---

## Assumptions
- SI units are used.
- Vehicle mass is constant during each calculation.
- Basic distance calculations assume constant speed.
- Basic acceleration calculations assume constant acceleration.
- Gravitational acceleration is approximately 9.81 m/s².
- The initial vehicle model ignores aerodynamic drag.
- Rolling resistance is ignored.
- Tyre slip and traction limitations are ignored.
- Drivetrain losses are ignored.
- Road gradient is ignored.
- Wind effects are ignored.
- Power is initially treated as a simplified value rather than a complete engine/motor power curve.
---

## Limitations
The calculations are simplified models and do not represent the complete behaviour of a real vehicle.

The current model does not account for:

Aerodynamic drag
Downforce
Tyre grip
Traction limits
Rolling resistance
Drivetrain efficiency
Gear ratios
Engine/motor power curves
Road gradients
Wind
Suspension behaviour
Weight transfer
Changing vehicle conditions

Therefore, the current calculator is useful for learning fundamental vehicle physics but cannot yet accurately predict real-world vehicle performance.
---

## What I learned
- How basic physics equations can be converted into Python calculations.
- The difference between mass and weight.
- How power-to-mass ratio can be used to compare vehicles.
- How mass affects acceleration when driving force is constant.
- How speed, distance and time are related.
- How acceleration describes a change in velocity over time.
- That a simple vehicle model requires assumptions.
- That real vehicle performance depends on many interacting factors.
- That Python can be used to automate engineering calculations.
---

## What I need to learn next
- Newton's Second Law and vehicle driving force
- The relationship between power, force and speed
- More realistic acceleration modelling
- Tyre grip and traction
- Braking force and braking distance
- Rolling resistance
- Aerodynamic drag
- Downforce
- Cornering forces
- Vehicle dynamics
- NumPy for engineering calculations
- Matplotlib for data visualisation
- Using experimental/data-driven results to validate models
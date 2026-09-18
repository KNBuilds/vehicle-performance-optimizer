# Vehicle Performance & Setup Optimizer
## September 17, 2026

### Today's objective
Define the scope and engineering foundations of the project.

### What I worked on
- Defined the project purpose
- Identified vehicle parameters
- Identified performance outputs
- Reviewed basic vehicle physics
- Created the project development roadmap
- Tested basic vehicle parameters

### Physics concepts reviewed
- Distance
- Power-to-weight ratio
- Aerodynamic drag
- Downforce
- Friction
- Braking

### What I learned
- Aerodynamic drag
- Downforce
- Friction
- Braking
- Planning a project

### Problems/questions
1. What does each function calculate?
calculate_distance = distance = speed * time
calculate_power_to_weight_ratio = ratio = power / mass

2. What are the inputs?
 - speed
 - time
 - power
 - mass

3. What is the output?
 - distance
 - power to weight ratio

4. What units am I using?
 - speed = metres per second
 - time = seconds
 - power = Watts
 - mass = kilograms
 - distance = metres
 - power =  Watts per kilogram

5. What would happen if I changed the vehicle mass?
As the mass increases the power to weight ratio will decrease and vice versa

6. What would happen if I changed the power?
As the power increases the power to weight ratio will increase and vice versa

7. What additional vehicle physics calculations will I need?
 - Speed conversions
 - Time
 - Acceleration
 - Force
 - Engine/motor power
 - Vehicle mass
 - Traction
 - Braking force
 - Deceleration
 - Braking distance
 - Tyre-road friction
 - Initial speed
 - Corner radius
 - Lateral acceleration
 - Tyre grip
 - Cornering force
 - Maximum cornering speed
 - Air density
 - Drag coefficient
 - Frontal area
 - Velocity
 - Drag force
 - Downforce
 - Lift coefficient
 - Coefficient of friction
 - Normal force
 - Available grip
 - Traction limit
 - Acceleration limit
 - Braking limit
 - Cornering limit



### Engineering assumptions
 - The vehicle's mass remains constant during the calculation.
 - The available power is treated as a constant value 
 - The vehicle travels in a straight line for the basic distance calculation.
 - Air resistance, rolling resistance, tyre slip,, wind, and many variabls are initially ignored.
 - The vehicle starts from the conditions specified in the calculation, such as a given speed and time.
 - The equations are simplified models of vehicle behaviour, not a complete simulation of a real vehicle.
 - Units are consistent, such as metres, seconds, kilograms, and watts.

### What I need to research
Vehicle physics

### Next step
Build the first acceleration model.
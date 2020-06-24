#%% Let us create code for a simple physics simulation

# Let us start by defining some simulation parameters

# Physical constants
g = 9.81  # [m/s^2]
acceleration = -g

# Initial conditions
init_height = 10  # [m]
init_velocity = 2.5  # [m/s]

# Simulation parameters
simulation_time = 5  # [s]
time_step = 0.1  # [s]
num_time_steps = int(simulation_time/time_step)  # Unitless


#%% Let us display the variables in the terminal window

# Printing a single variable
print(acceleration)

# Printing mutlitple variables
print(g, acceleration)

# Printing numbers directly
print(10)

# Printing text
print('The acceleration is', acceleration)
print("The gravitational constant is", g)

# Advanced text formatting
print(f'The height + speed is {init_height + init_velocity}')
print(f'The acceleration is {acceleration:.0f}')


#%% A brief introduction to loops in Python

height = init_height
velocity = init_velocity
time = 0
print(height)
time = time + time_step
height = height + velocity*time_step
velocity = velocity + acceleration*time_step
print(height)
time += time_step    # x += a  <=> x = x + a   
height += velocity*time_step
velocity += acceleration*time_step
print(height)

# This quickly becomes tedious, let us instead use a loop

height = init_height
velocity = init_velocity
time = 0

for i in range(num_time_steps):
    time += time_step
    height += velocity*time_step
    velocity += acceleration*time_step
    
    print(height)
    print(velocity)
    
# Yay, the simulation is running!!!
# It's impossible to see what's going on though...

#%% Formatting our simulation output

height = init_height
velocity = init_velocity
time = 0

for i in range(num_time_steps):
    time += time_step
    height += velocity*time_step
    velocity += acceleration*time_step
    
    print(
        f'The height is {height:.2f} meters and '
        f'the velocity is {velocity:.2f} meters per second '
        f'after {time:.2f} seconds'
    )


# Some more formatting

height = init_height
velocity = init_velocity
time = 0

for i in range(num_time_steps):
    time += time_step
    height += velocity*time_step
    velocity += acceleration*time_step
    
    print(
        f'The height is {height:6.2f} meters and '
        f'the velocity is {velocity:6.2f} meters per second '
        f'after {time:6.2f} seconds'
    )

# Notice how every digit spans (at least) 6 characters, prepended
# by zeros. This comes from the 6 in {height:6.2f}.
    

#%% A slight look at the range function

for i in range(10):
    print(i)


i = 0
print(i)
i = 1
print(i)
# ...
i = 10-1
print(i)


#%% Stopping the simulation


height = init_height
velocity = init_velocity
time = 0

for i in range(num_time_steps):
    time += time_step
    height += velocity*time_step
    velocity += acceleration*time_step
    
    if height <= 0:  # If you want to check equality, use if height == 0
        break
        # continue
    
    print(
        f'The height is {height:6.2f} meters and '
        f'the velocity is {velocity:6.2f} meters per second '
        f'after {time:6.2f} seconds'
    )


#%% Saving the simulation results

list_of_numbers = [1, 2, 3]
print(list_of_numbers)

# To get the first element of a list, write
print(list_of_numbers[0])

x = list_of_numbers[1]
print(x)

# To get the length of a list, use the len function
print('The length of the list is', len(list_of_numbers))

#%% We cannot do this:
print(list_of_numbers[len(list_of_numbers)])

#%% So how to access the last element?
# Like so?
print(list_of_numbers[len(list_of_numbers) - 1])
# This is better:
print(list_of_numbers[-1])

# Negative indices start at the end and count backwards
print(list_of_numbers[-2])

# There is something called slicing, to select multiple elements'

#%% Extending lists
print(list_of_numbers)
list_of_numbers.append(4)
print(list_of_numbers)

#%% Exercise

squares = [] # <- [0, 1, 4, 9, 16]

for i in range(5):
    squares.append(i**2)
    

#%% Using lists in our simulation

height = init_height
velocity = init_velocity
time = 0

heights = []
velocities = []
time_points = []

for i in range(num_time_steps):
    time += time_step
    height += velocity*time_step
    velocity += acceleration*time_step
    
    if height <= 0:  # If you want to check equality, use if height == 0
        break
        # continue

    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

print(heights)
print(f'The simulation ended after {time_points[-1]:.1f} seconds.')

#%% How does a for-loop work?

for i in range(10):
    print(i)

# What is this range(10)?
print(range(10))

# Let's convert it to a list
print(list(range(10)))

# So what is a for loop then?
list_range = list(range(10))
i = list_range[0]
print(i)
i = list_range[1]
print(i)
i = list_range[2]
print(i)
# ..
i = list_range[-1]
print(i)

for i in list_range:
    print(i)


# So, can we use this to look at out simulation results?

for height in heights:
    print(f'The height is {height:.2f}')

#%% Zip magic
    
# Iterating over two lists simultaneously
for height, time in zip(heights, time_points):
    print(f'The height after {time:.1f} seconds is {height:.2f}')

# Iterating over three lists simultaneously
for height, velocity, time in zip(heights, velocities, time_points):
    print(f'The height and velocity after {time:.1f} seconds '
          f'is {height:.2f} meters and {velocity:.2f} meters per second, '
          f'respectively.')


for idx in range(len(heights)):
    height = heights[idx]
    velocity = velocities[idx]
    time = time_points[idx]
    print('...')

#%% Enumerate magic

for idx, height in enumerate(heights):
    print(f'The {idx}-th height is {height:.2f}')
    
for idx, _ in enumerate(heights):
    print(idx)


#%% Improving readability and reusability with functions

heights = []
velocities = []
time_points = []

height = init_height
velocity = init_velocity
time = 0

def euler_step(x, dxdt, dt):
    return x + dt*dxdt

def evolve_equations_of_motion(height, velocity, time):
    height = euler_step(height, velocity, time_step)
    velocity = euler_step(velocity, acceleration, time_step)
    time += time_step
    
    return height, velocity, time

for _ in range(num_time_steps):  # We use underscore instead of i here because we're not interested in this variable
    height, velocity, time = evolve_equations_of_motion(
        height, velocity, time
    )
    
    if height < 0:
        break
    
    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

#%% Creating one large function for everything


def euler_step(x, dxdt, dt):
    return x + dt*dxdt

def evolve_equations_of_motion(height, velocity, acceleration, time):
    height = euler_step(height, velocity, time_step)
    velocity = euler_step(velocity, acceleration, time_step)
    time += time_step
    
    return height, velocity, time

def compute_num_timepoints(simulation_length, time_step):
    return int(simulation_length/time_step)

def simulate_ball_throw(
    init_height,
    init_velocity,
    acceleration,
    simulation_length,
    time_step
):
    num_time_points = compute_num_timepoints(
        simulation_length, time_step
    )

    height = init_height
    velocity = init_velocity
    time = 0

    heights = []
    velocities = []
    time_points = []
    for _ in range(num_time_steps):  # We use underscore instead of i here because we're not interested in this variable
        height, velocity, time = evolve_equations_of_motion(
            height, velocity, acceleration, time
        )
        
        if height < 0:
            break
        
        heights.append(height)
        velocities.append(velocity)
        time_points.append(time)
    
    return heights, velocities, time_points

print(
    simulate_ball_throw(
            init_height,
            init_velocity,
            acceleration,
            simulation_time,
            time_step
        )
)


#%% How to have default arguments for functions
    


def euler_step(x, dxdt, dt):
    return x + dt*dxdt

def evolve_equations_of_motion(height, velocity, acceleration, time):
    height = euler_step(height, velocity, time_step)
    velocity = euler_step(velocity, acceleration, time_step)
    time += time_step
    
    return height, velocity, time

def compute_num_timepoints(simulation_length, time_step):
    return int(simulation_length/time_step)

def simulate_ball_throw(
    init_height,
    init_velocity,
    acceleration=-9.81,  # <- -9.81 is default for acceleration
    simulation_length=10,  # <- 10 is default for simulation_length
    time_step=0.1  # <- 0.1 is default for time_step
):
    num_time_points = compute_num_timepoints(
        simulation_length, time_step
    )

    height = init_height
    velocity = init_velocity
    time = 0

    heights = []
    velocities = []
    time_points = []
    for _ in range(num_time_steps):  # We use underscore instead of i here because we're not interested in this variable
        height, velocity, time = evolve_equations_of_motion(
            height, velocity, acceleration, time
        )
        
        if height < 0:
            break
        
        heights.append(height)
        velocities.append(velocity)
        time_points.append(time)
        
    
    return heights, velocities, time_points



height, velocity, time_points = simulate_ball_throw(
    init_height,
    init_velocity,
)

print(height)


#%% Another function with defaults

def add(x, y=2):
    return x + y

print(add(1, 3))
print(add(1))

#%% Specifying inputs in custom order

height, velocity, time_points = simulate_ball_throw(
    init_height=5,
    init_velocity=3,
    simulation_length=20
)

print(height)


#%% Another function with keyword-arguments

def add_and_multiply(a, b=2, c=1):
    return (a + b)*c

print(add_and_multiply(2, 2, 3))
print(add_and_multiply(2, 2))
print(add_and_multiply(2, c=3))

#%%
import matplotlib.pyplot as plt
import numpy as np

heights, velocities, time_points = simulate_ball_throw(
    init_height,
    init_velocity
)

time_points = np.array(time_points)

exact_heights = (
    init_height + 
    init_velocity*time_points + 
    0.5*acceleration*time_points**2
)

plt.plot(time_points, heights, label='Numerically computed')
plt.plot(time_points, exact_heights, label='Exact solution')
plt.legend()
plt.show()
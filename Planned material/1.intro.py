#%% Let us create code for a very simple physics simulation
# Let us simulate the trajectory of a ball that approaches the earth
# To do this, we start by defining some parameters
# This is done in a similar fashion as in other languages, such as
# MATLAB and R. If you've programmed in C/C++/Java, you might notice
# that Python does not require us to specify the variable type.

# Constants
g = 9.81  # [m/s^2]

# Initial conditions
h0 = 10    # [m]
v0 = 2.5  # [m/s]
a = -g    # [m/s^2]

# Simulation parameters
simulation_time = 5  # [s]
dt = 0.1  # [s]
num_timesteps = int(simulation_time/dt)  # Unitless

# In this last line, we convert a floating point number (double in
# MATLAB) to an integer. This means that we change how the computer
# represents the number internally, and is important for certain
# operations.

#%% Let us then show the variables in the terminal window
# To show variables in the terminal window, we use the ``print`` command,
# which lets us display strings in the terminal window.

print('a:', a)
print('v0:', v0)
print('h0:', h0)

# Here we see that a string is a sequence of text surrounded by
# quotation marks. These quotation marks can either be double
# quotation marks (e.g. "a: "), or single quotation marks
# (e.g. 'a: '). The one you choose depends on your own preference.
# However, you should be consistent with your use. Either use
# single or double, don't change between.
#%% We can format the strings better using so-called f-strings

print(f'a:  {a:5.2f}')
print(f'v0: {v0:5.2f}')
print(f'h0:  {h0:5.2f}')

# What we just used is an f-string, or format-string, which is
# a relatively new addition to the Python language. It lets
# us weave code and text together in one elegant expression.
# f-strings are created similarly to strings, but the first
# quotation mark (either single or double) should have an f
# preceding it, as seen above. Moreover, with an f-string, we
# can easily format the output. The syntax is the following:
# A left curly brace indicate that the subseeding expression
# should be evaluated. Python stops evaluating the moment it
# reaches either a colon or a right curly brace. Everything 
# subseeding the colon is formatting options. 5.2f means that 
# we want the experssion to be formated as a floating point
# number spanning five characters


#%% A brief introduction to loops in Python.

# Now that we have defined our simulation parameters, let us
# perform a quick experiment. Let us throw the ball upwards
# and track its y-coordinate using Euler's method. 

height = h0
velocity = v0
t = 0
print(height)
t = t + dt
height = height + dt*velocity
velocity = velocity + dt*a
print(height)
t += dt
height += dt*velocity
velocity += dt*a
print(height)


# This is quickly becoming tedious, let us instead use a loop

height = h0
velocity = v0
acceleration = a
for i in range(num_timesteps):
    velocity += acceleration*dt
    height += velocity*dt
    print(height)

#%% Stripping the loop down to its basics
# So what we just saw is a for loop, let us inspect what it does a
# bit further, let us strip it down to its basic form.
for i in range(10):
    print(i)
    
# We see that i starts at zero and increases by one until it reaches 10-1.
# This is one of the most common ways to use for-loops in Python
# and is a pattern we will se often. We will go deeper into its
# inner workings later, but first, let's look at the simulation again.

#%% Finding when the ball reaches the ground
# Let us see when the ball reaches the ground. That is, when is h=0?
# To do this, we need an if-test

height = h0
velocity = v0
acceleration = a
for i in range(num_timesteps):
    velocity += acceleration*dt
    height += velocity*dt
    if height < 0:
        break
    print(height)
    
# Here we use two useful parts of Python. If tests and the
# break keyword. The point of break is to stop the loop
# and by using it, we can often avoid using while-loops altogether.

#%% Saving the simulation results in lists

# It is not allways useful to simply print out the simulation
# results without storing them. Rather, we wish to store the
# results in a list, where each element contain one time-step.

# To do this, we use the list data structure provided by the
# Python language. Let us explore lists a bit first.

# We will start with two useful data structures, lists and tuples.
list_of_numbers = [1, 2, 3]

# We see that we can define lists using square brackets, separating
# the elements with commas. To extract a single element from a list,
# we use the []-operator
print(list_of_numbers[0])

# Note that Python is zero-indexed, so the first element in an iterable
# has index 0, the second has index 2 and so forth. The following code
# is, therefore, not valid

#print(list_of_numbers[3])

# To get the length of an iterable, we write the following
print(len(list_of_numbers))

# Note that we cannot get the last element of an iterable like so
#print(list_of_numbers[len(list_of_numbers)])
# since the last element in ``list_of_numbers`` has index 2.
# Therefore, we must access it the following way
print(list_of_numbers[len(list_of_numbers)-1])
# or, simply
print(list_of_numbers[-1])

# Here, we see that using negative indices when indexing an iterable in
# Python is equivalent to indexing "backwards". See the example below

n = 2
print(list_of_numbers[len(list_of_numbers)-n])
print(list_of_numbers[-n])

#%% Extending lists
# There is one final piece of the puzzle that we need before we can 
# perform a simple simulation of gravity. Namely how to extend
# lists. We can do this using the ``append`` method.
    
list_of_numbers = [1, 2, 3]
print(list_of_numbers)
list_of_numbers.append(4)
print(list_of_numbers)

# We see that the append function adds a new element to the list.
# Thus, to create a list with the integers x^2 for 0 <= x < 10,
# we simply write

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


#%% Storing the simulation results in a list

# Now, we want to store the results from our falling-ball simulation.
# Modify the code above so that the heights measured from the simulation
# is stored in a list.
heights = [h0]

# Solution:
height = h0
velocity = v0
acceleration = a
for i in range(num_timesteps):
    velocity += acceleration*dt
    height += velocity*dt
    if height < 0:
        break
    heights.append(height)

print(heights)


# We might also be interested in the different values for the
# velcity, height and timesimultaneously, create three lists
# ``heights``, ``velicities`` and ``time_points`` and store
# the respective values in these lists.

# Solution:

heights = [h0]
velocities = [v0]
time_points = [0]

height = h0
velocity = v0
acceleration = a
time = 0
for i in range(num_timesteps):
    time += dt
    velocity += acceleration*dt
    height += velocity*dt
    if height < 0:
        break
    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

print(heights)


#%% Going back to for-loops details

# Let us, for a moment, look back to for loops, and in particular
# how they are implemented. Till now, we have only seen the pattern
for i in range(5):
    print(f'Do somthing: {i}')

# However, this hides the "true nature" of the for-loops in Python,
# namely, that they are for-each loops. Let us illustrate this

for height in heights:
    print(height)

# Thus, we see that a for loop iterate through an ``iterable`` object.
# The for-loop above is, in fact, equal to writing:

height = heights[0]
print(height)
height = heights[1]
print(height)
#...
height = heights[-1]
print(height)

#%% The range-function
# Using this knowledge, we can unwrap what the range-function does.
# Calling range(5) creates a list-like object containing the numbers
# 0 to 4. To illustrate this, let us print it.
print(range(5))

# Oh, we cannot se the numbers. Let us convert it to a list before
# printing it

print(list(range(5)))

# Now, for some other uses of range, what do you think will be
# printed out when we write the following.

print(list(range(3, 8)))

# How about this?

print(list(range(3, 8, 2)))

# Or this

print(list(range(8, 3, -1)))


#%% Exersices
# Create a list with integers x^2 - 2x for < x < 15

# Create the list above, but in reverse order


#%% zip and enumerate
# There are two more patterns I want to show you, however, we do not
# have time to look thoroughly on these patterns.

#%% Iterating over multiple lists with zip
for time, height in zip(time_points, heights):
    print(f'The height is {height:5.2f} after {time:5.2f} seconds')

for time, height, velocity in zip(time_points, heights, velocities):
    print(f'The height is {height:5.2f} and the velocity is {velocity:5.2f} after {time:5.2f} seconds')

#%% Getting indices and values simultaneously
for i, time in enumerate(time_points):
    print(f'The {i}-th time-point is {time} seconds')

#%% Improving our simulation with functions.

# Let us now generalise the simulations by using functions. 
# By doing this, we get more readable code that is easier modify.
    
# To find the points we can modify, we can copy paste the code
# below.
    

#%% Using functions to prevent repeating code

heights = [h0]
velocities = [v0]
time_points = [0]

height = h0
velocity = v0
acceleration = a
time = 0
for i in range(num_timesteps):
    time += dt
    velocity += acceleration*dt  # <-- These two lines are the same
    height += velocity*dt        # <-|   So we can create a function
    if height < 0:
        break
    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

print(heights)


#%% Let us create the function 

def euler_step(x, dx, dt):
    return x + dx*dt


heights = [h0]
velocities = [v0]
time_points = [0]

height = h0
velocity = v0
acceleration = a
time = 0

for i in range(num_timesteps):
    time += dt
    velocity = euler_step(velocity, acceleration, dt)
    height = euler_step(height, velocity, dt)
    if height < 0:
        break

    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

print(heights)


#%% Using functions in place of comments

# The code above is slightly difficult to read, another useful
# way to use functions is instead of comments. By defining
# functions, we can easily understand what the code does, without
# worrying about implementation details.


def euler_step(x, dx, dt):
    return x + dx*dt

def evolve_equations_of_motion(height, velocity, time, acceleration, dt):
    time += dt
    velocity = euler_step(velocity, acceleration, dt)
    height = euler_step(height, velocity, dt)
    
    return height, velocity, time

# Here, we see a new concept: mutliple return values. 
# It is a very useful feature that is easy to use.

heights = [h0]
velocities = [v0]
time_points = [0]

height = h0
velocity = v0
acceleration = a
time = 0

for i in range(num_timesteps):
    time, velocity, height = evolve_equations_of_motion(
        height, velocity, time, acceleration, dt
    )
    
    if height < 0:
        break

    heights.append(height)
    velocities.append(velocity)
    time_points.append(time)

print(heights)

# Here we see two 
#%% We can also move the simulation loop inside a function

# Exercise: Create a function that takes the initial height,
# initial velocity, initial time, acceleration, and simulation length
# as input arguments and returns a list with heights, velocities and
# time points.

def simulate_ball_throw(
    initial_height,
    initial_velocity,
    initial_time,
    acceleration,
    simulation_time,
    timestep
):
    time = initial_time
    height = initial_height
    velocity = initial_velocity
    
    heights = [initial_height]
    velocities = [initial_velocity]
    time_points = [initial_time]  

    num_timesteps = int(simulation_time/timestep)
    for i in range(num_timesteps):
        height, velocity, time = evolve_equations_of_motion(
            height, velocity, time, acceleration, timestep
        )
        if height < 0:
            break
        heights.append(height)
        velocities.append(velocity)
        time_points.append(time)
    
    return heights, velocities, time_points


heights, velocities, time_points = simulate_ball_throw(
    initial_height=h0,
    initial_velocity=v0,
    initial_time=0,
    acceleration=acceleration,
    simulation_time=3,
    timestep=dt
)
print(heights)


#%% Teaser: Data visualisation and numerical programming
# 
import numpy as np
import matplotlib.pyplot as plt

time_points = np.array(time_points)
exact_heights = h0 + v0*time_points + 0.5*acceleration*time_points**2

plt.plot(time_points, heights, label='Numerical solution')
plt.plot(time_points, exact_heights, label='Exact solution')

plt.legend()
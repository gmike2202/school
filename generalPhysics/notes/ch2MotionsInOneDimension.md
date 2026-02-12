# Motion in One Dimension

<!--toc:start-->
- [Motion in One Dimension](#motion-in-one-dimension)
  - [Position, Velocity, and Speed of a Particle](#position-velocity-and-speed-of-a-particle)
  - [Instantaneous Velocity and Speed](#instantaneous-velocity-and-speed)
  - [Analysis Model: Particle Under Constant Velocity](#analysis-model-particle-under-constant-velocity)
  - [The Analysis Model Approach to Problem-Solving](#the-analysis-model-approach-to-problem-solving)
    - [Conceptualize](#conceptualize)
    - [Categorize](#categorize)
    - [Analyze](#analyze)
    - [Finalize](#finalize)
  - [Acceleration](#acceleration)
  - [Analysis Model: Particle Under Constant Acceleration](#analysis-model-particle-under-constant-acceleration)
  - [Freely Falling Objects](#freely-falling-objects)
  - [Kinematic Equations Derived from Calculus](#kinematic-equations-derived-from-calculus)
<!--toc:end-->

## Position, Velocity, and Speed of a Particle

- Displacement $\Delta x$ - of a particle is defined as its change in position in some time interval.
- Distance - is the length of a path followed by a particle.
- Vector quantity - Requires the specification of both direction and magnitude
- Scalar quantity - Has a numerical value and no direction.
- Displacement - $\Delta x \equiv x_f - x_i$
- Average velocity - defined as the particle's displacement $\Delta x$ divided by the time interval $\Delta t$ during which that displacement occurs: $V_{x,avg} \equiv \frac{\Delta x}{\Delta t}$
- Average speed - defined as the total distance d traveled divided by the total time interval required to travel that distance: $V_{avg} \equiv \frac{d}{\Delta t}$

Average Speed and Average Velocity:
  - The magnitude of the average velocity is *not* the average speed.

## Instantaneous Velocity and Speed
- Instantaneous velocity - equals the limiting value of the ratio $\frac{\Delta x}{\Delta t}$ as $\Delta t$ approaches zero: 
  - $v_x \equiv \lim_{\Delta t\to0} \frac{\Delta x}{\Delta t}$
  - In calculus notation:
    - $$v_x \lim_{\Delta t\to0}\frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$
- Instantaneous speed - defined as the magnitude of a particle's instantaneous velocity. It has no direction associated with it.

>[!Note]
  >In any graph of physical data, the slope represents the ratio of the change in the quantity represented on the vertical axis to the change in the quantity represented on the horizontal axis. Remember that a slope has units (unless both axes have the same units).
  
>[!Note]
  >The magnitude of the instantaneous velocity is the instantaneous speed. In an infinitesimal time interval, the magnitude of the displacement is equal to the distance traveled by the particle.

## Analysis Model: Particle Under Constant Velocity
- Analysis model is a common situation that occurs time and again when solving physics problems.
- The form an analysis model takes is a description of either:
  1. the behavior of some physical entity or 
  2. The interaction between that entity and the environment

Steps to solve a problem:
  1. Identify the analysis model that is appropriate for the problem.
  2. The model tells you which equation to use for the mathematical representation

- Particle under constant speed - $v = \frac{d}{\Delta t}$

## The Analysis Model Approach to Problem-Solving

### Conceptualize
- Think and understand the situation. Study any representations of the information  
- Almost always make a quick drawing of the situation. Indicate any known values
- Look for key phrases such as "starts from rest" ($v_i = 0$) or "stops" ($v_f=0$)
- What is the questions asking? Will the final result be numerical, algebraic, or verbal? Do you know what units to expect?
- What should a reasonable answer look like?

### Categorize
- Simplify the problem. Use a simplification model to remove details that are not important to the solution
- Categorize the problem in one of two ways: Is it a simple substitution problem? Or is it an analysis problem?
- If it is an analysis problem, the situation must be analyzed more deeply to generate an appropriate equation and reach a solution. Have you seen this type of problem before? If so, identify any analysis model(s) appropriate for the problem to prepare for the Analyze step

### Analyze
- Analyze and strive for a mathematical solution. 
- Use algebra (and calculus if necessary) to solve symbolically for the unknown variable in terms of what is given. Finally, substitute in the appropriate numbers, calculate the result, and round it to the proper number of significant figures

### Finalize
-  Examine your numerical answer. Does it have the correct units? Does it meet your expectations from your conceptualization of the problem? What about the algebraic form of the result? Does it make sense?
-  Think about the problem. How was it similar to others? How was it different? Why was it assigned? What have you learned by doing it?

## Acceleration
- The average acceleration of a particle is defined as the change in velocity $\Delta v_x$ divided by the time interval $\Delta t$ during which that change occurs:
  - $a_{x,avg} \equiv \frac{\Delta V_x}{\Delta t} = \frac{v_{xf} - v_{xi}}{t_f - t_i}$
- Instantaneous acceleration - The limit of the average acceleration as $\Delta t$ approaches zero.
  - $a_x \equiv \lim_{\Delta t\to0} \frac{\Delta v_x}{\Delta t} = \frac{dv_x}{dt}$
  - The instantaneous acceleration equals the derivative of the velocity with respect to time, which by definition is the slope of the velocity-time graph.
- The force on an object is proportional to the acceleration of the object:
  - $F_x \propto a_x$
>Negative Acceleration:  
 Keep in mind that negative acceleration does not necessarily mean that an object is slowing down. If the acceleration is negative and the velocity is negative, the object is speeding up! 

- Acceleration can be written as:
  - $a_x = \frac{dv_x}{dt} \frac{d}{dt} (\frac{dx}{dt}) \frac{d^2x}{dt^2}$

## Analysis Model: Particle Under Constant Acceleration
- Particle under constant acceleration - Analysis model in which the acceleration is constant. In such a case, the average acceleration $a_{x,avg}$ over any time interval is numerically equal:
  - $v_{xf} = v_{xi} + a_xt$ for constant $a_x$
- We can express the average velocity in any time interval as the arithmetic mean of the initial velocity $v_{xi}$ and the final velocity $v_{xf}$:
  - $v_{x,avg} = \frac{V_{xi} + v_{xf}}{2}$ for constant $a_x$
- How to obtain the position of an object as a function of time. Recall that $\Delta x$ represents $x_f - x_i$ and recognizing that $\Delta t = t_f - t_i = t - 0 = t$:
  - $x_f = x_i + \frac{1}{2}(v_xi + v_xf)t$ for constant $a_x$
  - Additional useful equation: $x_f = x_i + V_{xi}(t) + \frac{1}{2}a_xt^2$ for constant $a_x$

## Freely Falling Objects
- A freely falling object is an object that moves freely under the influence of gravity alone, regardless of its initial motion

>[!Note]
> A common misconception is that the acceleration of a projectile at the top of its trajectory is zero. Although the velocity at the top of the motion of an object thrown upward momentarily goes the zero, *the acceleration is still that due to gravity at this point.* If the velocity and acceleration were both zero, the projectile would stay at the top.

## Kinematic Equations Derived from Calculus
![image](/Users/muck/Documents/Syncthing/School/generalPhysics/53278_02_f15-t2.png)

- The total displacement for the interval $t_f-t_i$ is the sum of the areas of all the rectangles from $t_i$ to $t_f$:
  - $$\Delta x = \sum_{n} V_{xn,avg} \Delta t_n$$
- As the intervals are made smaller and smaller, the number of terms in the sum increases and the sum approaches a value equal to the are under the curve in the velocity-time graph.
  - $$\Delta x = \lim_{\Delta t_n\to0} \sum_n v_{xn,avg} \Delta t_n$$
- The limit of the sum = definite integral
  - $\Delta x = \int_{t_i}^{t_f} v_x(t)dt$

### Kinematic Equations
- $x_f - x_i = v_{xi}t + \frac{1}{2}a_x(t)^2$

> [!Note]
> If this discussion of integration is confusing, just remember that the integral of a function is simply the area between the function and the x axis between the limits of integration. If the function has a simple shape, the are can be easily calculated without integration. For example, if the function is a constant, so that its graph is a horizontal line, the area is just that of the rectangle between the line and the x axis!



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#------------------------------
# y_v - system of equations, here an x' and V'
def euler(iv, y_v, step, f):
    return y_v + step * f(iv, y_v) 

# initial condition
g = 9.8
L = 3  # resting length of string
ΔL = 1  # spring delta uder a mass
m = 0.5
k = g*m/ΔL 
b = 0.1
y0 = np.array([2.0, 0.0]) # initial position and velocity

y = y0.copy()
f = lambda iv, y_v : np.array([y_v[1], -k/m*y[0]-(L+ΔL) -b/m*y_v[1]])
#------------------------------
fig = plt.figure()
ax = plt.axes(xlim=[-5, 5], ylim=[-5,5])
ax.grid()
ax.invert_yaxis()
position, = ax.plot([],[], 'bo-', lw=2)
velocity, = ax.plot([],[], 'go-', lw=2)
acceleration, = ax.plot([],[], 'ro-', lw=2)

step = 0.01  # step for integration fun
fps = 30
time = 5  # time in seconds
total_time = 0


def init():
    global total_time 
    print("Total time:", total_time, "s")
    total_time += time
    y = y0.copy()
    position.set_data([],[])
    velocity.set_data([],[])
    acceleration.set_data([],[])
    return position, velocity, acceleration

def frame(i, step):
    global y
    # print("Frame", i)
    ny = euler(i*step, y, step, f)  # y = [position, velocity]
    a = f(i*step, y)[-1]
    position.set_data([2, 2], [-(L+ΔL), ny[0]])
    velocity.set_data([0, 0], [0, ny[1]])
    acceleration.set_data([-2, -2], [0, a/10])
    y = ny
    return position, velocity, acceleration

anim = animation.FuncAnimation(
            fig,
            func = frame,
            frames = fps*time,
            fargs = (step,),
            interval = 1000*step,
            init_func = init,
            blit=True
        )

plt.show()
# anim.save(
        # 'test.mp4',
        # fps=fps,
        # extra_args=['-vcodec', 'libx264']
    # )

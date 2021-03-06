import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import shared.euler as elr
#------------------------------
# y_v - system of equations, here an x' and V'
# def euler(iv, y_v, step, f):
    # return y_v + step * f(iv, y_v) 

g = 9.8
L = 3  # resting length of string
ΔL = 1  # spring delta uder a mass

x0 = -(L+ΔL) 
Δx = 2
ΔV = 0

m = 0.5
k = g*m/ΔL   # spring coefficient
b = 0.1  # damping coefficient

y0 = np.array([Δx, ΔV]) # initial position and velocity
y = y0.copy()

f = lambda iv, y_v : np.array([y_v[1], -(k/m)*y[0] - (b/m)*y_v[1]])
step = 0.01  # step for integration fun
integr = elr.heun2
#------------------------------
w = 7
h = 5
fig = plt.figure()
ax = plt.axes(xlim=[-w, w], ylim=[-h,h])
ax.grid()
ax.invert_yaxis()
fig.suptitle("Spring movement w/ Heun 2nd order method.", fontsize=14)
position, = ax.plot([],[], 'bo-', lw=2)
velocity, = ax.plot([],[], 'go-', lw=2)
acceleration, = ax.plot([],[], 'ro-', lw=2)

fps = int(1/step)
time = 20  # time in seconds

ax.text(-4, x0-0.2, "Acceleration/10",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(0, x0-0.2, "Velocity/5",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(4, x0-0.2, "Position",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)

ax.text(-5, 4, "Step size [s]: " + str(step),
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)


def init():
    y = y0.copy()
    position.set_data([],[])
    velocity.set_data([],[])
    acceleration.set_data([],[])
    return position, velocity, acceleration

def frame(i, step):
    global y
    # print("Frame", i)
    ny = integr(i*step, y, step, f)  # y = [position, velocity]
    a = f(i*step, y)[-1]
    position.set_data([4, 4], [x0, ny[0]])
    velocity.set_data([0, 0], [0, ny[1]/5])
    acceleration.set_data([-4, -4], [0, a/10])
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

# plt.show()
anim.save(
        'single.mp4',
        fps=fps,
        extra_args=['-vcodec', 'libx264']
    )

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
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
integr = elr.rk4
#------------------------------
w = 7
h = 5

fig = plt.figure()
ax = p3.Axes3D(fig)
# Setting the axes properties
ax.set_xlim3d([-w, w])
ax.set_xlabel('X')

ax.set_ylim3d([-w, w])
ax.set_ylabel('Y')

ax.set_zlim3d([-h, h])
ax.set_zlabel('Z')

ax.set_title('3D Spring')
# ax.grid()
ax.invert_zaxis()
position, = ax.plot([],[],[], 'bo-', lw=2)

fps = int(1/step)
time = 10  # time in seconds

Δt = 5
uptime = 0


def init():
    global uptime 
    print("Total time:", uptime, "s")
    uptime += Δt
    y = y0.copy()
    position.set_data([0, 0], [0, 0])
    position.set_3d_properties([x0, y[0]])
    return position,

def frame(i, step):
    global y
    y = integr(i*step, y, step, f)  # y = [position, velocity]
    position.set_data([0, 0], [0, 0])
    position.set_3d_properties([x0, y[0]])
    return position,

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
        # 'single.mp4',
        # fps=fps,
        # extra_args=['-vcodec', 'libx264']
    # )

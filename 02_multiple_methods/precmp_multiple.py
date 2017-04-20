import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import shared.euler as elr
import shared.precomp as pc
#------------------------------
g = 9.8     # gravity acceleration
L = 3       # resting length of string
ΔL = 1      # spring delta uder a mass
ΣL = L+ΔL   # total spring length at equilibrium
x0 = -(ΣL)  # spring hung point

m = 1       # mass of object attached to spring
k = g*m/ΔL  # spring coefficient
b = 0.5     # damping coefficient

Δx = (x0 + ΣL) + 2      # distance from equilibrium
ΔV = 0                  # initlia velocity
y0 = np.array([Δx, ΔV]) # initial conditions

f = lambda iv, y_v : np.array([y_v[1], -(k/m)*y_v[0] - (b/m)*y_v[1]])
#------------------------------
time = 20                     # time of animation in seconds

step = 0.02                   # step size for integration
int_frames = int(time/step)   # number of integration frames

interval = max(10, 1000*step) # interval between anim frames in ms
fps = int(1000/interval)      # animation frames per second 
frames = time * fps
amul = max(1, int(int_frames/frames))    # animation multiplier

# numerical integration methods:
y1 = pc.prcmp(elr.euler, y0, f, step, int_frames)     # Euler's method
y2 = pc.prcmp(elr.heun2, y0, f, step, int_frames)     # Heun's 2nd order method
y3 = pc.prcmp(elr.midpnt, y0, f, step, int_frames)    # Midpoint Euler's method
y4 = pc.prcmp(elr.back, y0, f, step, int_frames)      # Backward Euler's method
y5 = pc.prcmp(elr.rk4, y0, f, step, int_frames)       # Runge-Kutta 4 method

a1 = y1[::amul, :]
a2 = y2[::amul, :]
a3 = y3[::amul, :]
a4 = y4[::amul, :]
a5 = y5[::amul, :]
#------------------------------
w = 7
h = 5
fig = plt.figure()
ax = plt.axes(xlim=[-w, w], ylim=[-h,h])

ax.text(-6, x0-0.2, "Euler",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(-3, x0-0.2, "Heun",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(0, x0-0.2, "Midpoint",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(3, x0-0.2, "Backward",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)
ax.text(6, x0-0.2, "RK4",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)

ax.text(-4, 4, "Step size [s]: " + str(step),
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)

ax.grid()
ax.invert_yaxis()

p1, = ax.plot([],[], 'bo-', lw=2)
p2, = ax.plot([],[], 'go-', lw=2)
p3, = ax.plot([],[], 'ro-', lw=2)
p4, = ax.plot([],[], 'mo-', lw=2)
p5, = ax.plot([],[], 'co-', lw=2)

def frame(i, step):
    """
        Called for each frame of animation
    """
    p1.set_data([-6, -6], [x0, a1[i, 0]])
    p2.set_data([-3, -3], [x0, a2[i, 0]])
    p3.set_data([0, 0], [x0, a3[i, 0]])
    p4.set_data([3, 3], [x0, a4[i, 0]])
    p5.set_data([6, 6], [x0, a5[i, 0]])
    return p1, p2, p3, p4, p5

anim = animation.FuncAnimation(
            fig,
            func = frame,
            frames = frames,
            fargs = (step,),
            interval = 1000*step,
            blit=True
        )

plt.show()

# anim.save(
        # 'multiple03.mp4',
        # fps=fps,
        # extra_args=['-vcodec', 'libx264']
    # )

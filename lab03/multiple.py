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

m = 1
k = g*m/ΔL   # spring coefficient
b = 0.5  # damping coefficient

y0 = np.array([Δx, ΔV]) # initial position and velocity
y1 = y0.copy()
y2 = y0.copy()
y3 = y0.copy()
y4 = y0.copy()
y5 = y0.copy()

f = lambda iv, y_v : np.array([y_v[1], -(k/m)*y_v[0] - (b/m)*y_v[1]])
step = 0.0001  # step for integration fun
int1 = elr.euler
int2 = elr.heun
int3 = elr.midpnt
int4 = elr.back
int5 = elr.rk4
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
con, = ax.plot([],[], 'k--', lw=1)

fps = int(1/step)
time = 5  # time in seconds

Δt = 5
uptime = 0


def init():
    global uptime 
    print("Total time:", uptime, "s", y1[0],y4[0],y5[0])
    uptime += Δt
    p1.set_data([],[])
    p2.set_data([],[])
    p3.set_data([],[])
    p4.set_data([],[])
    p5.set_data([],[])
    con.set_data([],[])
    return p1, p2, p3, p4, p5, con

def frame(i, step):
    global y1, y2, y3, y4, y5
    # print("Frame", i)
    y1 = int1(i*step, y1, step, f)  # y = [position, velocity]
    y2 = int2(i*step, y2, step, f)
    y3 = int3(i*step, y3, step, f)
    y4 = int4(i*step, y4, step, f)
    y5 = int5(i*step, y5, step, f)
    p1.set_data([-6, -6], [x0, y1[0]])
    p2.set_data([-3, -3], [x0, y2[0]])
    p3.set_data([0, 0], [x0, y3[0]])
    p4.set_data([3, 3], [x0, y4[0]])
    p5.set_data([6, 6], [x0, y5[0]])
    # con.set_data([-6, -3, 0, 3, 6], [y1[0], y2[0], y3[0], y4[0], y5[0]])
    return p1, p2, p3, p4, p5, con

anim = animation.FuncAnimation(
            fig,
            func = frame,
            frames = fps*time,
            fargs = (step,),
            interval = 1000*step,
            init_func = init,
            blit=False
        )

plt.show()
# anim.save(
        # 'single.mp4',
        # fps=fps,
        # extra_args=['-vcodec', 'libx264']
    # )

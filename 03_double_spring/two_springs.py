import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import shared.euler as elr
#------------------------------
g = 9.8
# [mass 1, mass 2]
m = np.array([1,1])

# [rest Length, ΔL]
L1 = np.array([3, 0.5])
L2 = np.array([3, 0.5])

k = g*np.array([m[0]/L1[1], m[1]/L2[1]])   # spring coefficients

# L1[2] = (m[1]*g)/k[0]

x0 = -np.sum(L1)   # x0 in the sense of initial position for the whole system
x_start = x0 + np.array([np.sum(L1), np.sum(L1)+np.sum(L2)])  # starting positions of springs 
Δx =  x_start + np.array([3,3])  # initial position
ΔV = np.array([0,0])  # initial speed

b = 0.1  # damping coefficient - why would you use the different damping for each object?

y0 = np.array([Δx, ΔV]) # initial position and velocity
y = y0.copy()

#--------------- Diff function --------------
def fun(iv, yv):
    ΔL1 = yv[0,0]
    ΔL2 = yv[0,1] - (np.sum(L2) + ΔL1)
    xb2 = -k[1]/m[1] * ΔL2 - b/m[1]*yv[1,1]
    # xb1 = -k[0]/np.sum(m) * ΔL1 - b[0]*yv[1,0] + (-k[1]/np.sum(m) * ΔL2 - b[1]*yv[1,1]) 
    xb1 = -k[0]/m[0] * ΔL1 - b/m[0]*yv[1,0] + k[1]/m[1]*ΔL2 
    return np.array([yv[1,:], [xb1, xb2]])

f = fun  # lambda iv, y_v : np.array([y_v[1], -(k/m)*y_v[0] - (b/m)*y_v[1]])
step = 0.01  # step for integration fun
intm = elr.rk4
#------------------------------
w = 7
h = 15
fig = plt.figure()
ax = plt.axes(xlim=[-w, w], ylim=[-h,h])

ax.text(0, x0-0.2, "RK4",
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)

ax.text(4, -4, "Step size [s]: " + str(step),
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=10)

ax.grid()
ax.invert_yaxis()

p, = ax.plot([],[], 'y-', lw=2)
p1, = ax.plot([],[], 'mo', lw=2)
p2, = ax.plot([],[], 'co', lw=2)

fps = int(1/step)
Δt = 5
uptime = 0

def init():
    global uptime 
    print("Total time:", uptime, "s")
    uptime += Δt
    p.set_data([],[])
    p1.set_data([],[])
    p2.set_data([],[])
    return p, p1, p2 

def frame(i, step):
    global y
    # print("Frame", i)
    y = intm(i*step, y, step, f)  # y = [position, velocity]
    p.set_data([0, 0, 0], [x0, y[0,0], y[0,1]])
    p1.set_data([0], [y[0,0]])
    p2.set_data([0], [y[0,1]])
    return p, p1, p2 

anim = animation.FuncAnimation(
            fig,
            func = frame,
            frames = fps*Δt,
            fargs = (step,),
            interval = 1000*step,
            init_func = init,
            blit=True
        )

plt.show()
# anim.save(
        # 'double.mp4',
        # fps=fps,
        # extra_args=['-vcodec', 'libx264']
    # )

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import shared.euler as elr
import shared.precomp as pc
#------------------------------
g = 9.8
L1 = np.array([3, 0.5]) # [rest length, ΔL]
L2 = np.array([2, 0.5])
ΣL1 = np.sum(L1)    # first spring length at equilibrium under 1 mass
ΣL2 = np.sum(L2)    # second spring length at equilibrium under 1 mass
xh = -np.sum(L1)    # first string hung point

m = np.array([2,2])     # [mass 1, mass 2]
k = g * np.array([m[0]/L1[1], m[1]/L2[1]])

x0 = xh + np.array([ΣL1, ΣL1 + ΣL2])   # springs starting positions
Δx = x0 + np.array([1,1])       # initial position
ΔV = np.array([0,0])             # initial speed

b = 0.3  # damping coefficient characteristic to a fluid|environment

y0 = np.array([Δx, ΔV]) # initial conditions

#--------------- Diff function --------------
def diff(iv, yv):
    ΔL1 = yv[0,0]
    ΔL2 = yv[0,1] - (ΣL2 + ΔL1)
    xb2 = -k[1]/m[1] * ΔL2 - b/m[1]*yv[1,1]
    xb1 = -k[0]/m[0] * ΔL1 - b/m[0]*yv[1,0] + k[1]/m[1]*ΔL2  # motion resistance whould not be taken into account
    return np.array([yv[1,:], [xb1, xb2]])
#--------------------------------------------
time = 20                     # time of animation in seconds

step = 0.01                   # step size for integration
int_frames = int(time/step)   # number of integration frames

interval = max(10, 1000*step) # interval between anim frames in ms
fps = int(1000/interval)      # animation frames per second 
frames = time * fps
amul = max(1, int(int_frames/frames))    # animation multiplier

y = pc.prcmp(elr.rk4, y0, diff, step, int_frames)
a = y[::amul, :]
#--------------------------------------------
w = 4
h = 8
fig = plt.figure()
fig.suptitle("Two spring movement w/ RK4 integration.", fontsize=14)
ax = plt.axes(xlim=[-w, w], ylim=[xh-2,h])

# ax.text(0, xh-0.5, "RK4",
        # verticalalignment='bottom',
        # horizontalalignment='center',
        # fontsize=12)

ax.text(-2, 5, "Step size [s]: " + str(step),
        verticalalignment='bottom',
        horizontalalignment='center',
        fontsize=11)

ax.grid()
ax.invert_yaxis()

p, = ax.plot([],[], 'k-', lw=2)
p1, = ax.plot([],[], 'mo', lw=4)
p2, = ax.plot([],[], 'co', lw=2)

def frame(i, step):
    p.set_data([0, 0, 0], [xh, a[i,0,0], a[i,0,1]])
    p1.set_data([0], [ a[i,0,0] ])
    p2.set_data([0], [ a[i,0,1] ])
    return p, p1, p2 

anim = animation.FuncAnimation(
            fig,
            func = frame,
            frames = frames,
            fargs = (step,),
            interval = interval,
            blit=True
        )

# plt.show()

anim.save(
        'pre_double.mp4',
        fps=fps,
        extra_args=['-vcodec', 'libx264']
    )

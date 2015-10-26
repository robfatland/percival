# The top block 1 drops some random equations on top of one another, kinda artistic

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


##################
###
### Block 1 Random equations overlay
###
##################
#eqs = []
#eqs.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
#eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
#eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
#eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
#eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))


#plt.axes([0.025,0.025,0.95,0.95])

#for i in range(24):
#    index = np.random.randint(0,len(eqs))
#    eq = eqs[index]
#    size = np.random.uniform(12,32)
#    x,y = np.random.uniform(0,1,2)
#    alpha = np.random.uniform(0.25,.75)
#    plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
#             transform=plt.gca().transAxes, fontsize=size, clip_on=True)

#plt.xticks([]), plt.yticks([])
## savefig('../figures/text_ex.png',dpi=48)
#plt.show()

# This variant strips out the art and just places some text on the plot
#   Note that 'axes' operates in a plot-relative [0, 1] space; as do ticks and locations
plt.axes([0,0,1,1])
# eq = r"$\frac{17^2}{19^2}$"
eq = str(17)
size = 14
x,y=.75,.95
plt.text(x, y, eq, ha='center', va='center', color="#000000", alpha=1.0, transform=plt.gca().transAxes, fontsize=size, clip_on=True)
plt.xticks([.1,.2,.4,.8]), plt.yticks([.5,.6,.7])
plt.show()











##################
###
### Block 2 grid stuff
###
##################

#N = 8
## make an empty data set
#data = np.ones((N, N)) * np.nan
## wtf
#print range(3)[::-1]
## fill in some fake data
## for j in range(3)[::-1]:
#for j in [2, 1, 0]:
#    data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j
## make a figure + axes
#fig, ax = plt.subplots(1, 1, tight_layout=True)
## make color map
#my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
## set the 'bad' values (nan) to be white and transparent
#my_cmap.set_bad(color='orange', alpha=1.0)
## draw the grid
#for x in range(N + 1):
#    ax.axhline(x, lw=2, color='k', zorder=5)
#    ax.axvline(x, lw=2, color='k', zorder=5)
## draw the boxes
#ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
## turn off the axis labels
#ax.axis('off')
#plt.show()
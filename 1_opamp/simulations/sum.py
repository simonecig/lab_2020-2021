#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load data
simulation0 = pd.read_csv("sum/sum0.txt", delimiter='\t')
simulation = pd.read_csv("sum/sum.txt", delimiter='\t')
vo = pd.read_csv("sum/wpd_Vo.txt", delimiter=',')
v1 = pd.read_csv("sum/wpd_V1.txt", delimiter=',')

# create data for V2
v2sper = 5.095
n = 130
v2= np.linspace(0,0.002,n)


# shift data to align the simulation
# and conver in ms
offset = 1
vo['freq'] = (vo['freq'] + offset)*10**(-3)
v1['freq'] = (v1['freq'] + offset)*10**(-3)

# create subplots
fig, ax = plt.subplots(ncols=2)
fig.set_figwidth(8)
fig.set_figheight(5)


# plot first set of simulations
xmax=0.001
simulation0.plot(x='time', y='V(vout)', ax=ax[0], xlim=(0,xmax), label='$V_{out}$ simulazione',
                color='tomato', style='--')
simulation0.plot(x='time', y='V(n001)', ax=ax[0], xlim=(0,xmax), label='$V_2$ simulazione',
                color='maroon', style='--')
simulation0.plot(x='time', y='V(vin)', style='--', ax=ax[0], xlim=(0,xmax), label='$V_1$ simulazione',
                color='orange')

# plot corrected simulations
simulation.plot(x='time', y='V(vout)', ax=ax[1], xlim=(0,0.001), label='$V_{out}$ simulazione',
                color='tomato', style='--')
simulation.plot(x='time', y='V(n001)', ax=ax[1], xlim=(0,0.001), label='$V_2$ simulazione',
                color='maroon', style='--')
simulation.plot(x='time', y='V(vin)', style='--', ax=ax[1], xlim=(0,0.001), label='$V_1$ simulazione',
                color='orange')
# plot data on first plot
vo.plot(x='freq', y='v', ax=ax[0],label='$V_{out}$ webplotdig.', kind='scatter',  s=0.9,  color='blue')
v1.plot(x='freq', y='v', ax=ax[0], label='$V_1$ webplotdig', kind='scatter',s=0.9, color='midnightblue',
        xlabel='t (s)', ylabel='$V_{out}$ (V)')
ax[0].scatter(v2, np.linspace(v2sper,v2sper,n), label='$V_2$ webplotdig',s=0.9, color='cornflowerblue')
# plot data on second plot
vo.plot(x='freq', y='v', ax=ax[1],label='$V_{out}$ webplotdig.', kind='scatter',  s=0.9,  color='blue')
v1.plot(x='freq', y='v', ax=ax[1], label='$V_1$ webplotdig.', kind='scatter',s=0.9, color='midnightblue',
        xlabel='t (s)', ylabel='$V_{out}$ (V)')
ax[1].scatter(v2, np.linspace(v2sper,v2sper,n), label='$V_2$ webplotdig.',s=0.9, color='cornflowerblue')


#plot customization
ax[0].set_title("Simulazione con $V_2=5$ V")
ax[1].set_title("Simulazione con $V_2=5.01$ V")

ax[0].tick_params(axis='both', which='minor', direction='in')
ax[0].tick_params(axis='both', which='major', direction='in')
ax[0].minorticks_on()
ax[1].tick_params(axis='both', which='minor', direction='in')
ax[1].tick_params(axis='both', which='major', direction='in')
ax[1].minorticks_on()

#ax[0].legend(bbox_to_anchor=(1, 1, 1, 1),  mode="expand", ncol=2, loc='lower left',prop={'size': 8}, framealpha=1, markerscale=2.0)
ax[0].lege
ax[1].legend(bbox_to_anchor=(0, 0, 1, 0),  mode="expand", ncol=2,loc='lower left',prop={'size': 8}, framealpha=1, markerscale=2.0)


ax[0].ticklabel_format(axis='x', style='scientific', scilimits=(2,3))
ax[1].ticklabel_format(axis='x', style='scientific', scilimits=(2,3))
fig.tight_layout()

plt.show()
fig.savefig("sum_simulation.png",dpi=250)

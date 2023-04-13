#Author: Gopal Srivastava
#Date: April, 13 2023 

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.lines import Line2D

df = pd.read_csv("color.csv")
legend_breast = []
legend_lung = []
for cell in df.Cell_lines:
	if df[df.Cell_lines==cell]["Tissue"].values[0] == "breast":
		legend_breast.append(Line2D([0],[0],marker='o',markersize=10,color=df[df.Cell_lines==cell]["color"].values[0],label=cell,lw=0))
	elif df[df.Cell_lines==cell]["Tissue"].values[0] == "lung":
		legend_lung.append(Line2D([0],[0],marker='P',markersize=10,color=df[df.Cell_lines==cell]["color"].values[0],label=cell,lw=0))
	else:
		continue


lung = mlines.Line2D([], [], color=None, markerfacecolor=None, mec='blue', marker='P', markersize=10, pickradius=10, fillstyle=None, ls='', label='Lung')
breast = mlines.Line2D([], [], color=None, markerfacecolor=None, mec='blue', marker='o', ls='', markersize=10, pickradius=10, fillstyle=None, label='Breast')
fig = plt.figure(figsize=(10,6), dpi=300)
spec = fig.add_gridspec(2, 1)
plt.subplots_adjust(wspace=0, hspace=0)
ax10 = fig.add_subplot(spec[0, :])
ax10.legend(title='Lung cancer cell-lines', handles=legend_lung,numpoints=1,ncol=6,frameon=False, fontsize=10, loc='upper left',labelspacing=1.0,bbox_transform=fig.transFigure)
plt.axis('off')
ax11 = fig.add_subplot(spec[0, :])
ax11.legend(title='Breast cancer cell-lines', handles=legend_breast, numpoints=1, ncol=6,frameon=False, fontsize=10,loc='lower left',labelspacing=1.0,bbox_transform=fig.transFigure)
plt.axis('off')
plt.savefig("Figure/Legend.png", dpi=300, bbox_inches="tight")


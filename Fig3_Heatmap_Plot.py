import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import Counter
from scipy import stats
from matplotlib import pyplot, transforms
from PIL import Image
from io import BytesIO

df_all = pd.read_csv('Data/Correlation_DACS_TC_MCC.csv')
df = df_all[df_all['MCC']>=0]
tc_threshold_g = np.arange(0, 0.95, 0.05) #The interval does not include the ending point
tc_threshold = np.around(tc_threshold_g, decimals=3)
print('tc_threshold', tc_threshold)
mcc_threshold_g = np.arange(0, 0.95, 0.05)
mcc_threshold = np.around(mcc_threshold_g, decimals=3)
print('mcc_threshold', mcc_threshold)
positive_frac = np.zeros([len(tc_threshold), len(mcc_threshold)])

for i in range(len(tc_threshold)):
    tc_thr = tc_threshold[i]
    for j in range(len(mcc_threshold)):
        mcc_thr = mcc_threshold[j]
        df_higher = df[(df.TC >= tc_thr) & (df.MCC >= mcc_thr)]
        cnt = dict(Counter(df_higher['Kendall_class']))
        if -1.0 in cnt:
            frac = cnt[1.0] / (cnt[1.0] + cnt[-1.0])
        else:
            frac = cnt[1.0] / cnt[1.0]
        positive_frac[i,j] = frac
p_f = np.around(positive_frac, decimals=3)
print('positive_frac', p_f)

df_dacs_06 = df[df.DACS >= 0.6]
count_o6 = dict(Counter(df_dacs_06['Kendall_class']))
print(count_o6)
print('fraction of positive kendall tau with dacs>=0.6', count_o6[1]/(count_o6[1]+count_o6[-1]))
############## combined Heatmap ################################
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(8, 7), dpi=200,
                                             gridspec_kw={
                                                 'width_ratios': [5, 2],
                                                 'height_ratios': [1, 5],
                                                 'wspace': 0.04,
                                                 'hspace': 0.04})

## MCC histogram
sns.distplot(df.MCC, hist=False, ax=ax0, kde_kws={'lw':1.5,'color':'royalblue'}, hist_kws={"edgecolor": 'b'})
ax0.tick_params(axis='both', which='major', labelsize=14.5)
ax0.set(xlabel=None)
ax0.set(xticklabels=[])
ax0.set(ylabel=None)
ax0.set(yticklabels=[])
ax0.set_ylim(0, 10)
ax0.set_xlim(-0.05, 0.95)
l1 = ax0.lines[0]
x1 = l1.get_xydata()[:, 0]
y1 = l1.get_xydata()[:, 1]

ax0.fill_between(x1, y1, color="cornflowerblue", alpha=0.5)

## blank part
ax1.axis('off')

### heatmap
levels = np.linspace(0.5, 1.0, 11)
im = ax2.contourf(mcc_threshold,tc_threshold,positive_frac, levels=levels, cmap='Blues_r', origin='upper')
ax2.invert_yaxis()
# patch = patches.Circle((0.0, 0.0), radius=6, linestyle='--', transform=ax2.transData)
circle1 = plt.Circle((0.05, 0.05), 0.55, fill=False, ec='k', ls='--', lw=2)
ax2.add_patch(circle1)
ax2.set_xlabel('Drug action similarity',fontsize=15)
ax2.set_ylabel('Chemical similarity',fontsize=15)
ax2.set_ylim(0.95, -0.05)
ax2.set_xlim(-0.05, 0.95)
ax2.tick_params(axis='both', which='major', labelsize=14.5)

rect1 = patches.Rectangle((-0.05, 0.57), 0.048, 0.047, linewidth=1, facecolor='w', edgecolor=None)
rect2 = patches.Rectangle((0.57, -0.05), 0.048, 0.047, linewidth=1, facecolor='w', edgecolor=None)
ax2.add_patch(rect1)
ax2.add_patch(rect2)
ax2.hlines(y=0.6, xmin=-0.05, xmax=0, linewidth=0.5, color='grey')
ax2.vlines(x=0.6, ymin=-0.05, ymax=0, linewidth=0.5, color='grey')
### TC histogram
kde = stats.gaussian_kde(df.TC)
xx = np.linspace(0, 1, 1000)
base = pyplot.gca().transData
rot = transforms.Affine2D().rotate_deg(-90)
# define transformed line
ax3.plot(xx, kde(xx), 'royalblue', linewidth=1.5, transform= rot + base)
ax3.fill_between(xx, kde(xx), transform= rot + base, color="cornflowerblue", alpha=0.5)
ax3.set_ylim(-0.95, 0.05)
ax3.set_xlim(0, 5.5)
ax3.set(xlabel=None)
ax3.set(xticklabels=[])
ax3.set(ylabel=None)
ax3.set(yticklabels=[])
## color bar
cbar = plt.colorbar(im, ax=ax3, fraction=0.5)
cbar.ax.tick_params(labelsize=14.5)
cbar.set_label(label='Fraction of drug pairs', size=15)

for ax in (ax0, ax1, ax2, ax3):
    for spine in ax.spines.values():
        spine.set_edgecolor('grey')
plt.rc('axes', axisbelow=True)
ax0.set_axisbelow(True)
ax2.set_axisbelow(True)
ax3.set_axisbelow(True)
ax0.xaxis.grid(True)
ax2.grid()
ax3.yaxis.grid(True)
plt.show()

png1 = BytesIO()
fig.savefig(png1, format='png')
png2 = Image.open(png1)
png2.save('Figure/Figure3.tiff')
png1.close()

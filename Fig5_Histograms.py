import pandas as pd
import statistics
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from matplotlib.lines import Line2D
df = pd.read_csv('Data/AugmentedData.csv')
df_org = pd.read_csv('Data/Original_synergy_data.csv')
synergy_aug = df.Synergy_Score
synergy_org = df_org.SYNERGY_SCORE

tol_thr = len(synergy_aug)
maxv_thr = synergy_aug.max()
minv_thr = synergy_aug.min()
meanvalue_thr = statistics.mean(synergy_aug)
medianv_thr = statistics.median(synergy_aug)
modev_thr = statistics.mode(synergy_aug)
std_thr = statistics.stdev(synergy_aug)
print('augmentation data synergy statistics')
print('total number of cases',tol_thr)
print('max synergy value', maxv_thr)
print('min synergy value', minv_thr)
print('synergy mean', meanvalue_thr)
print('synergy median', medianv_thr)
print('synergy mode', modev_thr)
print('standard deviation', std_thr)

tol_org = len(synergy_org)
maxv_org = synergy_org.max()
minv_org = synergy_org.min()
meanvalue_org = statistics.mean(synergy_org)
medianv_org = statistics.median(synergy_org)
modev_org = statistics.mode(synergy_org)
std_org = statistics.stdev(synergy_org)
print('original synergy statistics')
print('total number of cases',tol_org)
print('max synergy value', maxv_org)
print('min synergy value', minv_org)
print('synergy mean', meanvalue_org)
print('synergy median', medianv_org)
print('synergy mode', modev_org)
print('standard deviation', std_org)


fig = plt.figure(dpi=200)
plt.hist(synergy_aug, 80, density=1, histtype='step', color='b', log=False,
         label='Augmented data',  linewidth=1.5)

plt.hist(synergy_org, 80, density=1, histtype='step', color='m', log=False,
         label='Original data',linestyle='dashed',
         linewidth=1.5)

plt.xlabel('Synergy score', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.xlim([-100, 150])
custom_lines = [Line2D([0,1],[0,1], linestyle='-', color='b', linewidth=1.5),
                Line2D([0,1],[0,1], linestyle='--', color='m', linewidth=1.5)]
                # Line2D([0], [0], color=cmap(1.), lw=4)]
plt.legend(custom_lines, ['Augmented data', 'Original data'], fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
# # plt.savefig('Figure/synergy_distribution_3.png', bbox_inches='tight')
# plt.savefig('Figure/synergy_distribution_step_histogram.png')
plt.show()

png1 = BytesIO()
fig.savefig(png1, format='png')
png2 = Image.open(png1)
png2.save('Figure/Figure5.tiff')
png1.close()


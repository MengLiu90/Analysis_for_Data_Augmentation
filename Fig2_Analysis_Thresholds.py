import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
from PIL import Image
from io import BytesIO

df = pd.read_csv('Correlation_DACS_TC_MCC.csv')
# ############ TC #######################
tc_threshold = np.arange(0, 0.95, 0.1) #The interval does not include the ending point
tc_threshold = np.around(tc_threshold, decimals=3)
rec_frac_high = []
for thr in tc_threshold:
    Tc_higher = df[df.TC >= thr]
    c_higher = dict(Counter(Tc_higher['Kendall_class']))
    fraction_higher = c_higher[1.0] / (len(Tc_higher)-c_higher[0.0])
    rec_frac_high.append(fraction_higher)

# ############ MCC #######################
mcc_threshold = np.arange(0, 0.95, 0.1) #The interval does not include the ending point
rec_fract_high = []
rec_fract_low = []
count_all_Kendall = dict(Counter(df['Kendall_class']))
for thr in mcc_threshold:
    MCC_higher = df[df.MCC >= thr]
    MCC_lower = df[df.MCC < thr]

    cnt_higher = dict(Counter(MCC_higher['Kendall_class']))
    cnt_lower = dict(Counter(MCC_lower['Kendall_class']))
    if -1.0 in cnt_higher:
        frac_higher = cnt_higher[1.0] / (cnt_higher[1.0] + cnt_higher[-1.0])
    else:
        frac_higher = cnt_higher[1.0] / cnt_higher[1.0]
    frac_lower = cnt_lower[1.0] / (cnt_lower[1.0] + cnt_lower[-1.0])
    rec_fract_high.append(frac_higher)
    rec_fract_low.append(frac_lower)

#################### random similarity #########
random_thr = np.arange(0, 0.95, 0.1)
frac_positives = []
for thr in random_thr:
    higher = df[df['random_similarity'] >= thr]
    Higher_cnt = dict(Counter(higher['Kendall_class']))
    frac_positive = Higher_cnt[1.0] / (Higher_cnt[1.0] + Higher_cnt[-1.0])
    frac_positives.append(frac_positive)

#### smoothen curves ####
XX = np.array([0.7])
YY = np.array([1])

Spline = make_interp_spline(tc_threshold, rec_frac_high)
X = np.linspace(0.1, 0.6, 100)
Y = Spline(X)
X_all = np.concatenate((X, XX))
Y_all = np.concatenate((Y, YY))

cubic_interp_model = interp1d(mcc_threshold, rec_fract_high, kind = "cubic")
A = np.linspace(0.1, 0.6, 500)
B = cubic_interp_model(A)
A_all = np.concatenate((A, XX))
B_all = np.concatenate((B, YY))

random_interp = make_interp_spline(random_thr, frac_positives)
M = np.linspace(0.1, 0.7, 100)
N = random_interp(M)


fig2 = plt.figure(dpi=200)
plt.plot(X_all, Y_all, color='blue', label="Chemical similarity")
plt.plot(A_all, B_all, 'm--', label="Drug action similarity")
plt.plot(M, N, 'k:', label="Random similarity")
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.legend(loc="upper left", fontsize=12)
plt.xlabel('Similarity threshold', fontsize=12)
plt.ylabel('Fraction of drug pairs', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()

png1 = BytesIO()
fig2.savefig(png1, format='png')
png2 = Image.open(png1)
png2.save('Figure/Figure2.tiff')
png1.close()

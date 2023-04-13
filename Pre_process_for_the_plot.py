import pandas as pd
import numpy as np
from collections import Counter
import os
df1 = pd.read_csv('Data/Correlation_DACS_TC_MCC.csv')
df = df1[df1.MCC > 0]
columns = ["DACS"]
df_synergy = pd.read_csv('Data/DACS_score_between_original_drug_and_similar_drugs.csv',usecols=columns)
data_dir = 'Data/for_intersection_plots'
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
## case count with DACS threshold ##
cnt_dacs_threshold = np.arange(0, 1.4, 0.01)
frac_dacs_threshold = np.arange(0, 1.4, 0.1)

dacs_count_all = np.zeros(len(cnt_dacs_threshold))
positive_frac_dacs = np.zeros(len(frac_dacs_threshold))

## cases count in dacs_score_between_original_drug_and_similar_drugs.csv dataset
for l in range(len(cnt_dacs_threshold)):
    dacs_thr = cnt_dacs_threshold[l]
    df_dacs_h = df_synergy[df_synergy.DACS >= dacs_thr] # all cases count
    dacs_count_all[l] = len(df_dacs_h)

## normalize dacs_count_all by max(dacs_count_all) to (0, 1]
# normalized_count_all = dacs_count_all/max(dacs_count_all)

## fraction of positives with DACS threshold ##
for q in range(len(frac_dacs_threshold)):
    dacs_thr = frac_dacs_threshold[q]
    df_dacs_h = df[df.DACS >= dacs_thr]
    cnt = dict(Counter(df_dacs_h['Kendall_class']))
    if -1.0 in cnt:
        dacs_frac = cnt[1.0] / (cnt[1.0] + cnt[-1.0])
    else:
        dacs_frac = cnt[1.0] / cnt[1.0]
    positive_frac_dacs[q] = dacs_frac

## convert the data into csv file to make plots in MATLAB
## to use MATLAB is to explicitly find the intersection point, not an approximate value
DF1 = pd.DataFrame(cnt_dacs_threshold)
DF1.to_csv('Data/for_intersection_plots/cnt_dacs_threshold.csv', header=False, index=False)
DF2 = pd.DataFrame(dacs_count_all)
DF2.to_csv('Data/for_intersection_plots/dacs_count_all.csv', header=False, index=False)
DF3 = pd.DataFrame(frac_dacs_threshold)
DF3.to_csv('Data/for_intersection_plots/frac_dacs_threshold.csv', header=False, index=False)
DF4 = pd.DataFrame(positive_frac_dacs)
DF4.to_csv('Data/for_intersection_plots/positive_frac_dacs.csv', header=False, index=False)
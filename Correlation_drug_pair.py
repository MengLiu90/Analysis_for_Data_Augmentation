import pandas as pd
import numpy as np
import scipy.stats

df_ic50 = pd.read_csv('Data/IC50Values.csv')
df_tc_mcc = pd.read_csv('Data/TC_MCC_for_drugpairs.csv')

df_tc_mcc["Kendall"] = np.nan
#The Spearman’s rho and Kendall’s tau-b statistics
df_ic50['tissue_cell'] = df_ic50['Tissue'] + '_' + df_ic50['Cell_lines']
cnt_0 = 0
cnt_1 = 0
cnt_more = 0
for i in range(len(df_tc_mcc)):#len(df_tc_mcc)
    dr1_cal = pd.DataFrame(columns=df_ic50.columns)
    dr2_cal = pd.DataFrame(columns=df_ic50.columns)

    dr1 = df_tc_mcc.iloc[i]['CID_1']
    dr2 = df_tc_mcc.iloc[i]['CID_2'] #get drug names in a drug-pair
    dr1_ic50 = df_ic50[df_ic50.CIDs == dr1]
    dr2_ic50 = df_ic50[df_ic50.CIDs == dr2] #get cases for each drug in the ic50 file

    dr1_tissue_cell = dr1_ic50.tissue_cell.unique().tolist()
    dr2_tissue_cell = dr2_ic50.tissue_cell.unique().tolist()

    dr1_set = set(dr1_tissue_cell)
    dr2_set = set(dr2_tissue_cell)
    common_ts_cl = dr1_set.intersection(dr2_set) #get the common tissue_cell

    if len(common_ts_cl) == 0:
        cnt_0 += 1
        df_tc_mcc.at[i, 'Kendall'] = 0# if no common tissue_cell, correlation set as 0
    elif len(common_ts_cl) == 1:
        cnt_1 += 1
        # only one common tissue_cell, correlation cannot be calculated, set as 0
        # because it will cause 0/0, which is undefined.
        df_tc_mcc.at[i, 'Kendall'] = 0
    else: #len(common_tis) > 1
        cnt_more += 1
        for common in common_ts_cl:
            dr1_inter = dr1_ic50[dr1_ic50.tissue_cell == common]
            dr2_inter = dr2_ic50[dr2_ic50.tissue_cell == common]
            dr1_cal = pd.concat([dr1_cal, dr1_inter])
            dr2_cal = pd.concat([dr2_cal, dr2_inter])

        df_tc_mcc.at[i, 'Kendall'] = scipy.stats.kendalltau(dr1_cal.logIC50, dr2_cal.logIC50)[0]
df_tc_mcc.to_csv('Correlation.csv', index=False)
# print('# of pairs with NO cell in common', cnt_0)
# print('# of pairs with one cell in common', cnt_1)
# print('# of pairs with at least 2 cells in common', cnt_more)


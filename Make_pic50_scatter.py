#Author: Gopal Srivastava
#Date: April, 13 2023 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plots(ic50, cid2, cid1="CIDs11597571"):
	pair = ic50[(ic50.CIDs==cid1) | (ic50.CIDs==cid2)]
	pair = pair.groupby("Cell_lines")
	pair_df = pd.DataFrame()
	for p in pair:
		if len(p[1]) > 1:
			pair_df = pd.concat([pair_df, p[1]], ignore_index=True)
	pair_df = pair_df.groupby("CIDs")
	pair_data = pd.DataFrame()
	for p in pair_df:
		cid, p = p[0], p[1].set_index("Cell_lines")
		p = p.rename(columns={"logIC50":names[cid]})
		pair_data = pd.concat([pair_data, p[["Tissue", names[cid]]]], axis=1)
	pair_data = pair_data.reset_index()
	pair_data = pair_data.rename(columns={"index":"Cell_lines"})
	pair_data = pair_data.loc[:,~pair_data.columns.duplicated()].copy()
	return pair_data
	


if __name__=="__main__":
	params = {'mathtext.default': 'regular' }          
	plt.rcParams.update(params)
	pair_drugs = ["CIDs06442177", "CIDs00004261", "CIDs00148177", "CIDs24856436", "CIDs05311497", "CIDs25227436"]
	names = {"CIDs11597571":"Crizotinib", "CIDs06442177":"Everolimus", "CIDs00004261":"Entinostat", "CIDs00148177":"Perifosine", "CIDs24856436":"Adavosertib", "CIDs05311497":"Vinorelbine", "CIDs25227436":"Capivasertib"}

	ic50 = pd.read_csv("Data/IC50Values.csv")
	markers = {"breast":"o", "lung":"P"}
	colors = {"BT474": "b", "CAMA1": "g", "HCC1500":"r", "MCF7":"c", "MDAMB361":"m", "T47D":"y", "UACC812":"tab:orange", "HCC1419":"tab:purple", "MDAMB175VII":"sienna", "NCIH1703":"saddlebrown", "NCIH520":"darkgoldenrod", "NCIH1299":"gold", "NCIH1793":"olive", "NCIH1975":"darkslategray", "NCIH2085":"deepskyblue", "NCIH2170":"deeppink", "NCIH2228":"cornflowerblue", "NCIH2291":"slategray", "NCIH23":"k", "NCIH358":"midnightblue", "CALU6":"purple", "NCIH838":"lightpink"}
	annotation = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
	fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10,6), dpi=300, sharex=False)#, constrained_layout=False)
	axes = axes.flatten()
	for i, drug in enumerate(pair_drugs):
		pair_data = plots(ic50, drug)
		for cell in pair_data.Cell_lines:
			pair_data.loc[pair_data.Cell_lines==cell, "color"] = colors[cell]
		for t in list(pair_data.Tissue.unique()):
			pair_data.loc[pair_data.Tissue==t, 'style'] = markers[t]
		

		for m, d in pair_data.groupby('style'):
			ax = axes[i].scatter(x=d["Crizotinib"], y=d[names[drug]], s=20, c=d['color'], marker=m, label=list(d.Tissue.unique())[0])
			sns.regplot(data=pair_data, x="Crizotinib", y=names[drug], scatter=False, line_kws={"color":"dodgerblue","lw":2}, ci=None, ax=axes[i])
			axes[i].set_xlabel(r'crizotinib, pIC$_{50}$', fontsize=10, labelpad=0.3)
			axes[i].set_ylabel("$"+names[drug].lower()+", pIC_{50}$", fontsize=10,labelpad=0.3)
			axes[i].annotate(annotation[i], xy=(-0.3,1.05), fontsize=10, xycoords="axes fraction")
	fig.tight_layout()	
	plt.savefig("Figure/Fig1.png", dpi=300, bbox_inches="tight")

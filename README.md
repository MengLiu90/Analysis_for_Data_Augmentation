# Analysis_for_Synergy_Data_Augmentation
This repository provides the analysis process for the synergy data augmentation. It contains the datasets utilized in the analysis and generates the figures that are presented in the paper to describe the analysis process.
## Dependencies
1. Pandas 1.1.3
2. Numpy 1.19.2
3. Scipy 1.7.3
4. Matplotlib 3.5.1
5. Seaborn 0.11.2
6. PIL 9.0.1
## Usage
The following steps provide a guide to reproduce the analysis results presented in the paper.
### Generation of Figure 1 
Similarity measure for cellular responses to drug treatment<br />
1. Run ```python Correlation_drug_pair.py```<br />
This will calculate the Kendall tau correlation coefficients for the drug pairs.
2. Run ```python make_pic50_scatter.py```<br />
3. Run ```python legend.py```<br />
4. Run ```python concat_figures.py```<br />
### Generation of Figure 2 
Relation between drug similarity and pharmacological effects<br />
Run ```python Fig2_Analysis_Thresholds.py```<br />
### Generation of Figure 3 
Heatmap of the fraction of drug pairs with positively correlated pharmacological effects<br />
Run ```python Fig3_Heatmap_Plot.py```<br />
### Generation of Figure 4
Optimal DACS threshold for data augmentation<br />
1. Download the dataset ```DACS_score_between_original_drug_and_similar_drugs.csv``` from the link https://osf.io/kd9e7/ and put the dataset in ```Data``` folder<br />
2. Run ```Pre_process_for_the_plot.py```<br />
3. Run ```Fig4_Analysis_Intersection.m``` in MATLAB
### Generation of Figure 5
Distribution plots of the synergy scores in original and augmented datasets<br />
1. Download the dataset ```AugmentedData.csv``` from link https://osf.io/kd9e7/ and put the dataset in ```Data``` folder<br />
2. Run ```Fig5_Histograms.py```

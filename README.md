# Analysis_for_Synergy_Data_Augmentation
This repository provides the analysis process for the synergy data augmentation. It contains the datasets utilized in the analysis and generates the figures that are presented in the paper to describe the analysis process.
## Dependencies
1. Pandas 1.1.3
2. Numpy 1.19.2
## Usage
The following steps provide a guide to reproduce the analysis results presented in the paper.
### Generation of Figure 1
1. Run ```python Correlation_drug_pair.py```<br />
This will calculate the Kendall tau correlation coefficients for the drug pairs.
2. Run ```python make_pic50_scatter.py```<br />
This code produces Figure 1 using the file generated by the first step. 

### Generation of Figure 2

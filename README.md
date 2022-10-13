# VS_project2
subproject for "Python for Biologists HT22"

## Program aim
can be used to combine RNAseq and Proteomics data 

## How to run
python merging_data.py

## Required libraries 
* import pandas as pd
* import numpy as np
* from bioinfokit import analys, visuz

## Files used in the program
Located in Folder "supp_files"

- **Proteome_FOX_1_OE.csv** - data for Proteomics analysis of cells with OE of transcription factor
- **RNAseq_FOX_1_OE.csv** - data for RNAseq analysis of cells with OE of transcription factor

## Files created during the run
Located in Folder **"supp_files"**
- **FOX_1_OE_combined.csv** - unsorted combined RNAseq and Proteomics data
- **FOX_1_OE_combined_selected.csv** - selected genes with p<0.05 and fdr<0.05 
- **"heatmap.png"** - heatmap of selected genes


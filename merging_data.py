# Import libraries
import pandas as pd
import numpy as np
from bioinfokit import analys, visuz

# Import Proteome data to panda dataframe
data_p = pd.read_csv("supp_files/Proteome_FOX_1_OE.csv", delimiter ="\t", usecols = ["GeneSymbol", "logFC_Pr","pvals_Pr"])                   
print("\n### Proteome_FOX_1_OE")
print(data_p.head(2), "\n")

# Control data type in Proteome dataframe
data_p.info()

# Convert values with incorrect datatype to float64
data_p.logFC_Pr = data_p.logFC_Pr.astype(np.float64)
data_p.pvals_Pr = data_p.pvals_Pr.astype(np.float64)
print("\n*** Control for datatype after correction")
data_p.info()

# Remove rows with null values
print("\nRemove rows with missing values:")
print("Before: ", len(data_p))
data_p = data_p[data_p.logFC_Pr != 0]
data_p = data_p[data_p.pvals_Pr != 0]
print("After: ", len(data_p))

# Check for missing values and drop those if exist
data_p.dropna(inplace=True)
print("\nRemove rows with NaN values")
print("Remaining genes in combined dataframe: ", len(data_p))
print("----------------\n")

# Import RNAseq data to panda dataframe
data_r = pd.read_csv("supp_files/RNAseq_FOX_1_OE.csv", delimiter ="\t", usecols = ["GeneSymbol", "logFC_RNA", "FDR_RNA"])
print("### RNAseq_FOX_1_OE\n")
print(data_r.head(2), "\n")

# Control data type in dataframe
print("\n*** Control for datatype in RNAseq")
data_r.info()

# Remove rows with null values
print("\n*** Remove rows with missing or NaN values in RNAseq:")
print("Before: ", len(data_r))
data_r = data_r[data_r.logFC_RNA != 0]
data_r = data_r[data_r.FDR_RNA != 0]
data_r.dropna(inplace=True)
print("After: ", len(data_r))

# Assign row index to the 1st column ("GeneSymbol") in both Proteomics and RNAseq 
data_p.set_index("GeneSymbol")
data_r.set_index("GeneSymbol")

# Print total amount of genes in the Proteomics data
print("\n--------------------------------")
print("Genes in Proteomics data: ", len(data_p))
print("Genes in RNAseq data: ", len(data_r))
print("--------------------------------\n")

# Create dataframe with merged data from both frames based on index ("GeneSymbol")
df = pd.merge(data_p, data_r, how="inner", on=["GeneSymbol"]) 
print("*** Dataframe with merged data \n", df.head(2))

# Genes detected in both Proteomics and RNAseq
print("\n--------------------------------")
print("Genes detected in both Proteomics and RNAseq ", len(df))

# Select Genes with p<0.05 and FDR<0.05 for Proteomics and RNAseq correspondently 
dt_selected= df[(df["pvals_Pr"] < 0.05) & (df["FDR_RNA"] < 0.05) ]
print("Genes with p<0.05 and fdr<0.05: ", len(dt_selected))
print("--------------------------------\n")

# Export combined and selected data to csv
df.to_csv("supp_files/FOX_1_OE_combined.csv", encoding='utf-8', sep='\t', index=False)
dt_selected.to_csv("supp_files/FOX_1_OE_combined_selected.csv", encoding='utf-8', sep='\t', index=False)

# Heatmap of selected RNAseq and Proteomics data
heatmap = pd.DataFrame(dt_selected, columns = ["GeneSymbol", "logFC_Pr", "logFC_RNA"])
heatmap = heatmap.set_index(df.columns[0])  # Set gene names as index
visuz.gene_exp.hmap(df=heatmap, dim=(3, 6), tickfont=(6, 4))

# User notification
print('\n*** SUMMARY \n Saved files: ')
print('"FOX_1_OE_combined.csv" - unsorted combined RNAseq and Proteomics data')
print('"FOX_1_OE_combined_selected.csv" - selected genes with p<0.05 and fdr<0.05 ')
print('"heatmap.png" - Heatmap of selected genes')
print("\nJob finished")

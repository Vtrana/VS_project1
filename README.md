# VS_project1
project for "Python for Biologists HT22"

## Program aim
can be used to combine RNAseq and Proteomics data 

## To install required libraries with conda
* conda install -c anaconda pandas
* conda install numpy
* conda install -c bioconda bioinfokit

## For test run one can create and use virtual environment
1. Open Anaconda Promt
2. Navigate to folder VS_project1 (cloned using GIT bash)
3. Create test environment using command: `> conda env create -n demo_env --file environment.yml`
4. To activate this environment, use `> conda activate demo-env`
5. To deactivate an active environment, use `> conda deactivate`
6. To remove test environment, use `> conda env remove -n demo-env`

## How to run
`python merging_data.py`

## Files used in the program
Located in Folder "supp_files"

- **Proteome_FOX_1_OE.csv** - data for Proteomics analysis of cells with OE of transcription factor
- **RNAseq_FOX_1_OE.csv** - data for RNAseq analysis of cells with OE of transcription factor

## Files created during the run
Located in Folder **"supp_files"**
- **FOX_1_OE_combined.csv** - unsorted combined RNAseq and Proteomics data
- **FOX_1_OE_combined_selected.csv** - selected genes with p<0.05 and fdr<0.05 
- **"heatmap.png"** - heatmap of selected genes


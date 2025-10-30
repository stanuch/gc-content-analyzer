# 📊 GC Content Analyzer
## 📋 Overview

GC Content Analyzer is a lightweight bioinformatics tool written in Python for analyzing the GC content of DNA sequences provided in FASTA format. 
It computes both global GC percentage and local GC content using a sliding window approach. The app generates a graph of the GC content percentage across the sequence and calculates the CpG and GpC islands count per 100 nucleotides (nt) in the sequence.

<p align="center">
  <img width="680" height="280" alt="gc content" src="https://github.com/user-attachments/assets/42ea620c-4183-4b2d-9e3e-d72959d03d36" />
  <img width="680" height="280" alt="cpg counts" src="https://github.com/user-attachments/assets/fbcca3da-0ef8-486e-b70f-be24e6b31116" />
</p>




## ⭐️ Current Features
- Read DNA/RNA sequences from FASTA files
- Calculate global GC % content
- Display results in the terminal
- Perform sliding window GC% analysis
- Create a plot with GC data

## 💾 Requirements:

- Python
- Biopython
- Matplotlib

## 💻 How to use
**1. Clone the repository:**
```bash
git clone https://github.com/stanuch/seq-global-align.git
cd dna-global-align
```
**2. Install dependencies**
```bash
pip install -r requirements.txt
```
**3. Prepare your FASTA file**
- Place your sequence files in the /sequences folder
- Use the .fasta format
- When running the program, enter only the file name without the extension (e.g., for seq1.fasta, just type seq1)

**4. Run the program**
```bash
python main.py
```

## 📖 Theoretical background
**Base pairing and stability**
- A–T pairs: 2 hydrogen bonds
- G–C pairs: 3 hydrogen bonds → stronger and more stable
- Higher GC% increases DNA stability and melting temperature.

**PCR and cloning**
- DNA with high GC% may require higher denaturation temperature.
- Primers should ideally have 40–60% GC content for stable binding.

**CpG islands**
- Regions ≥200 bp, GC ≥50%, and CpG observed/expected ratio >0.6.
- Often found near promoters and transcription start sites.
- Important for studying epigenetics, methylation, and gene regulation.


## 📚 References

- CpG site: https://en.wikipedia.org/wiki/CpG_site
- Coutinho, T. J. D., Franco, G. R., & Lobo, F. P. (2015). Homology-independent metrics for comparative genomics. Computational and Structural Biotechnology Journal, 13, 352–357

## ✅ To-Do

- Export results to CSV
- GUI

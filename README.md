# 📊 GC Content Analyzer
## 📋 Overview

GC Content Analyzer is a lightweight bioinformatics tool written in Python for analyzing the GC content of DNA sequences provided in FASTA format.
It computes both global GC percentage and local GC content using a sliding window approach.

GC content is a critical parameter in molecular biology:

- It affects DNA stability due to stronger G≡C base pairing (3 hydrogen bonds).
- It influences PCR performance, primer design, and cloning efficiency.
- GC-rich regions (CpG islands) are often associated with promoter regions and gene regulation.

## ⭐️ Current Features
- Read DNA/RNA sequences from FASTA files
- Calculate global GC % content
- Display results in the terminal (not fully done)
- ~~Perform sliding window GC% analysis~~

## 💾 Requirements:

- Python 3.8+
- Biopython (FASTA parsing)
- ~~Matplotlib / Plotly~~

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
- Place your sequence files in the sequences/ folder.
- Use the .fasta format.
- When running the program, enter only the file name without the extension (e.g., for seq1.fasta, just type seq1).

**4. Run the program**
```bash
python src/main.py
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

- Visualization of GC% distribution along sequences (Matplotlib / Plotly)
- Support for multiple sequences in one FASTA file
- Export results to CSV
- Web-based interface for interactive analysis

import os
from Bio import SeqIO
from sliding_window import sliding_gc_content

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, "..", "sequences") # fasta files path
    return os.path.join(seq_dir, f"{filename}.fasta")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def gc_content(seq_path):
    for record in SeqIO.parse(seq_path, "fasta"):
        counter = 0
        for nucleotide in record.seq:
            if nucleotide in ['C', 'G']:
                counter += 1
        gc_content = (counter / len(record.seq)) * 100
        return gc_content
    
def nucleotide_content(seq_path):
    for record in SeqIO.parse(seq_path, "fasta"):
        a_count = record.seq.count('A')
        t_count = record.seq.count('T')
        c_count = record.seq.count('C')
        g_count = record.seq.count('G')
        total = len(record.seq)
        return {
            'A': (a_count / total) * 100,
            'T': (t_count / total) * 100,
            'C': (c_count / total) * 100,
            'G': (g_count / total) * 100
        }

def main():
    cls()
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq_filename = input("Enter the name of your sequence file (without extension): ")

    seq_path = get_file_path(base_dir, seq_filename)
    if not os.path.exists(seq_path):
        print(f"File {seq_path} does not exist.")
        return
    
    print(f"GC content: {gc_content(seq_path):.2f}%")
    nuc_content = nucleotide_content(seq_path)
    print(f"Nucleotide content: \nA: {nuc_content['A']:.2f}% \nT: {nuc_content['T']:.2f}% \nC: {nuc_content['C']:.2f}% \nG: {nuc_content['G']:.2f}%")

    for bin, percentage in sliding_gc_content(seq_path, 25, 2):
        print(bin, f"{percentage:.2f}")


if __name__ == "__main__":
    main()
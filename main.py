import os
from Bio import SeqIO
from sliding_window import sliding_gc_content
from graph import create_x_values, create_y_values, gc_content_graph

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, ".", "sequences") # fasta files path
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
        u_count = record.seq.count('U') # in case of RNA
        c_count = record.seq.count('C')
        g_count = record.seq.count('G')
        total = len(record.seq)
        if 'U' in str(record.seq) and 'T' not in str(record.seq): # RNA
            return {
                'A': (a_count / total) * 100,
                'U': (u_count / total) * 100,
                'C': (c_count / total) * 100,
                'G': (g_count / total) * 100
            }
        else:  # DNA
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

    # Check if file exists and get full path
    seq_path = get_file_path(base_dir, seq_filename)
    if not os.path.exists(seq_path):
        print(f"File {seq_path} does not exist.")
        return
    
    # Overall GC and nucleotide content
    print(f"Number of nucleotides in the sequence: {len(next(SeqIO.parse(seq_path, 'fasta')).seq)}")
    print(f"GC content: {gc_content(seq_path):.2f}%")
    nuc_content = nucleotide_content(seq_path)

    if 'U' in nuc_content:
        print(f"Nucleotide content: \nA: {nuc_content['A']:.2f}% \nU: {nuc_content['U']:.2f}% \nC: {nuc_content['C']:.2f}% \nG: {nuc_content['G']:.2f}%")
    else:
        print(f"Nucleotide content: \nA: {nuc_content['A']:.2f}% \nT: {nuc_content['T']:.2f}% \nC: {nuc_content['C']:.2f}% \nG: {nuc_content['G']:.2f}%")

    # Sliding window GC content
    window_size = int(input("\nEnter window size - for sliding window analysis (press enter for default 26): ") or 26)
    if window_size < 1:
        print("Window size must be a positive integer.")
        return
    step_size = int(input("Enter step size (press enter for default 2): ") or 2)
    if step_size < 1:
        print("Step size must be a positive integer.")
        return
    print(f"\nSliding window GC content (window size: {window_size}, step size: {step_size}):")
    # for bin, percentage in sliding_gc_content(seq_path, window_size, step_size):
    #     print(bin, f"{percentage:.2f}")
    
    gc_list = sliding_gc_content(seq_path, window_size, step_size)

    x, y = create_x_values(gc_list), create_y_values(gc_list)
    
    gc_content_graph(x, y)

if __name__ == "__main__":
    main()
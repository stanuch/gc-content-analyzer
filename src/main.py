import os
from Bio import SeqIO
from analysis import gc_content, nucleotide_content, sliding_gc_content, cpg_islands, gpc_islands
from graph import create_x_values, create_y_values, gc_content_graph, cpg_islands_graph
from analysis import gc_content, nucleotide_content, sliding_gc_content, cpg_islands, gpc_islands

def get_file_path(base_dir: str, filename: str) -> str:
    seq_dir = os.path.join(base_dir, "..", "sequences")
    return os.path.join(seq_dir, f"{filename}.fasta")

def cls() -> None:
    os.system("cls" if os.name=="nt" else "clear")
    
def main() -> None:
    cls()
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq_filename = input("Enter the name of your sequence file (without extension): ")

    seq_path = get_file_path(base_dir, seq_filename)
    if not os.path.exists(seq_path):
        print(f"File {seq_path} does not exist.")
        return
    
    # Overall GC and nucleotide content
    print(f"Number of nucleotides in the sequence: {len(next(SeqIO.parse(seq_path, "fasta")).seq)}")
    print(f"GC content: {gc_content(seq_path):.2f}%")
    nuc_content = nucleotide_content(seq_path)

    if "U" in nuc_content:
        print(f"\nNucleotide content: \nA: {nuc_content["A"]:.2f}% \nU: {nuc_content["U"]:.2f}% \nC: {nuc_content["C"]:.2f}% \nG: {nuc_content["G"]:.2f}%")
    else:
        print(f"\nNucleotide content: \nA: {nuc_content["A"]:.2f}% \nT: {nuc_content["T"]:.2f}% \nC: {nuc_content["C"]:.2f}% \nG: {nuc_content["G"]:.2f}%")

    # Sliding window GC content
    window_size = int(input("\nEnter window size - for sliding window analysis (press enter for default 26): ") or 26)
    if window_size < 1:
        print("Window size must be a positive integer.")
        return
    step_size = int(input("Enter step size (press enter for default 2): ") or 2)
    if step_size < 1:
        print("Step size must be a positive integer.")
        return
    print(f"Sliding window GC content (window size: {window_size}, step size: {step_size}):")
    
    # Creating and displaying the graph
    gc_list = sliding_gc_content(seq_path, window_size, step_size)
    x, y = create_x_values(gc_list), create_y_values(gc_list)
    gc_content_graph(x, y)

    # CpG islands calculations and graph
    cpgs = cpg_islands(seq_path)
    gpcs = gpc_islands(seq_path)
    cpg_islands_graph(cpgs, gpcs)

if __name__ == "__main__":
    main()
import os
from Bio import SeqIO

def get_file_path(base_dir, filename):
    seq_dir = os.path.join(base_dir, "..", "sequences") # fasta files path
    return os.path.join(seq_dir, f"{filename}.fasta")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()
    base_dir = os.path.dirname(os.path.abspath(__file__)) # main.py path

    seq_filename = input("Enter the name of your sequence file (without extension): ")

    seq_path = get_file_path(base_dir, seq_filename)
    if not os.path.exists(seq_path):
        print(f"File {seq_path} does not exist.")
        return
    
    for record in SeqIO.parse(seq_path, "fasta"):
        counter = 0
        print(f"Sequence ID: {record.id}")
        print(f"Sequence Length: {len(record.seq)}")
        for nucleotide in record.seq:
            if nucleotide in ['C', 'G']:
                counter += 1
        gc_content = (counter / len(record.seq)) * 100
        print(f"GC Content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
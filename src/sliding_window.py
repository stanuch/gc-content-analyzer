from Bio import SeqIO

def sliding_gc_content(sequence_path, window_size, step_size):
    for record in SeqIO.parse(sequence_path, "fasta"):
        sequence = str(record.seq)
        gc_content = []
        for i in range(0, len(sequence) - window_size + 1, step_size):  # fixed range
            window = sequence[i:i + window_size]
            gc_percent = (window.count('G') + window.count('C')) / window_size * 100
            gc_content.append((f"{i}-{i + window_size}", gc_percent))  # keep as float
        return gc_content

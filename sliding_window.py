from Bio import SeqIO

def sliding_gc_content(sequence_path: str, window_size: int, step_size: int) -> list:
    for record in SeqIO.parse(sequence_path, "fasta"):
        sequence = str(record.seq)
        gc_content = []
        for i in range(0, len(sequence) - window_size + 1, step_size):  # fixed range
            window = sequence[i:i + window_size]
            gc_percent = (window.count("G") + window.count("C") + window.count ("g") + window.count("c")) / window_size * 100
            temp_list_elem = [[i+1,i + window_size], gc_percent]
            gc_content.append(temp_list_elem)
        return gc_content

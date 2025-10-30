from Bio import SeqIO

def sliding_gc_content(seq_path: str, window_size: int, step_size: int) -> list:
    for record in SeqIO.parse(seq_path, "fasta"):
        sequence = str(record.seq)
        gc_content = []
        for i in range(0, len(sequence), step_size):
            current_window_size = min(window_size, len(sequence) - i)
            window = sequence[i:i + current_window_size]
            gc_percent = (window.count("G") + window.count("C") + window.count ("g") + window.count("c")) / window_size * 100
            temp_list_elem = [[i+1,i + window_size], gc_percent]
            gc_content.append(temp_list_elem)
        return gc_content

def cpg_islands(seq_path: str, step_size: int = 2, window_size: int = 100) -> list:
    for record in SeqIO.parse(seq_path, "fasta"):
        sequence = str(record.seq)
        cpg = []
        for i in range(0, len(sequence), step_size):
            current_window_size = min(window_size, len(sequence) - i)
            window = sequence[i:i + current_window_size]
            cpg_count_per_100 = ((window.count("CG") + window.count("cg")) / window_size * 100)
            temp_list_elem = [[i+1,i + window_size], int(cpg_count_per_100)]
            cpg.append(temp_list_elem)
        return cpg
    
def gpc_islands(seq_path: str, step_size: int = 2, window_size: int = 100) -> list:
    for record in SeqIO.parse(seq_path, "fasta"):
        sequence = str(record.seq)
        gpc = []
        for i in range(0, len(sequence), step_size):
            current_window_size = min(window_size, len(sequence) - i)
            window = sequence[i:i + current_window_size]   
            gpc_count_per_100 = ((window.count("GC") + window.count("gc")) / current_window_size * 100)
            temp_list_elem = [[i+1, i + current_window_size], int(gpc_count_per_100)]
            gpc.append(temp_list_elem)
        return gpc
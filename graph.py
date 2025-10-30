import matplotlib.pyplot as plt

def create_x_values(gc_list: list) -> list:
    x = []
    for elem in gc_list:
        x.append(elem[0][0])
    return x

def create_y_values(gc_list: list) -> list:
    y = []
    for elem in gc_list:
        y.append(elem[1])
    return y

def gc_content_graph(x: list, y: list) -> tuple:
    fig, ax = plt.subplots()
    
    norm = plt.Normalize(vmin=0, vmax=100)
    colors = plt.cm.inferno(norm(y))
    
    for i in range(len(x) - 1):
        ax.fill_between(x[i:i+2], 0, y[i:i+2], color=colors[i])
    
    ax.set_xlabel("Nucleotide Position")
    ax.set_ylabel("GC Content (%)")
    ax.set_title("GC Content Across Sequence")
    ax.set(xlim=(min(x), max(x)), ylim=(0, 100))
    
    sm = plt.cm.ScalarMappable(cmap="inferno", norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label="GC Content (%)")
    
    ax.grid(alpha=0.4)
    plt.show()
    return fig, ax

def cpg_islands_graph(cpg_counts: list, gpc_counts: list) -> tuple:
    fig, ax = plt.subplots()

    x_cpg = [elem[0][0] for elem in cpg_counts]
    y_cpg = [elem[1] for elem in cpg_counts]

    x_gpc = [elem[0][0] for elem in gpc_counts]
    y_gpc = [elem[1] for elem in gpc_counts]
    
    ax.plot(x_cpg, y_cpg, color="darkblue", label='CpG')
    ax.plot(x_gpc, y_gpc, color="orange", label='GpC')

    ax.set_xlabel("Nucleotide Position", fontsize=12, fontweight='bold')
    ax.set_ylabel("Count per 100 nt", fontsize=12, fontweight='bold')
    ax.set_title("CpG and GpC Counts Across Sequence", fontsize=14, fontweight='bold', pad=20)
    
    ax.set(xlim=(min(x_cpg), max(x_cpg)), ylim=(0, max(y_cpg) + 5))
    ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
    
    ax.grid(alpha=0.4)
    plt.show()
    return fig, ax
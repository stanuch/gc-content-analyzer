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
    
    ax.grid()
    plt.show()
    return fig, ax
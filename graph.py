import matplotlib as mp
import matplotlib.pyplot as plt

def create_x_values(gc_list):
    x = []
    for elem in gc_list:
        x.append(elem[0][0])
    return x

def create_y_values(gc_list):
    y = []
    for elem in gc_list:
        y.append(elem[1])
    return y

def gc_content_graph(x: list, y: list):
    fig, ax = plt.subplots()

    ax.stackplot(x,y)
    ax.set_xlabel('Nucleotide Position')
    ax.set_ylabel('GC Content (%)')
    ax.set_title('GC Content Across Sequence')

    ax.set(xlim=(min(x), max(x)), ylim=(0, 100))
    
    ax.grid()
    plt.show()
    return fig, ax
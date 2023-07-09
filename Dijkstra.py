import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


def insert(heap, edge):
    #fuegt eine Kante zu dem Heap hinzu und stellt die Heapbedingungen sicher
    heap.append(edge)
    heapify_up(heap, len(heap) - 1)


def extract_min(heap):
    # Wenn der Heap leer ist dann wird None ausgegeben
    if len(heap) == 0:
        return None

    min_edge = heap[0]  #Das kleinste Element des Heaps
    last_edge = heap.pop()

    #Um die Heapbedingungen sicherzustellen
    if len(heap) > 0:
        heap[0] = last_edge
        heapify_down(heap, 0)

    return min_edge     #Gibt das kleinste Element zurueck


def heapify_up(heap, index):
    parent_index = (index - 1) // 2     #Der Elternindex wird berechnet

    #Jetzt werden das Elternelement mit dem Kindelement verglichen bis das Elternelement kleiner ist als das Kindelement
    while index > 0 and heap[index]["costs"] < heap[parent_index]["costs"]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index    #Falls groesser als das Kindelement wird die Indexen getauscht und den Elternindex nochmal berechnet
        parent_index = (index - 1) // 2


def heapify_down(heap, index):
    #Die linke und rechte Kindindexe werden berechnet
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    smallest_index = index

    #Der linke Kindknote wird verglichen nd ggf getauscht
    if left_child_index < len(heap) and heap[left_child_index]["costs"] < heap[smallest_index]["costs"]:
        smallest_index = left_child_index

    # Der rechte Kindknote wird verglichen nd ggf getauscht
    elif right_child_index < len(heap) and heap[right_child_index]["costs"] < heap[smallest_index]["costs"]:
        smallest_index = right_child_index

    if smallest_index != index:
        heap[index], heap[smallest_index] = heap[smallest_index], heap[index]
        heapify_down(heap, smallest_index)


def plot_heap(heap):
    G = nx.Graph()
    for i, node in enumerate(heap):
        G.add_node(i, label="(" + node["source"] + "->" + node["target"] + "," + str(node["costs"]) + ")")
        if i > 0:
            parent = (i - 1) // 2
            G.add_edge(parent, i)

    pos = graphviz_layout(G, prog="dot")

    labels = {node: data["label"] for node, data in G.nodes(data=True)}
    node_colors = ["red" if node == 0 else "lightblue" for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors,
            node_size=1500, font_size=8, font_color="black")
    plt.show()


heap = []
insert(heap, {"source": "A", "target": "B", "costs": 5})
insert(heap, {"source": "B", "target": "C", "costs": 3})
insert(heap, {"source": "C", "target": "D", "costs": 7})
insert(heap, {"source": "D", "target": "E", "costs": 2})
insert(heap, {"source": "E", "target": "F", "costs": 4})
insert(heap, {"source": "F", "target": "G", "costs": 6})
insert(heap, {"source": "G", "target": "H", "costs": 1})
insert(heap, {"source": "X", "target": "Z", "costs": 12})
insert(heap, {"source": "M", "target": "Y", "costs": 16})
insert(heap, {"source": "M", "target": "Y", "costs": 14})
insert(heap, {"source": "M", "target": "A", "costs": 0})
insert(heap, {"source": "M", "target": "Y", "costs": 1})

print(extract_min(heap))
plot_heap(heap)

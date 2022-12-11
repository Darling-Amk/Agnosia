Len = 4
Size = 5

def delVertex(G,d):
    G_ = {
        "In": set(),
        "Out": set()
    }
    for v in G:
        if v!=d:
            G_[v] = set()

    for u in G_:
        for v in G[u]:
            if v==d or u==d:
                continue
            G_[v].add(u)

    return G_


def CreateGraph():
    G = {
        "In":set(),
        "Out":set()
    }
    for i in range(1,1+Len*Size):
        G[i] = set()


    for i in range(Len+1):
        for j in range(1,Size+1):
            if i == 0:
                G["In"].add(i*Len+j)
                continue
            elif i == Len:
                G[(i-1) * Size + j].add("Out")
                continue
            else:
                for k in range(1, Size + 1):
                    G[(i-1)*Size+j].add(i*Size+k)

    G = delVertex(G, 10)
    G = delVertex(G, 9)
    G = delVertex(G, 8)

    G = delVertex(G, 18)
    G = delVertex(G, 19)
    G = delVertex(G, 20)

    return G


if __name__=='__main__':
    g = CreateGraph()
    print(g)
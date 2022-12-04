

G = {
    "In":set(),
    "Out":set()
}


Len = 3
Size = 3

for i in range(1,1+Len*Size):
    G[i] = set()


for i in range(Len+1):
    for j in range(1,Size+1):
        if i == 0:
            G["In"].add(i*Len+j)
            continue
        elif i == Len:
            G[(i-1) * Len + j].add("Out")
            continue
        else:
            for k in range(1, Size + 1):
                G[(i-1)*Len+j].add(i*Len+k)

print(G)
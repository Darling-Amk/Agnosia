import random
from Classes import Monster
from Classes import Treasure
from Classes import Camp
from Classes import RandomEvent
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
            G_[u].add(v)

    return G_


def generateGraph():
    G = {
        "In":set(),
        "Out":set()
    }
    for i in range(1,1+Len*Size):
        G[i] = set()
    toDel = set()
    lstmsk = 1
    lstnum = 1
    for i in range(1, Len + 1):
        was = [0] * 10
        num = random.randrange(1, Size)        
        for vertex in range(num + 1, Size + 1):            
            toDel.add((i - 1) * Size + vertex)        

        if(i == 1):              
            for edge in range(1, num + 1):                
                G["In"].add((i - 1) * Size + edge)
            lstmsk = (1 << num) - 1
            lstnum = num
            continue

        for j in range(1, lstnum + 1):                        
            msk = random.randrange(1, (1 << num))
            print((i - 2) * Size + j, " ", msk)
            for edge in range(0, num):
                if((msk & (1 << edge)) != 0):                    
                    G[(i - 2) * Size + j].add((i - 1) * Size + edge + 1)
                    was[edge + 1] = 1
        for j in range(1, num + 1):
            if(was[j] == 0):
                v = random.randrange(1, lstnum + 1)
                G[(i - 2) * Size + v].add((i - 1) * Size + j)        
        lstnum = num

    for j in range(1, lstnum + 1):        
        G[(Len - 1) * Size + j].add("Out")  
        
    for i in toDel:
        G = delVertex(G, i)

    print(G)
    return G

def generateEvents(G):
    events = {}
    events["In"] = Monster()
    events["Out"] = Monster()
    for i in G:
        if(i == "In" or i == "Out"): continue
        print(i, " ", (i - 1) / Size)
        if(((i - 1) // Size) % 2 != 0): events[i] = Monster()
        else:
            rnd = random.randrange(0, 3)
            if(rnd == 0):
                events[i] = Camp()
            elif(rnd == 1):
                events[i] = Treasure()
            else: events[i] = RandomEvent()
    print(events)
    return events

if __name__=='__main__':
    g = generateGraph()
    print(g)
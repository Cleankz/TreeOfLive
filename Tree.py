def TreeOfLife(H, W, N, tree):
    tree_result = []
    result = []
    for i in range(H):
        a = []
        for j in tree[i]:
            if j ==".":
                a.append(0)
            elif j =="+":
                a.append(1)
        tree_result.append(a)
     
    for time in range(N):
        if time % 2 == 0:
            for x in range(H):
                tree_result[x][:]=[i+1 for i in tree_result[x]]
        else:
            for y in range(H):
                tree_result[y][:]=[i+1 for i in tree_result[y]]
            for z in range(H):
                for v in range(W):
                    if z == 0 and tree_result[z][v] >= 3 and v == 0:
                        tree_result[z][v] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z+1][v] < 3:
                            tree_result[z+1][v] = 0
                    elif z == 0 and tree_result[z][v] >= 3 and v == W -1:
                        tree_result[z][v] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z+1][v] < 3:
                            tree_result[z+1][v] = 0
                    elif z == 0 and tree_result[z][v] >= 3:
                        tree_result[z][v] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z + 1][v] < 3:
                            tree_result[z + 1][v] = 0
                    elif z == H - 1 and tree_result[z][v] >= 3 and v == 0:
                        tree_result[z][v] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                    elif z == H - 1 and tree_result[z][v] >= 3 and v == W -1:
                        tree_result[z][v] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                    elif z == H - 1 and tree_result[z][v] >= 3:
                        tree_result[z][v] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                    elif tree_result[z][v] >= 3 and v == W - 1:
                        tree_result[z][v] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                        if tree_result[z + 1][v] < 3:
                            tree_result[z + 1][v] = 0
                    elif tree_result[z][v] >= 3 and v == 0:
                        tree_result[z][v] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                        if tree_result[z + 1][v] < 3:
                            tree_result[z + 1][v] = 0
                    elif tree_result[z][v] >= 3:
                        tree_result[z][v] = 0
                        if tree_result[z][v + 1] < 3:
                            tree_result[z][v + 1] = 0
                        if tree_result[z][v - 1] < 3:
                            tree_result[z][v - 1] = 0
                        if tree_result[z-1][v] < 3:
                            tree_result[z-1][v] = 0
                        if tree_result[z + 1][v] < 3:
                            tree_result[z + 1][v] = 0
                        
                    else:
                        continue
    for i in range(H):
        string = ''
        for j in range(W):
            if tree_result[i][j] > 0:
                string += "+"
            else:
                string += "."
        result.append(string)
    return result
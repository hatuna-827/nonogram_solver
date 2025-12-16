def main():
    # get size
    height, width = map(int, input().split())
    # create grid
    grid = []
    for h in range(height):
        grid.append([])
        for w in range(width):
            grid[h].append("?")
    # create H & H_sum
    H = []
    H_sum = 0
    for h in range(height):
        H.append(list(map(int, input().split())))
        H_sum += sum(H[h])
    # create W & W_sum
    W = []
    W_sum = 0
    for w in range(width):
        W.append(list(map(int, input().split())))
        W_sum += sum(W[w])
    # sum check
    if H_sum != W_sum:
        print("No solution")
        print("Height Sum", H_sum)
        print("Width Sum", W_sum)
        exit()
    # create Hb_sum & Wb_sum
    Hb_sum = []
    for h in range(len(H)):
        Hb_sum.append([0])
        for i in H[h]:
            Hb_sum[-1].append(Hb_sum[-1][-1] + i)
    Wb_sum = []
    for w in range(len(W)):
        Wb_sum.append([0])
        for i in W[w]:
            Wb_sum[-1].append(Wb_sum[-1][-1] + i)
    # create Hw & Ww
    H_list = []
    for h in range(height):
        H_list.append(genlist(H[h], width))
    W_list = []
    for w in range(width):
        W_list.append(genlist(W[w], height))
    # with logic
    while True:
        before = grid[:]
        with_logic(grid, height, width, H_list)
        grid = [list(x) for x in zip(*grid)]
        with_logic(grid, width, height, W_list)
        grid = [list(x) for x in zip(*grid)]
        if before == grid:
            break
    print("=" * (width * 2 - 1))
    print_out(grid)
    print("=" * (width * 2 - 1))
    print("height", height, "width", width)
    for h in range(height):
        for w in range(width):
            if grid[h][w] == "?":
                break
        else:
            continue
        break
    else:
        exit()
    # without logic
    # without_logic(grid,height,width,H,W)


# def without_logic(grid,height,width,H,W):
#   stack=[grid]
#   while len(stack)!=0:
#     grid=stack.pop()
#     for h in range(height):
#       nothing=True
#       for i in grid[h]:
#         if i=="?":
#           nothing=False
#           break
#       if nothing:
#         continue


def with_logic(grid, height, width, H):
    for h in range(height):
        nothing = True
        for i in grid[h]:
            if i == "?":
                nothing = False
                break
        if nothing:
            continue
        lines = H[h]
        for i in range(len(lines)):
            for w in range(width):
                if grid[h][w] != "?" and lines[i][w] != grid[h][w]:
                    lines[i] = "@"
                    break
        lines = [i for i in lines if i != "@"]
        H[h] = lines
        grid[h] = dup(lines)
    return grid


def dup(o):
    result = list(o[0])
    width = len(result)
    for O in o[1:]:
        for w in range(width):
            if result[w] != "?" and result[w] != O[w]:
                result[w] = "?"
    return result


def genlist(d, width):
    if (d[0]==0):
        return ["."*width]
    r = width - sum(d) - len(d) + 2
    m = [r - 2]
    for i in d:
        m.append(m[-1] + i + 1)
    m.pop(0)
    result = []
    for w in range(width):
        result.append([])
    for s in range(r):
        result[s + d[0] - 1].append("." * s + "#" * d[0])
    for i in range(1, len(d)):
        old = result[:]
        result = []
        for w in range(width):
            result.append([])
        for s in range(1, r + 1):
            l = s + d[i]
            c = "." * s + "#" * d[i]
            for o in range(m[i] - l):
                for v in old[o]:
                    result[o + l].append(v + c)
    for i in range(len(result) - 1):
        for v in result[i]:
            result[-1].append(v + "." * (width - i - 1))
    return result[-1]


def print_out(grid):
    for line in grid:
        print(" ".join(line))
    return


if __name__ == "__main__":
    main()

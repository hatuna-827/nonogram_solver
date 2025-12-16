# def fill_line(grid, Hb_sum, Hw, h):
#     for i in range(1, len(Hw) - 1):
#         Hw[i] += 1
#     fill(grid, h, 0, h, Hw[0], ".")
#     Hw_sum = [0]
#     for i in range(len(Hw)):
#         Hw_sum.append(Hw_sum[-1] + Hw[i])
#     for i in range(1, len(Hw)):
#         fill(grid, h, Hw_sum[i] + Hb_sum[i - 1], h, Hw_sum[i] + Hb_sum[i], "#")
#         fill(grid, h, Hw_sum[i] + Hb_sum[i], h, Hw_sum[i + 1] + Hb_sum[i], ".")
#     for i in range(1, len(Hw) - 1):
#         Hw[i] -= 1
#     return grid


# def fill(grid, start_h, start_w, end_h, end_w, content):
#     if start_w == -1:
#         start_w = 0
#     for h in range(start_h, end_h + 1):
#         for w in range(start_w, end_w):
#             grid[h][w] = content
#     return grid


# def print_out(grid):
#     for line in grid:
#         print(" ".join(line))
#     return


# d = [1, 1, 1]
# width = 8

# b_sum = [0]
# for i in d:
#     b_sum.append(b_sum[-1] + i)

# result = []
# list = [0] * (len(d) + 1)
# list[-1] = width - sum(d) - len(d) + 1
# result.append(list[:])
# while list[0] != width - sum(d) - len(d) + 1:
#     i = -1
#     while list[i] == 0:
#         i -= 1
#     list[i - 1] += 1
#     list[-1] = list[i] - 1
#     if i != -1:
#         list[i] = 0
#     result.append(list[:])

# print(result)
# for i in range(len(result)):
#     result[i] = fill_line([["?"] * width], b_sum, result[i], 0)[0]
# print_out(result)

# -------------------------------------------------------------------------------------------------------

# d = [2, 1, 1]
# width = 8

# min = [0]
# for i in d[:-1]:
#     min.append(min[-1] + i + 1)

# result=[]
# print(min)

# print([""]*width)
# print([""]*(width-min[-1]))

# -------------------------------------------------------------------------------------------------------


def print_out(g):
    for value in g:
        for v in value:
            print(v)


# hoge = [
#     "..##.#.#",
#     ".##..#.#",
#     "##...#.#",
#     ".##.#..#",
#     "##..#..#",
#     "##.#...#",
#     ".##.#.#.",
#     "##..#.#.",
#     "##.#..#.",
#     "##.#.#..",
# ]
# hoge.reverse()
# for i in hoge:
#     print(i)

d = [1, 1,1]
width = 8

r = width - sum(d) - len(d) + 2
m = [r-2]
for i in d:
    m.append(m[-1] + i + 1)
m.pop(0)
print(m)

result = []
for w in range(width):
    result.append([])
for s in range( r):
    result[s + d[0] - 1].append("." * s + "#" * d[0])

print(result)
# exit()

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
result = result[-1]
print(result)
# exit()

# for i in d
# for r in range(min,max)
# for i in range(sum(d) - len(d) + 2):
#     result.append("." * i + "#" * d[0])

for v in result:
    print(v)

# print(result)

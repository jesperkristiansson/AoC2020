'''
Created on 3 Jan 2022

@author: Jesper Kristiansson
'''
from functools import reduce

def treesForSlope(lines, dx, dy):
    x = 0
    trees = 0
    for y in range(0, len(lines), dy):
        if lines[y][x] == '#':
            trees += 1
        x = (x + dx) % len(lines[y])
    return trees


if __name__ == '__main__':
    inp = open("input.in").read().split("\n")
    slopeTrees = []
    slopeTrees.append(treesForSlope(inp, 1, 1))
    slopeTrees.append(treesForSlope(inp, 3, 1))
    slopeTrees.append(treesForSlope(inp, 5, 1))
    slopeTrees.append(treesForSlope(inp, 7, 1))
    slopeTrees.append(treesForSlope(inp, 1, 2))
    print("Part 1:", str(slopeTrees[1]))
    print("Part 2:", str(reduce(lambda a, b : a*b, slopeTrees)))
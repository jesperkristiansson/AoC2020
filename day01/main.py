'''
Created on 2 Jan 2022

@author: Jesper Kristiansson
'''


def part1(numbers):
    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                return i * j


def part2(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i * j * k


if __name__ == '__main__':
    file = open("input.in")
    inp = file.read().split()
    inputNumbers = list(map(lambda s: int(s), inp))
    print("Part 1:", str(part1(inputNumbers)))
    print("Part 2:", str(part2(inputNumbers)))

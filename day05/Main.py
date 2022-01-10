'''
Created on 10 Jan 2022

@author: Jesper Kristiansson
'''


def main():
    inp = open("input.in").read().split()
    seatIDs = list()
    for line in inp:
        row = ''
        col = ''
        for char in line:
            if char == 'B':
                row += '1'
            elif char == 'F':
                row += '0'
            elif char == 'R':
                col += '1'
            elif char == 'L':
                col += '0'
            else:
                raise Exception("invalid input")
        row = int(row, 2)
        col = int(col, 2)
        seatIDs.append(row * 8 + col)
    seatIDs.sort(reverse=True)
    highestID = seatIDs[0]
    print("Part 1:", highestID)
    for seatID in range(highestID):
        if seatID not in seatIDs and seatID - 1 in seatIDs and seatID + 1 in seatIDs:
            print("Part 2:", seatID)


if __name__ == '__main__':
    main()

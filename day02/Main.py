'''
Created on 3 Jan 2022

@author: Jesper Kristiansson
'''

if __name__ == '__main__':
    file = open("input.in")
    inp = file.read().split("\n")
    valid1, valid2 = 0, 0
    for line in inp:
        split = line.split()
        policy = split[0].split("-")
        firstNum = int(policy[0])
        secondNum = int(policy[1])
        letter = split[1][0]
        password = split[2]
        count = password.count(letter)
        if firstNum <= count <= secondNum:
            valid1 += 1
        if (password[firstNum-1] == letter) ^ (password[secondNum-1] == letter):
            valid2 += 1
    print("part 1:", str(valid1))
    print("part 2:", str(valid2))

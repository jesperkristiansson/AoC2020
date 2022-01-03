'''
Created on 2 Jan 2022

@author: Jesper Kristiansson
'''

if __name__ == '__main__':
    file = open("input.in")
    inp = file.read().split()
    inputNumbers = list(map(lambda s : int(s), inp))
    for i in inputNumbers:
        for j in inputNumbers:
            for k in inputNumbers:
                if i + j + k== 2020:
                    print(i*j*k)
                    exit()
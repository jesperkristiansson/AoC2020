'''
Created on 3 Jan 2022

@author: Jesper Kristiansson
'''
import re

eyeColors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validateFields(fields):
    validByr = 1920 <= int(fields["byr"]) <= 2002
    validIyr = 2010 <= int(fields["iyr"]) <= 2020
    validEyr = 2020 <= int(fields["eyr"]) <= 2030
    hgt = fields["hgt"]
    if hgt[-2:] == "cm":
        validHgt = 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == "in":
        validHgt = 59 <= int(hgt[:-2]) <= 76
    else:
        validHgt = False
    hcl = fields["hcl"]
    if hcl[0] == "#" and len(hcl) == 7:
        validHcl = re.match("^[a-f0-9]*", hcl[1:])
    else:
        validHcl = False
    validEcl = fields["ecl"] in eyeColors
    pid = fields["pid"]
    if len(pid) == 9:
        validPid = re.match("^[0-9]*", pid)
    else:
        validPid = False
    return validByr and validIyr and validEyr and validHgt and validHcl and validEcl and validPid


if __name__ == '__main__':
    inp = open("input.in").read().split("\n\n")
    valids1, valids2 = 0, 0
    for line in inp:
        fields = {}
        for field in line.split():
            f = field.split(":")
            fields[f[0]] = f[1]
        requiredLength = 7
        if "cid" in fields:
            requiredLength += 1
        if len(fields) >= requiredLength:
            valids1 += 1
            if validateFields(fields):
                valids2 += 1
    print("Part 1:", valids1)
    print("Part 2:", valids2)

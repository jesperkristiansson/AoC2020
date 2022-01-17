'''
Created on 17 Jan 2022

@author: Jesper Kristiansson
'''

if __name__ == '__main__':
    inp = open("input.in").read()
    groups = inp.split("\n\n")
    any_answered_yes = 0
    all_answered_yes = 0
    for group in groups:
        answers = dict()
        people = group.split("\n")
        for person in people:
            for answer in person:
                answers[answer] = answers.get(answer, 0) + 1
        any_answered_yes += len(answers)
        for k, v in answers.items():
            if v == len(people):
                all_answered_yes += 1
    print("Part 1:", any_answered_yes)
    print("Part 2:", all_answered_yes)
'''
Created on 17 Jan 2022

@author: Jesper Kristiansson
'''

gold = "shiny gold"

class Bag:
    def __init__(self):
        self.subbags = dict()
        
def leads_to_gold(bags, color):
    for next_color in bags[color].subbags:
        if next_color == gold:
            return True
        if leads_to_gold(bags, next_color):
            return True
    return False

def bags_in_bag(bags, color):
    number_of_bags = 0
    for next_color, number in bags[color].subbags.items():
        number_of_bags += number*bags_in_bag(bags, next_color) + number
    return number_of_bags

def make_dictionary_of_bags(rules):
    bags = dict()
    for rule in rules:
        bag = Bag()
        split = rule.split(" contain ")
        splitsplit = split[0].split(" ")
        color = f'{splitsplit[0]} {splitsplit[1]}'
        for subbag in split[1].split(", "):
            subsplit = subbag.split()
            if subsplit[0] != "no":
                number = int(subsplit[0])
                subcolor = f'{subsplit[1]} {subsplit[2]}'
                bag.subbags[subcolor] = number
        bags[color] = bag
    return bags

if __name__ == '__main__':
    rules = open("input.in").read().split("\n")
    bags = make_dictionary_of_bags(rules)
    
    contains_gold = 0
    for color in bags:
        if leads_to_gold(bags, color):
            contains_gold += 1
    print("Part 1:", contains_gold)
    print("Part 2:", bags_in_bag(bags, gold))
    
    
        
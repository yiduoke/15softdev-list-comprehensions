from collections import Counter

def check(password):
    listy = {'uppercase' if character.isupper() else 'lowercase' if character.islower() else 'number' if character.isdigit() else 'idle' for character in password}
    return (len(listy) == 4) or (len(listy) == 3 and 'idle' not in listy)

print(check("meowHA194.."))

# Write a function that uses list comprehension to return a password's strength rating. 
# This function should return a lower integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10) Consider these criteria:
# mixture of upper- and lower-case
# inclusion of numerals
# inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *

def level(password):
    specials = ".?!&#,;:-_*"
    upper = -1
    lower = -1
    number = -1
    special = -1
    listy = ['uppercase' if character.isupper() else 'lowercase' if character.islower() else 'number' if character.isdigit() else 'special' if character in specials else 'idle' for character in password]
    dictionary = Counter(listy) #{'lowercase': 4, 'number': 3, 'uppercase': 2, 'special': 2}

    if check(password): #if the password meets minimum requirements
        score = (dictionary['lowercase'] + dictionary['uppercase'] + dictionary['number'] + dictionary['special'])
        if score > 10:
            return 10
        return score
    return 0

print(level("meowAC194.."))
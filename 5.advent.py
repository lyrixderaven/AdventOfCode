from inputs import FIFTH

strings = FIFTH.strings

def is_nice(string):

    bad_strings = ['ab','cd', 'pq', 'xy']
    for baddie in bad_strings:
        if baddie in string:
            print "{} in {}".format(baddie, string)
            return False

    vowel_counter = 0
    for vowel in 'aeiou':
        if vowel in string:
            vowel_counter += string.count(vowel)
    if vowel_counter < 3:
        print "Not enough vowels in {}".format(string)
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    double_letter = False
    for letter in alphabet:
        if '{}{}'.format(letter,letter) in string:
            double_letter = True
            break

    if not double_letter:
        print "No double letters in {}".format(string)
        return False

    return True

counter = 0
for string in strings:
    if is_nice(string):
        counter += 1

print counter

def is_also_nice(string):
    double_occ = False
    for idx in range(0,len(string)-1):
        if string.count(string[idx:idx+2]) > 1:
            double_occ = True
            break

    if not double_occ:
        return False

    inbetween = False
    for idx in range(0,len(string)-2):
        if string[idx:idx+3][0] == string[idx:idx+3][2]:
            inbetween = True
            break

    if not inbetween:
        return False

    return True



counter = 0
for string in strings:
    if is_also_nice(string):
        counter += 1

print counter
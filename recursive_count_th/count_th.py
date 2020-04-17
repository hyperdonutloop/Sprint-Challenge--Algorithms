'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # th is two letters, so less than two doesn't matter
    if len(word) < 2:
        return 0
    # check the word two letters at a time
    # 0:2 - 0 starts at the left of the word, then moves over. 2 is between letter 2 and 3. 
    elif word[0:2] == 'th':
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

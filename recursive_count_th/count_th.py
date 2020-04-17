'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th_helper(word, occurrences=None):
    if len(word) <= 1:
        return occurrences
    elif word[0:2:1] == "th"[0:2:1]:
        return count_th_helper(word[1::1], occurrences + 1)
    else:
        return count_th_helper(word[1::1], occurrences)


def count_th(word):
    if len(word) <= 1:
        return 0
    else:
        occurrences = 0
        return count_th_helper(word, occurrences)

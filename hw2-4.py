ls = input().title().split()
for e, word in enumerate(ls, 1):
    if len(word) > 10:
        print(e, word[0:9])
    else:
        print(e, word)

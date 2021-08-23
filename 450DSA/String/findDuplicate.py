def countDuplicate(string):
    words = {}
    for char in string:
        if char not in words:
            words[char] = 1

        else:
            words[char] += 1

    for char in words:
        print(f'{char} : {words[char]}')



countDuplicate('hello Worldw')
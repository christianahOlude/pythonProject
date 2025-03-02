def number_of_characters(word):
    list = []
    for char in word:
        list.append(char)
    return list


def two_seperated_words(word1, word2):
    output = ''
    for char in word1:
        output += char
    for char in word2:
        output += char
    return output.slice(0,9,1)


def returns_ce(words,ce):
    expect = ''
    for char in words:
        char += ce
        expect += char
    return expect





# def upper_case(word):
#     list = []
#     for char in word:
#         list.append(char.upper())

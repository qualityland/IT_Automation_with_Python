def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_letters("aaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")
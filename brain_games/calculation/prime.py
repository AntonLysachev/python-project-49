import random


def prime():
    numb = random.randint(1, 100)
    temp = numb - 1

    def simple_or_not(tem, num):
        if tem > 1:
            if not (num % tem):
                res = 'no'
            else:
                return simple_or_not(tem - 1, num)
        else:
            res = 'yes'
        return res

    result = simple_or_not(temp, numb)
    meaning = numb
    data = (meaning, str(result))
    return data

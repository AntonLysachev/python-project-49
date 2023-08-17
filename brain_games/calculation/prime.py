import random


def game():
    number = random.randint(1, 100)
    def simple_or_not(numb):
        temp = numb -1
        if numb == 1:
           return False 
        while(temp > 1):
            if not (numb % temp) or numb == 1:
             return False
            temp -= 1
        return True
    result = simple_or_not(number) and 'yes' or 'no'
    meaning = number
    data = (meaning, str(result))
    return data

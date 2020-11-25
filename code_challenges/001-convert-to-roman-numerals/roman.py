# Purpose of the this coding challenge is to write a program that converts the given number to the Roman numerals.

roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def IntToRoman (xn):
    x = xn
    y = 0
    Str = ""
    for i, r in roman_map:
         #　take the number and divisible by the roman number from 1000 to 1.
        y = x//i    

        for j in range(0, y):
            # If after divisibility is not 0 then take the roman number from list into String.
            Str = Str+r 

        # Take the remainder to next round.
        x = x%i 
    print(Str)
    return Str

print(IntToRoman(4568))
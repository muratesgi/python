
conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]

while True:
    num= input(''' ###This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively :''')
    if num == "exit":
        break
    elif num.isdigit() != True:
        print("enter the integer")
    elif int(num) > 3999:
        print("enter the bettween 1 and 3999")
    else:
        num = int(num)


#num = 4
    roman = ''
    i = 0 #initiate i = 0
    while num > 0:
        while conv[i][0] > num:
            i+=1 #increments i to largest value greater than current num
        roman += conv[i][1] #adds the roman numeral equivalent to string
        num -= conv[i][0] #decrements your num
    print(roman)
    break


    
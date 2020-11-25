string = (input("Please entry a string\n").lower())
list1 = ("a", "e", "u", "ı", "o")
i = 0
if len(string) == 1:
    print("Negative")
while i < (len(string)-1):
    for x in string[i]:
        for y in string[i+1]:
            if ((x in list1) and (y in list1)) is True:
                print("Positive")
            else:
                print("Negative")
            i+=1
    
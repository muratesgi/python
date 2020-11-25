# def bracket(data):
#     A={'(':')', '[':']', '{':'}'}
#     for i in range(int(len(data)/2)):
#         if data[0] in A.keys():
#             if A[data[0]] == data[-1]:
#                 data = data[1:-1]
#             else:
#                 return False
#                 break
#         if len(data) == 0:
#             return True

# print(bracket("()[]{}"))


def checkform(text):
    pairs = {')':'(', ']':'[','}':'{'}
    que = []
    for i in text:
        if i in pairs.values():
            que.append(i)
        elif i in pairs.keys():
            if que[-1] == pairs[i]:
                que.pop(-1)
            else:
                return False #parantez açılmadan kapanmış
        else:
            return False #geçersiz karakter
    if que:
        return False
    else: return True     
    #return False if que else True #que de eleman varsa False

print(checkform("{()}"))

###################################
def find_brackets(string):
    cont = True
    while cont == True:
        cont = False
        for i in ["()","{}","[]"]:
            if i in string:
                cont = True
                string = string.replace(i,"")
    return len(string) == 0
print(find_brackets("{()()}"))



'''
Script to convert number into words
'''
def main3(num):
    def one(a):
        word = ''
        if a == '0':
            word = ""
        if a == '1':
            word = "One"
        if a == '2':
            word = "Two"
        if a == '3':
            word = "Three"
        if a == '4':
            word = "Four"
        if a == '5':
            word = "Five"
        if a == '6':
            word = "Six"
        if a == '7':
            word = "Seven"
        if a == '8':
            word = "Eight"
        if a == '9':
            word = "Nine"
        if a == '10':
            word = "Ten"
        if a == '11':
            word = "Eleven"
        if a == '12':
            word = "Twelve"
        if a == '13':
            word = "Thirteen"
        if a == '14':
            word = "Fourteen"
        if a == '15':
            word = "Fifteen"
        if a == '16':
            word = "Sixteen"
        if a == '17':
            word = "Seventeen"
        if a == '18':
            word = "Eighteen"
        if a == '19':
            word = "Nineteen"

        return word

    def twenty(a):
        word = ''
        if a == '2':
            word = "twenty"
        if a == '3':
            word = "Thirty"
        if a == '4':
            word = "Fourty"
        if a == '5':
            word = "Fifty"
        if a == '6':
            word = "Sixty"
        if a == '7':
            word = "Seventy"
        if a == '8':
            word = "Eighty"
        if a == '9':
            word = "Ninety"
        if a == '0':
            word = ''
        return word

    leng = len(num)
    if (int(num) < 20):
        a = num
        word = one(a)
        out= (word)
        return out
    
    elif (leng == 2 and 20 <= int(num) < 100 ):
        a = num[1]
        word1 = one(a)
        b = num[0]
        word2 = twenty(b)
        out = (str(word2) + str(word1))
        return out
    
    elif (leng == 3 and 100 <= int(num) < 1000):
        mid = (str(num[1])+str(num[2]))
        c = num[0]
        word3 = one(c)
        if (int(mid) < 20):
            word2 = one(mid)
            out = (str(word3)+" hundred and "+ str(word2))
            return out
        else:
            a = num[2]
            b = num[1]
            word1 = one(a)
            word2 = twenty(b)
            if ( int(a) == 0 and int(b) == 0):
                out = (str(word3)+" hundred")
                return out
            else:
                out = (str(word3)+" hundred and "+ str(word2) + str(word1))
                return out

def main6(num):
    def one(a):
        word = ''
        if a == '0':
            word = ""
        if a == '1':
            word = "One"
        if a == '2':
            word = "Two"
        if a == '3':
            word = "Three"
        if a == '4':
            word = "Four"
        if a == '5':
            word = "Five"
        if a == '6':
            word = "Six"
        if a == '7':
            word = "Seven"
        if a == '8':
            word = "Eight"
        if a == '9':
            word = "Nine"
        if a == '10':
            word = "Ten"
        if a == '11':
            word = "Eleven"
        if a == '12':
            word = "Twelve"
        if a == '13':
            word = "Thirteen"
        if a == '14':
            word = "Fourteen"
        if a == '15':
            word = "Fifteen"
        if a == '16':
            word = "Sixteen"
        if a == '17':
            word = "Seventeen"
        if a == '18':
            word = "Eighteen"
        if a == '19':
            word = "Nineteen"

        return word

    def twenty(a):
        word = ''
        if a == '2':
            word = "twenty"
        if a == '3':
            word = "Thirty"
        if a == '4':
            word = "Fourty"
        if a == '5':
            word = "Fifty"
        if a == '6':
            word = "Sixty"
        if a == '7':
            word = "Seventy"
        if a == '8':
            word = "Eighty"
        if a == '9':
            word = "Ninety"
        if a == '0':
            word = ''
        return word

    leng = len(num)
    if (int(num) < 20):
        a = num
        word = one(a)
        out= (word)
        return out
    
    elif (leng == 2 and 20 <= int(num) < 100 ):
        a = num[1]
        word1 = one(a)
        b = num[0]
        word2 = twenty(b)
        out = (str(word2) + str(word1))
        return out
    
    elif (leng == 3 and 100 <= int(num) < 1000):
        mid = (str(num[1])+str(num[2]))
        c = num[0]
        word3 = one(c)
        if (int(mid) < 20):
            word2 = one(mid)
            out = (str(word3)+" lack and "+ str(word2))
            return out
        else:
            a = num[2]
            b = num[1]
            word1 = one(a)
            word2 = twenty(b)
            if ( int(a) == 0 and int(b) == 0):
                out = (str(word3)+" lack")
                return out
            else:
                out = (str(word3)+" lack and "+ str(word2) + str(word1))
                return out

def main9(num):
    def one(a):
        word = ''
        if a == '0':
            word = ""
        if a == '1':
            word = "One"
        if a == '2':
            word = "Two"
        if a == '3':
            word = "Three"
        if a == '4':
            word = "Four"
        if a == '5':
            word = "Five"
        if a == '6':
            word = "Six"
        if a == '7':
            word = "Seven"
        if a == '8':
            word = "Eight"
        if a == '9':
            word = "Nine"
        if a == '10':
            word = "Ten"
        if a == '11':
            word = "Eleven"
        if a == '12':
            word = "Twelve"
        if a == '13':
            word = "Thirteen"
        if a == '14':
            word = "Fourteen"
        if a == '15':
            word = "Fifteen"
        if a == '16':
            word = "Sixteen"
        if a == '17':
            word = "Seventeen"
        if a == '18':
            word = "Eighteen"
        if a == '19':
            word = "Nineteen"

        return word

    def twenty(a):
        word = ''
        if a == '2':
            word = "twenty"
        if a == '3':
            word = "Thirty"
        if a == '4':
            word = "Fourty"
        if a == '5':
            word = "Fifty"
        if a == '6':
            word = "Sixty"
        if a == '7':
            word = "Seventy"
        if a == '8':
            word = "Eighty"
        if a == '9':
            word = "Ninety"
        if a == '0':
            word = ''
        return word

    leng = len(num)
    if (int(num) < 20):
        a = num
        word = one(a)
        out= (word)
        return out
    
    elif (leng == 2 and 20 <= int(num) < 100 ):
        a = num[1]
        word1 = one(a)
        b = num[0]
        word2 = twenty(b)
        out = (str(word2) + str(word1))
        return out
    
    elif (leng == 3 and 100 <= int(num) < 1000):
        mid = (str(num[1])+str(num[2]))
        c = num[0]
        word3 = one(c)
        if (int(mid) < 20):
            word2 = one(mid)
            out = (str(word3)+" crore and "+ str(word2))
            return out
        else:
            a = num[2]
            b = num[1]
            word1 = one(a)
            word2 = twenty(b)
            if ( int(a) == 0 and int(b) == 0):
                out = (str(word3)+" crore")
                return out
            else:
                out = (str(word3)+" crore and "+ str(word2) + str(word1))
                return out

print("................................................................")
print("Script to convert number into words")
print("................................................................")
num = input("enter the number:")
leng = len(num)
print("................................................................")
print("You have entered : " + num)
print("")
print("")
print("................................................................")




if ( int(num) < 1000 and (leng == 1)):
    l3 = (str(num[0]))
    val1 = main3(l3)
    print(str(val1))
    
elif (int(num) < 1000 and leng == 2):
    l3 = (str(num[0])+str(num[1]))
    val1 = main3(l3)
    print(str(val1))
    
elif (int(num) < 1000 and leng == 3):
    l3 = (str(num[0])+str(num[1])+str(num[2]))
    val1 = main3(l3)
    print(str(val1))
        
elif (1000 <= int(num) < 1000000 and leng == 4):

    l3 = (str(num[1])+str(num[2])+str(num[3]))
    l6 = (str(num[0]))
    val1 = main3(l3)
    val2 = main6(l6)
    print(str(val2)+" thousand " + str(val1))
       
elif(1000 <= int(num) < 1000000 and leng == 5):
    l3 = (str(num[2])+str(num[3])+str(num[4]))
    l6 = (str(num[0])+str(num[1]))
    val1 = main3(l3)
    val2 = main6(l6)
    print(str(val2)+" thousand " + str(val1))
          
elif(1000 <= int(num) < 1000000 and leng == 6):
    l3 = (str(num[3])+str(num[4])+str(num[5]))
    l6 = (str(num[0])+str(num[1])+str(num[2]))
    val1 = main3(l3)
    val2 = main6(l6)
    print(str(val2)+" thousand " + str(val1))

elif(1000000 <= int(num) < 1000000000 and leng == 7):
    l3 = (str(num[4])+str(num[5])+str(num[6]))
    l6 = (str(num[1])+str(num[2])+str(num[3]))
    l9 = (str(num[0]))
    val1 = main3(l3)
    val2 = main6(l6)
    val3 = main9(l9)
    print(str(val3)+" million "+str(val2)+" thousand " + str(val1))

elif(1000000 <= int(num) < 1000000000 and leng == 8):
    l3 = (str(num[5])+str(num[6])+str(num[7]))
    l6 = (str(num[2])+str(num[3])+str(num[4]))
    l9 = (str(num[0])+str(num[1]))
    val1 = main3(l3)
    val2 = main6(l6)
    val3 = main9(l9)
    print(str(val3)+" million "+str(val2)+" thousand " + str(val1))
    
elif(1000000 <= int(num) < 1000000000 and leng == 9):
    l3 = (str(num[6])+str(num[7])+str(num[8]))
    l6 = (str(num[3])+str(num[4])+str(num[5]))
    l9 = (str(num[0])+str(num[1])+str(num[2]))
    val1 = main(l3)
    val2 = main(l6)
    val3 = main(l9)
    print(str(val3)+" million "+str(val2)+" thousand " + str(val1))

else:
    print('Number above a billion, please use your brains')


print('')




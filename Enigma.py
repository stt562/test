#imports
import os
import random
import string

#Functions
def rotate(l, n):
    return l[n:] + l[:n]
class plug:
    @staticmethod
    def encrypt(message):
        plug = "YAQXSWCDEVFRBGTNHZMJUKILOP"
        plug = list(plug)
        temp = ""
        for i in str(message):
            if i not in string.ascii_lowercase:
                temp += i
                continue
            temp += i.upper()
        message = str(temp)
        nmessage = ""
        for i in message:
            if i not in string.ascii_uppercase:
                nmessage += i
                continue
            nmessage += plug[string.ascii_uppercase.index(i)]
        return nmessage
    @staticmethod
    def decrypt(message):
        plug = "YAQXSWCDEVFRBGTNHZMJUKILOP"
        plug = list(plug)
        temp = ""
        for i in str(message):
            if i not in string.ascii_lowercase:
                temp += i
                continue
            temp += i.upper()
        message = str(temp)
        nmessage = ""
        for i in message:
            if i not in string.ascii_uppercase:
                nmessage += i
                continue
            nmessage += string.ascii_uppercase[plug.index(i)]
        return nmessage
class rotator:
    @staticmethod
    def encrypt(message):
        save = 0
        save2 = 0
        nmessage = ""
        temp = ""
        for i in str(message):
            if i not in string.ascii_lowercase:
                temp += i
                continue
            temp += i.upper()
        message = str(temp)
        routator1 = "IUXMDRLBEFCOPNYJWQSTAZKVGH"
        routator2 = "OJPBESMYUIRFXWCGKLZNQTDVHA"
        routator3 = "RUPHKTVCYOXSEDIMNJQGFLZWAB"
        routator1 = list(routator1)
        routator2 = list(routator2)
        routator3 = list(routator3)
        for i in message:
            if i not in string.ascii_uppercase:
                nmessage += i
                continue
            index = string.ascii_uppercase.index(i)
            c1 = routator1[index]
            index2 = string.ascii_uppercase.index(c1)
            c2 = routator2[index2]
            index3 = string.ascii_uppercase.index(c2)
            c3 = routator3[index3]
            nmessage += c3
            routator1 = rotate(routator1, 1)
            save += 1
            if save == len(routator1):
                save = 0
                routator2 = rotate(routator2, 1)
                save2 += 1
                if save2 == len(routator2):
                    save2 = 0
                    routator3 = rotate(routator3, 1)
        return nmessage
    @staticmethod
    def reverse(message):
        save = 0
        save2 = 0
        nmessage = ""
        temp = ""
        for i in str(message):
            if i not in string.ascii_lowercase:
                temp += i
                continue
            temp += i.upper()
        message = str(temp)
        routator1 = "IUXMDRLBEFCOPNYJWQSTAZKVGH"
        routator2 = "OJPBESMYUIRFXWCGKLZNQTDVHA"
        routator3 = "RUPHKTVCYOXSEDIMNJQGFLZWAB"
        routator1 = list(routator1)
        routator2 = list(routator2)
        routator3 = list(routator3)
        routator1.reverse()
        routator2.reverse()
        routator3.reverse()
        for i in message:
            if i not in string.ascii_uppercase:
                nmessage += i
                continue
            index = routator3.index(i)
            c1 = string.ascii_uppercase[index]
            index2 = routator2.index(c1)
            c2 = string.ascii_uppercase[index2]
            index3 = routator1.index(c2)
            c3 = string.ascii_uppercase[index3]
            nmessage += c3
            routator3 = rotate(routator3, 1)
            save += 1
            if save == len(routator3):
                save = 0
                routator2 = rotate(routator2, 1)
                save2 += 1
                if save2 == len(routator2):
                    save2 = 0
                    routator3 = rotate(routator1, 1)
        return nmessage
def reflector(message):
    nmessage = ""
    reflector = list("XSHPJKBDNOMZUYIWTVCEGFRLAQ")
    for i in message:
        if i not in string.ascii_lowercase:
            nmessage += i
            continue
        nmessage += reflector[string.ascii_uppercase.index(i)]
    return nmessage
class enigma:
    @staticmethod
    def enigma(message):
        return plug.decrypt(rotator.reverse(reflector(rotator.encrypt(plug.encrypt(message)))))

#Main
os.system('@Title Enigma')
os.system('@echo off')
while True:
    print(enigma.enigma(input('')))
import math
import random

message = input()
def encryption(message):
    mydict = {
        "a": 44,
        "b": 43,
        "c": 42,
        "d": 41,
        "e": 40,
        "f": 39,
        "g": 38,
        "h": 37,
        "i": 36,
        "j": 35,
        "k": 34,
        "l": 33,
        "m": 32,
        "n": 31,
        "o": 30,
        "p": 29,
        "q": 28,
        "r": 27,
        "s": 26,
        "t": 25,
        "u": 24,
        "v": 23,
        "w": 22,
        "x": 21,
        "y": 20,
        "z": 19,
        "0": 18,
        "1": 17,
        "2": 16,
        "3": 15,
        "4": 14,
        "5": 13,
        "6": 12,
        "7": 11,
        "8": 10,
        "A": 45,
        "B": 46,
        "C": 47,
        "D": 48,
        "E": 49,
        "F": 50,
        "G": 51,
        "H": 52,
        "I": 53,
        "J": 54,
        "K": 55,
        "L": 56,
        "M": 57,
        "N": 58,
        "O": 59,
        "P": 60,
        "Q": 61,
        "R": 62,
        "S": 63,
        "T": 64,
        "U": 65,
        "V": 66,
        "W": 67,
        "X": 68,
        "Y": 69,
        "Z": 70,
        "9": 71,
        "_": 72,
        "-": 73,
        "%": 74,
        "!": 75,
        "@": 76,
        "$": 77,
        "^": 78,
        "&": 79,
        "*": 80,
        "(": 81,
        ")": 82,
        "{": 83,
        "}": 84,
        "[": 85,
        "]": 86,
        "=": 87,
        "+": 88,
        ";": 89,
        ":": 90,
        "'": 91,
        "|": 92,
        "<": 93,
        ">": 94,
        ",": 95,
        ".": 96,
        "?": 97,
        "/": 98,
        " ": 99,
            }
    string = ""
    for i in message:
        k = str(mydict[i])
        string += k
    array1 = ["AAA", "AAC", "AAG", "AAT", "ACA", "ACC"]
    array2 = ["ACG", "ACT", "AGA", "AGC", "AGG", "AGT"]
    array3 = ["ATA", "ATC", "ATG", "ATT", "CAA", "CAC"]
    array4 = ["CAG", "CAT", "CCA", "CCC", "CCG", "CCT"]
    array5 = ["CGA", "CGC", "CGG", "CGT", "CTA", "CTC"]
    array6 = ["CTG", "CTT", "GAA", "GAC", "GAG", "GAT"]
    array7 = ["GCA", "GCC", "GCG", "GCT", "GGA", "GGC"]
    array8 = ["GGG", "GGT", "GTA", "GTC", "GTG", "GTT"]
    array9 = ["TAA", "TAC", "TAG", "TAT", "TCA", "TCC"]
    array0 = ["TCG", "TCT", "TGA", "TGC", "TGG", "TGT"]

    a = len(string)
    a = math.pow(10, a)
    a = a - int(string)
    res = ""
    res += str(a)
    res = res[:-2]
    result =""
    for i in res:
        if(i=="0"):
            x0 = random.choice(array0)
            result +=x0
        elif(i=="1"):
            x1 = random.choice(array1)
            result +=x1
        elif(i=="2"):
            x2 = random.choice(array2)
            result +=x2
        elif(i=="3"):
            x3 = random.choice(array3)
            result +=x3
        elif(i=="4"):
            x4 = random.choice(array4)
            result +=x4
        elif(i=="5"):
            x5 = random.choice(array5)
            result +=x5
        elif(i=="6"):
            x6 = random.choice(array6)
            result +=x6
        elif(i=="7"):
            x7 = random.choice(array7)
            result +=x7
        elif(i=="8"):
            x8 = random.choice(array8)
            result +=x8
        elif(i=="9"):
            x9 = random.choice(array9)
            result +=x9
    print(result)
if __name__ == '__main__':
    encryption(message)
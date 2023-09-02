from django.shortcuts import render
from django.http import HttpResponse
import math
import random



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

    
    res = string
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
    return result

def decryption(message):
    lulu = []
    for i in range(0, len(message), 3):
        lulu.append(message[i:i+3])

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


    num =""
    for i in lulu:
        if(i in array0):
            num += "0"
        elif(i in array1):
            num += "1"
        elif(i in array2):
            num += "2"
        elif(i in array3):
            num += "3"
        elif(i in array4):
            num += "4"
        elif(i in array5):
            num += "5"
        elif(i in array6):
            num += "6"
        elif(i in array7):
            num += "7"
        elif(i in array8):
            num += "8"
        elif(i in array9):
            num += "9"

    lulu.clear()
    for i in range(0, len(num), 2):
        lulu.append(num[i:i+2])


    mydict ={
        44: "a",
        43: "b",
        42: "c",
        41: "d",
        40: "e",
        39: "f",
        38: "g",
        37: "h",
        36: "i",
        35: "j",
        34: "k",
        33: "l",
        32: "m",
        31: "n",
        30: "o",
        29: "p",
        28: "q",
        27: "r",
        26: "s",
        25: "t",
        24: "u",
        23: "v",
        22: "w",
        21: "x",
        20: "y",
        19: "z",
        18: "0",
        17: "1",
        16: "2",
        15: "3",
        14: "4",
        13: "5",
        12: "6",
        11: "7",
        10: "8",
        45: "A",
        46: "B",
        47: "C",
        48: "D",
        49: "E",
        50: "F",
        51: "G",
        52: "H",
        53: "I",
        54: "J",
        55: "K",
        56: "L",
        57: "M",
        58: "N",
        59: "O",
        60: "P",
        61: "Q",
        62: "R",
        63: "S",
        64: "T",
        65: "U",
        66: "V",
        67: "W",
        68: "X",
        69: "Y",
        70: "Z",
        71: "9",
        72: "_",
        73: "-",
        74: "%",
        75: "!",
        76: "@",
        77: "$",
        78: "^",
        79: "&",
        80: "*",
        81: "(",
        82: ")",
        83: "{",
        84: "}",
        85: "[",
        86: "]",
        87: "=",
        88: "+",
        89: ";",
        90: ":",
        91: "'",
        92: "|",
        93: "<",
        94: ">",
        95: ",",
        96: ".",
        97: "?",
        98: "/",
        99: " "
    }
    res =""
    for i in lulu:
        res += mydict[int(i)]

    return res



def home(request):
    if(request.method == 'POST'):
        message = request.POST['message']
        if 'enc' in request.POST:
            result=""
            result = encryption(message)
            return render(request,'index.html',{'result': result})
        if 'dec' in request.POST:
            result = decryption(message)
            return render(request,'index.html',{'result': result})
    return render(request, 'index.html')
    
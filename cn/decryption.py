import math
message = input()
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
    a = str(num)
    a= math.pow(10, len(a))
    a = int(a)
    a -= int(num)
    num = str(a)
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

    print(res)
if __name__ == '__main__':
    decryption(message)
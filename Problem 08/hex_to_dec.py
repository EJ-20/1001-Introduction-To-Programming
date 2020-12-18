def hexa(code):
    code = list(code)
    if code[2] == "A":
        code[2] = "10"
    elif code[2] == "B":
        code[2] = "11"
    elif code[2] == "C":
        code[2] = "12"
    elif code[2] == "D":
        code[2] = "13"
    elif code[2] == "E":
        code[2] = "14"
    elif code[2] == "F":
        code[2] = "15"
    return code

def decToHex(code):
    
    if len(code) == 1:
        return int(code[0])
    else:
        return int(code[0]) * 16**(len(code)-1) + decToHex(code[1:])

def main():
    code = "98A"
    print("The decimal equivalent of the hexadecimal number", code, "is",decToHex(hexa(code)))
main()
        

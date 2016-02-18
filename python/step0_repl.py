import sys

def READ(str):
    return str

def EVAL(str):
    return str

def PRINT(str):
    return str

def rep(str):
    readReturn = READ(str)
    evalReturn = EVAL(str)
    printReturn = PRINT(str)
    return printReturn

def main():
    while True:
        try:
            userInput = input("user> ")
        except EOFError:
            print("")
            sys.exit(0)
        repReturn = rep(userInput)
        print(repReturn)

if __name__ == "__main__":
    main()

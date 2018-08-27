# Saurav Chhapawala #
#       2018        #

letters = ["a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]

def main():
    while True:
        menu()
        word = input()
        
        if word.lower() == "q":
            print("Good Bye")
            break
                
        if word.lower() == "d":
            print("What do you want to decode?")
            decoded = decode(input())
            print(decoded)
            print("")
        
        if word.lower() == "c":
            print("What do you want to cypher?")
            secret = cipher(input())
            print(secret)
            print("")

def menu():
    print("What would you like to do?")
    print("Decode (D)")
    print("Cipher (C)")
    print("Change Offset (O)")
    print("Quit (Q)")
    print("")

def cipher(word):
    word = word.lower()
    ans = ""
    for i in range(len(word)):
        if word[i] not in letters:
            ans += " "
            continue
        for j in range(len(letters)):
            if word[i] == letters[j]:
                change = j + 3
                #25 because index starts at 0
                if change > 25:
                    #subtract 26 to account for index starting at 0
                    #Index of 'z' is 25, 25+3=28, 28-26= 2, index 2 of letters is 'b'
                    change -= 26
                ans += letters[change]
    return ans

def decode(word):
    word = word.lower()
    ans = ""
    for i in range(len(word)):
        if word[i] not in letters:
            ans += " "
            continue
        for j in range(len(letters)):
            if word[i] == letters[j]:
                change = j - 3
                #0 because thats the start
                if change < 0:
                    #add 26 if change goes negative to go back to right letter
                    #Index of 'a' is 0, 0-3= -3, -3+26=23, index 23 of letters is 'x'
                    change += 26
                ans += letters[change]
    return ans

main()

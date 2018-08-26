letters = ["a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]

def main():
    while True:
        print("Decode or Cipher? (D/C) enter 'q' to quit")
        word = input()
        
        if word.lower() == "q":
            print("Good Bye")
            break
                
        if word.lower() == "d":
            print("What do you want to decode?")
            dec = input()
            decoded = decode(dec)
            print(decoded)
            print("")
        
        if word.lower() == "c":
            print("What do you want to cypher?")
            secret = input()
            ciphered = cipher(secret)
            print(ciphered)
            print("")
        
def cipher(word):
    word = word.lower()
    ans = ""
    for i in range(len(word)):
        if word[i] == " ":
            ans += " "
            continue
        for a in range(len(letters)):
            if word[i] == letters[a]:
                change = a + 3
                #25 because index starts at 0
                if change > 25:
                    #subtract 26 to account for index starting at 0
                    #Index of 'z' is 25, 25+3=28, 28-26=2, index 2 of letters is 'b'
                    change = change - 26
                ans += letters[change]
    return ans

def decode(word):
    word = word.lower()
    ans = ""
    for i in range(len(word)):
        if word[i] == " ":
            ans += " "
            continue
        for a in range(len(letters)):
            if word[i] == letters[a]:
                change = a - 3
                if change < 0:
                    change = change + 26
                ans += letters[change]
    return ans

main()

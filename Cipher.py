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
        
        if word[i] == l0:
            ans += l0
        if word[i] == l1:
            ans += l25
        if word[i] == l2:
            ans += l26
        if word[i] == l3:
            ans += l1
        if word[i] == l4:
            ans += l2
        if word[i] == l5:
            ans += l3
        if word[i] == l6:
            ans += l4
        if word[i] == l7:
            ans += l5
        if word[i] == l8:
            ans += l6
        if word[i] == l9:
            ans += l7
        if word[i] == l10:
            ans += l8
        if word[i] == l11:
            ans += l9
        if word[i] == l12:
            ans += l10
        if word[i] == l13:
            ans += l11
        if word[i] == l14:
            ans += l12
        if word[i] == l15:
            ans += l13
        if word[i] == l16:
            ans += l14
        if word[i] == l17:
            ans += l15
        if word[i] == l18:
            ans += l16
        if word[i] == l19:
            ans += l17
        if word[i] == l20:
            ans += l18
        if word[i] == l21:
            ans += l19
        if word[i] == l22:
            ans += l20
        if word[i] == l23:
            ans += l21
        if word[i] == l24:
            ans += l22
        if word[i] == l25:
            ans += l23
        if word[i] == l26:
            ans += l24
    return ans

main()

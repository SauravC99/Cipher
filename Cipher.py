l0, l1, l2, l3, l4, l5, l6 = " ", "a", "b", "c", "d", "e", "f"
l7, l8, l9, l10, l11, l12, l13 = "g", "h", "i", "j", "k", "l", "m"
l14, l15, l16, l17, l18, l19, l20 = "n", "o", "p", "q", "r", "s", "t"
l21, l22, l23, l24, l25, l26 = "u", "v", "w", "x", "y", "z"

# To Do:
# add a secret key to cypher many times
# clean up code
# improve UI and UX

def main():
    print("Decode or Cipher? (D/C) Press 'p' to quit")
    word = input()
            
    if word == "D" or word == "d":
        print("What do you want to decode?")
        dec = input()
        decoded = decode(dec)
        print(decoded)
        print("")
    
    if word == "C" or word == "c":
        print("What do you want to cypher?")
        secret = input()
        ciphered = cipher(secret)
        print(ciphered)
        print("")

    main()
        
def cipher(word):
    word = word.lower()
    ans = ""
    for i in range(0, len(word)):
        if word[i] == l0:
            ans += l0
        if word[i] == l1:
            ans += l3
        if word[i] == l2:
            ans += l4
        if word[i] == l3:
            ans += l5
        if word[i] == l4:
            ans += l6
        if word[i] == l5:
            ans += l7
        if word[i] == l6:
            ans += l8
        if word[i] == l7:
            ans += l9
        if word[i] == l8:
            ans += l10
        if word[i] == l9:
            ans += l11
        if word[i] == l10:
            ans += l12
        if word[i] == l11:
            ans += l13
        if word[i] == l12:
            ans += l14
        if word[i] == l13:
            ans += l15
        if word[i] == l14:
            ans += l16
        if word[i] == l15:
            ans += l17
        if word[i] == l16:
            ans += l18
        if word[i] == l17:
            ans += l19
        if word[i] == l18:
            ans += l20
        if word[i] == l19:
            ans += l21
        if word[i] == l20:
            ans += l22
        if word[i] == l21:
            ans += l23
        if word[i] == l22:
            ans += l24
        if word[i] == l23:
            ans += l25
        if word[i] == l24:
            ans += l26
        if word[i] == l25:
            ans += l1
        if word[i] == l26:
            ans += l2
    return ans

def decode(word):
    word = word.lower()
    ans = ""
    for i in range(0, len(word)):
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

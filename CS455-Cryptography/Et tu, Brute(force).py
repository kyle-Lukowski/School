def Main():


    Cipher1 = "TUZBKXEYKIAXK"
    Cipher2 = "TSJLCPYZJCRMZPSRCDMPACYRRYAIQ"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range (0, 26): #loop 26 times through entire alphabet
        result = ""
        for letter in Cipher1:
            shift = (alphabet.find(letter) - i) % 26
            result = result+alphabet[shift]            #index of shift is ciphertext minus key

        print(result+" Key #"+str(i+1))               #NOTVERYSECURE Key = 7 (Ciphertext minus 7)

    for i in range (0, 26):
        result = ""
        for letter in Cipher2:
            shift = (alphabet.find(letter) - i) % 26
            result = result+alphabet[shift]

        print(result+" Key #"+str(i+1))              #VULNERABLETOBRUTEFORCEATTACKS Key = 25 (Ciphertext minus 25)

    

    

Main()
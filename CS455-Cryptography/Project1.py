import operator

def Main():

    with open("ciphertext.txt", "r",encoding='utf-8') as file:
        text = file.read()
    

    frequency = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in text:
        if letter in alphabet:
            if letter not in frequency:
                frequency[letter] = 1
            else:
                frequency[letter] += 1

    print("Frequency of letters in given ciphertext",frequency)
    print("\n")


    guess = text.replace("B", "e")
    guess = guess.replace("N", "t")
    guess = guess.replace("A", "h")  #THE freq analysis

    guess = guess.replace("U", "a")   # "AT"

    guess = guess.replace("V", "o") #only option that fits with two letter words for "to"

    guess = guess.replace("W", "n") # Only option for THA(N) because E and T are already solved

    guess = guess.replace("L", "d")  # Last sentence of first pg NEE(D) and AN(D) substitutes L

    guess = guess.replace("R", "f") #two letter word that can't be ON so OF is also frequent

    guess = guess.replace("K", "i")  #Two letter word ending in N and cant be o or n or e

    guess = guess.replace("H", "c")  # First sentence "in FAHT" or in FA(C)T

    guess = guess.replace("C", "r")  # first sentence "conCaction" -> contraction

    guess = guess.replace("Q", "m")  #first sentence iQQediate -> immediate

    guess = guess.replace("Y", "l")  # the faiYOre -> the "failure"
    guess = guess.replace("O", "u")  

    guess = guess.replace("G", "s") #third line conGiderinS -> "considering"
    guess = guess.replace("S", "g")  

    guess = guess.replace("F", "p")  #first line simFle -> "simple"

    guess = guess.replace("J", "y")  #first line onlJ -> "only"

    guess = guess.replace("D", "x")   #4th line ineDperienced -> "inexperienced"

    guess = guess.replace("M", "q")  #4th line Muestion -> "question"

    guess = guess.replace("I", "w")  # Ias -> was Ias -> was also www website at end of txt

    guess = guess.replace("T", "b")  #last paragraph weTsite -> website also aTout -> about

    guess = guess.replace("E", "j")  #proEect -> project last paragraph

    guess = guess.replace("Z", "v")  #receiZed -> received second paragraph

    guess = guess.replace("P", "k")  #second pg first line walPed -> walked

    guess = guess.replace("X", "z")  #last letter x -> z familiariXed 

    print(guess) #prints decrypted text

    with open('plaintext.txt', 'w',encoding='utf-8') as f:
     f.write(guess)
    

Main()
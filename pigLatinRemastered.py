sentence = input("Enter a line to be translated into pig latin: \n")

def pigLatin(sentence):
    if sentence == " ":
        print("No answer given")
        return

    pig = "ay"

    word_list = sentence.lower().split()
    vowels = "aeiouy"

    result = []



    for word in word_list:
        first = word[0]

        if first in vowels:
            word += "w"

        elif word[1] not in vowels and word[2] not in vowels:
            word = word[3] + word[0:3]

        elif word [1] not in vowels:
            word = word[2] + word[0:2]

        else:
            word = word[1:] + word[0]
        
        new_word = word + pig
        result.append(new_word)
        

    final_sentence = " ".join(result)
    print(final_sentence[0].upper() + final_sentence[1:] + ".")

    run_again = input("Translate another line(y/n): ").lower()
    
    if run_again == "y":
        sentence = input("Enter a line to be translated \n") 
        pigLatin(sentence)
    elif run_again == "n":
        print("Goodbye")


pigLatin(sentence)
        

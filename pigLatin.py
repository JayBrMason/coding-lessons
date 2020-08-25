def main():
    words = str(input("Input word:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")
    print ()
    
    run_again = input("continue?(y/n) ")
    print (run_again)

    if run_again == "n":
        print ("Done")

    elif run_again == "y":
        
        main()
main()

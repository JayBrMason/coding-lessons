num = int(input("Input a number:"))


def squares(num):
  print("Number, Squared, Cubed")
  for i in range(1, num+1):
    if i <= num:
      print (i, i**2, i**3)
  



  run_again = input("continue?")
  print (run_again)

  if run_again == "y":
    num = int(input("enter a whole number"))
    squares(num)

squares(num)
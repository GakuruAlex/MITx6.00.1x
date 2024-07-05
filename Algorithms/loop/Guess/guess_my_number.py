def guess_my_number()-> None:
     print("Please think of  a number between 0 (inclusive) and 100!")

     high: int = 100
     low: int = 0


     while True:
         mid: int = int((low + high) / 2)
         print(f"Is your secret number {mid}?")
         reply = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

         if reply == 'h':
             high = mid
         elif reply == "l":
             low = mid
         elif reply == "c":
             break
         else:
              print("Sorry, I did not understand your input.")

     print(f"Game over. Your secret number was: {mid}")

def main()->None:
    guess_my_number()

if __name__ == "__main__":
    main()
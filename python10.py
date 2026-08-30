# How while loops work- countdown

#count = 5

#while count > 0 :
#    print(count)
#    count = count - 1

#print("What the Deuce!")

# rep counter

#for rep in range(1, 5):
#    print(f"Thats a rep .{rep}")

# Lets try creating a guessing game

secret_word = "python"

while True:
    guess = input("Guess what programming language we using: ").lower()

    if guess == secret_word:
        print("HOORAY You guessed it!")
        break
    else:
        print("OUUUH Try again!")
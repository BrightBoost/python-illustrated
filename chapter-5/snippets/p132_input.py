name = input("What is your name? ")
print("Hello", name)


secret_word = "python123"
attempt = ""

while attempt != secret_word:
    attempt = input("Guess the word: ")

print("You've guessed it!")
# Without match statement
pet_type = "axolotl"

if pet_type == "cat":
    print("A cat goes meow!")
elif pet_type == "dog":
    print("A dog goes woof!")
elif pet_type == "parrot":
    print("A parrot says 'Polly wants a cracker!'")
elif pet_type == "hamster":
    print("A hamster squeaks and loves to run on a wheel.")
elif pet_type == "snake":
    print("A snake goes hiss!")
elif pet_type == "lizard":
    print("A lizard may hiss softly or stay silent.")
elif pet_type == "tarantula":
    print("A tarantula doesn't vocalize, it's scary enough as is.")
else:
    print("I'm not sure what sound this pet makes!")



# With match statement
pet_type = "axolotl"

match pet_type:
    case "cat":
        print("A cat goes meow!")
    case "dog":
        print("A dog goes woof!")
    case "parrot":
        print("A parrot says 'Polly wants a cracker!'")
    case "hamster":
        print("A hamster squeaks and loves to run on a wheel.")
    case "snake":
        print("A snake goes hiss!")
    case "lizard":
        print("A lizard may hiss softly or stay silent.")
    case "tarantula":
        print("A tarantula doesn't vocalize, it's scary enough as is.")
    case _:
        print("I'm not sure what sound this pet makes!")



command = "sit"

match command:
    case "sit":
        print("Wiesje sits down.")
    case "stay":
        print("Wiesje stays put.")
    case "fetch":
        print("Wiesje fetches the ball.")
    case _:
        print("Wiesje tilts her head in confusion.")



# Multiple values for same case with | symbol
pet_type = "puppy"

match pet_type:
    case "cat" | "kitten":
        print("A cat goes meow!")
    case "dog" | "puppy":
        print("A dog goes woof!")
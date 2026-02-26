nr1 = 6
nr2 = 6
same = nr1 == nr2

nr1 = 5
nr2 = 7
same = nr1 == nr2

nr1 = 5
nr2 = 7
different = nr1 != nr2

hours_slept = 8
needed_sleep = 12
needs_more_sleep = hours_slept < needed_sleep

temperature = 25
is_hot = temperature > 30

not_cold = temperature >= 20
not_hot = temperature <= 25

is_comfortable = temperature >= 20 and temperature <= 25

is_uncomfortable = temperature <= 20 or temperature >= 25

favorite_food = "tuna"
is_favorite = favorite_food == "tuna"
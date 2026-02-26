is_dachshund = True
is_blue = False
is_blue_dachshund = is_dachshund and is_blue

is_sunny = True
is_human_home = True
going_outside = is_sunny and is_human_home

is_sunny = True
is_human_home = False
going_outside = is_sunny and is_human_home

is_sunny = True
is_human_home = True
if is_sunny and is_human_home:
    print("Perfect moment for a long nap in the sun!")
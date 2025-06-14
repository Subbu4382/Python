# Missionaries and Cannibals Game
boat_side = "Right"
missionaries_on_right = 3
cannibals_on_right = 3
missionary_on_left = 0
cannibals_on_left = 0
# ........................#
print("M =",missionary_on_left,"C =",cannibals_on_left,"|----------BOAT|","M =",missionaries_on_right,"C =",cannibals_on_right,)
print()
# ........................#
while True:
    missionaries = int(input("enter number of missionaries or enter 4 to quit : "))
    if missionaries == 4:
        print("You Quit. Game is Over")
        break
    cannibals = int(input("enter number of cannibals :"))

    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        print("Invalid Move: Total number of people on the boat should be 1 or 2 only")
        continue
    if boat_side == "Right":
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            print("Invalid move ")

        missionaries_on_right = missionaries_on_right - missionaries
        cannibals_on_right = cannibals_on_right - cannibals

        missionary_on_left = missionary_on_left + missionaries
        cannibals_on_left = cannibals_on_left + cannibals

        print()
        print("M =", missionary_on_left, "C =",cannibals_on_left,"|BOAT----------|","M =",missionaries_on_right, "C =",cannibals_on_right)
        print()
        boat_side = "Left"

    else:
        if missionary_on_left < missionaries or cannibals_on_left < cannibals:
            print("Invalid move")

        missionary_on_left = missionary_on_left - missionaries
        cannibals_on_left = cannibals_on_left - cannibals

        missionaries_on_right = missionaries_on_right + missionaries
        cannibals_on_right = cannibals_on_right + cannibals

        print()
        print("M =",missionary_on_left,"C =",cannibals_on_left,"|----------BOAT|","M =",missionaries_on_right,"C =",cannibals_on_right,)
        print()
        boat_side = "Right"

    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionary_on_left < cannibals_on_left and missionary_on_left > 0):
        print("you Loose the game! Better luck Next Time")
        break
    if missionary_on_left == 3 and cannibals_on_left == 3:
        print("*****You Won*****")
        break

with open('A_Input.txt') as file:
    puzzleInput = file.read()

points = 0
ref = "ABC"
ref2 = "BCA"

for i in puzzleInput.split("\n"):
    print(i)
    j = ref.index(i[0])
    if i[-1] == "Y":
        points += 3 + j + 1
    elif i[-1] == "Z":
        points += 6 + ref.index(ref2[j]) + 1
    else:
        points += ref2.index(i[0]) + 1
    print(points)
    print()

print(points)
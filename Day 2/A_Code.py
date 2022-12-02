with open('A_Input.txt') as file:
    puzzleInput = file.read()

points = 0
ref = "123"
ref2 = "231"

for i in puzzleInput.replace("A", '1').replace("B", '2').replace("C", '3').replace("X", '1').replace("Y", '2').replace(r"Z", '3').split("\n"):
    if i[0] == i[-1]:
        points += 3
    elif ref[ref2.index(i[-1])] == i[0]:
        points += 6
    points += int(i[-1])

print(points)
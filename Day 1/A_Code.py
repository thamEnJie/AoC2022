with open('A_Input.txt') as file:
    puzzleInput = file.read()

print(max([sum([int(y) for y in x.split("\n")]) for x in puzzleInput.split("\n\n")]))
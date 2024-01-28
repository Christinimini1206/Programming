"""
4
bird 2 flies eatsworms
cow 4 eatsgrass isawesome makesmilk goesmoo
sheep 1 eatsgrass
goat 2 makesmilk eatsgrass
"""

N = int(input())
animals = [input().split() for inp in range(N)]

maxim = 0
for a in range(N):  # Each animal
    character = [0] * int(animals[a][1])
    for char in range(int(animals[a][1])):  # Each characteristic pf an animals
        for check in range(N):  # Checking each characteristic in other animals
            # print(animals[a][2:][char], animals[check])
            if (check != a) and (animals[a][2:][char] in animals[check]):
                character[char] += 1
                # print(character)
    print(animals[a][0], character)

    if 0 in character:


    charCount = len(set(character))
    if charCount > maxim:
        maxim = charCount
print(maxim)



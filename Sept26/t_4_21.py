t = int(input()) # ввели кількість рядків, які ще належить зчитати із вхідних даних

FLOWER_GERANIUM = 1
FLOWER_CROCUS = 2
FLOWER_VIOLET = 3

for j in range(t):
    k = int(input())
    # G <--> FLOWER_GERANIUM
    # C <--> FLOWER_CROCUS
    # V <--> FLOWER_VIOLET
    #
    # posLeft, posCenter, posRight
    # початкове розташування було GCV, тобто FLOWER_GERANIUM, FLOWER_CROCUS, FLOWER_VIOLET
    posLeft = FLOWER_GERANIUM
    posCenter = FLOWER_CROCUS
    posRight = FLOWER_VIOLET
    for i in range(k):
        # перестановка правої і центральної квіточок
        posCenter, posRight = posRight, posCenter
        # альтернативний спосіб обміну значеннями між двома змінними:
        # tmp = posRight
        # posRight = posCenter
        # posCenter = tmp

        # перестановка лівої і центральної квіточок
        posCenter, posLeft = posLeft, posCenter
    #print(posLeft, posCenter, posRight)
    if posLeft == FLOWER_GERANIUM:
        print('G', end='')
    elif posLeft == FLOWER_CROCUS:
        print('C', end='')
    else:
        print('V', end='')

    if posCenter == FLOWER_GERANIUM:
        print('G', end='')
    elif posCenter == FLOWER_CROCUS:
        print('C', end='')
    else:
        print('V', end='')

    if posRight == FLOWER_GERANIUM:
        print('G')
    elif posRight == FLOWER_CROCUS:
        print('C')
    else:
        print('V')

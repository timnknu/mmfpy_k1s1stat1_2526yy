t = int(input()) # ввели кількість рядків, які ще належить зчитати із вхідних даних

for j in range(t):
    k = int(input())
    # G <--> 2
    # C <--> 8
    # V <--> 9
    #
    # posLeft, posCenter, posRight
    # початкове розташування було GCV, тобто 2, 8, 9
    posLeft = 2
    posCenter = 8
    posRight = 9
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
    if posLeft == 2:
        print('G', end='')
    elif posLeft == 8:
        print('C', end='')
    else:
        print('V', end='')

    if posCenter == 2:
        print('G', end='')
    elif posCenter == 8:
        print('C', end='')
    else:
        print('V', end='')

    if posRight == 2:
        print('G')
    elif posRight == 8:
        print('C')
    else:
        print('V')

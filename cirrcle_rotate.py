from os import system as sys
from time import sleep 
# import math




#расчет кординат для круга 



# cords.sort(key=lambda p: math.atan2(p[0], -p[1])) # команда заменяющая сортировку снизу




def circle_sort(): 

    cords = []
    for y in range(-26, 26):
        for x in range(-26, 26):
            cordinate = []
            if 25**2 >= (x**2) + ((y*2)**2) and 25**2 <= (x**2) + 50 + ((y*2)**2) + 50: # +50
                # print("#", end = "") # отрисовка для дебага
                cordinate.append(x)
                cordinate.append(y)
                cords.append(cordinate)
            else: 
                pass
                # print(" ", end = "") # отрисовка для дебага
        print("")
    # input()
    




    # for y in range(-26, 26):
    #     for x in range(-26, 26):
    #         cordinate = []
    #         if 25**2 >= (x**2) + ((y*2)**2)  and 25**2 <= (x**2) + ((y*2)**2)+25:
    #             print(f"({x}, {y})| ", end = "")

    #         else: print(" ", end = "")
    #     print("") # отрисовка для дебага



    # секторы круга 
    def sector(p):
        x, y = p
        if x >= 0 and y <= 0:
            sektor = 1
        elif x >= 0 and y > 0:
            sektor = 2
        elif x < 0 and y >= 0:
            sektor = 3
        elif x < 0 and y < 0:
            sektor = 4
        return (sektor)






    # списки для сектров
    fst_list = []
    snd_list = []
    trd_list = []
    fth_list = []





    #первый сектор
    for i in cords:
        if sector(i) == 1:
            fst_list.append(i)

    # print(fst_list) # вывод ля дебага








    # второй сектор
    for i in cords:
        if sector(i) == 2:
            snd_list.append(i)

    # сортировка по часовой стрелке
    for  i in range(len(snd_list)):
        for j in range(len(snd_list)):
            try:
                if snd_list[j+1][0] > snd_list[j][0] and snd_list[j+1][1] == snd_list[j][1]:
                    snd_list[j+1][0], snd_list[j][0] = snd_list[j][0], snd_list[j+1][0]
            except:
                pass
    # print(snd_list) # вывод для дебага








    # третий сектор
    for i in cords:
        if sector(i) == 3:
            trd_list.insert(0, i)
    # print(trd_list) # вывод для дебага








    # четвертый сектор
    for i in cords:
        if sector(i) == 4:
            fth_list.insert(0, i)

    # сортировка по часовой стрелке
    for  i in range(len(fth_list)):
        for j in range(len(fth_list)):
            try:
                if fth_list[j+1][0] < fth_list[j][0] and fth_list[j+1][1] == fth_list[j][1]:
                    fth_list[j+1][0], fth_list[j][0] = fth_list[j][0], fth_list[j+1][0]
            except:
                pass
    # print(fth_list) # вывод для дебага









    cords = fst_list + snd_list + trd_list + fth_list
    return cords


    # print("\n\n\nall", )
    # print(cords)        # вывод для дебага







sorted_cords = circle_sort()

from os import system as sys
from time import sleep

# ... функция circle_sort() остаётся без изменений ...

sorted_cords = circle_sort()

# все списки line1list...line4list и block генерации line_cords удалены


def render():
    sys("mode con: cols=200 lines=26")
    sys("cls")
    while True:
        for i in range(len(sorted_cords)):
            # четыре вершины квадрата для текущего i
            n = len(sorted_cords)
            x1cord = sorted_cords[i]
            x2cord = sorted_cords[(i - n // 4) % n]
            x3cord = sorted_cords[(i - n // 2) % n]
            x4cord = sorted_cords[(i - (3 * n) // 4) % n]

            # список всех точек рёбер (линий) текущего квадрата
            line_points = []

            # вспомогательная функция: все целые точки отрезка между a и b
            def line_between(a, b):
                points = []
                x1, y1 = a
                x2, y2 = b
                dx = x2 - x1
                dy = y2 - y1
                steps = max(abs(dx), abs(dy))
                if steps == 0:
                    return [a]
                for s in range(steps + 1):
                    t = s / steps
                    x = round(x1 + t * dx)
                    y = round(y1 + t * dy)
                    points.append([x, y])
                return points

            # добавляем рёбра квадрата
            line_points += line_between(x1cord, x2cord)
            line_points += line_between(x2cord, x3cord)
            line_points += line_between(x3cord, x4cord)
            line_points += line_between(x4cord, x1cord)

            # отрисовка
            for y in range(-13, 13):
                for x in range(-25, 26):
                    if [x, y] in ([x1cord, x2cord, x3cord, x4cord] + line_points ):
                        print("#", end="")
                    else:
                        print(" ", end="")
                print("")
            sleep(0.05)


render()
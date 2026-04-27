from os import system as sys
# import math




#расчет кординат для круга 
cords = []
for y in range(-26, 26):
    for x in range(-26, 26):
        cordinate = []
        if 25**2 >= (x**2) + ((y*2)**2) and 25**2 <= (x**2) + 50 + ((y*2)**2) + 50: # +50
            print("#", end = "") # отрисовка для дебага
            cordinate.append(x)
            cordinate.append(y)
            cords.append(cordinate)
        else: 
            pass
            print(" ", end = "") # отрисовка для дебага
    print("")
input()
    



# cords.sort(key=lambda p: math.atan2(p[0], -p[1])) # команда заменяющая сортировку снизу




def circle_sort(cords): 


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







sorted_cords = circle_sort(cords)






# отрисовка
def render():
    sys("mode con: cols=200 lines=26")
    for i in sorted_cords:
        for y in range(-13, 13):
            for x in range(-25, 26):
                if i[0] == x and i[1] == y:
                    print("#", end = "")
                else:
                    print(" ", end = "")
            print("")
        input("")

        








while True:
    render()


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



sorted_cords = circle_sort()



def zrotate(i):

    n = len(sorted_cords)
    z1cord = sorted_cords[i][0]
    z2cord = sorted_cords[i - n // 4][0] #- n // 4
    z3cord = sorted_cords[i - n // 4 * 3][0]
    z4cord = sorted_cords[i - n // 4 * 2][0]
    zallcords = [z1cord, z2cord, z3cord, z4cord]


    return(zallcords)



def yrotate(i):

    n = len(sorted_cords)
    y1cord = sorted_cords[i][1]
    y2cord = sorted_cords[i - n // 4][1] #- n // 4
    y3cord = sorted_cords[i - n // 4 * 3][1]
    y4cord = sorted_cords[i - n // 4 * 2][1]
    yallcords = [y1cord, y2cord, y3cord, y4cord]


    return(yallcords)




# def zrotate(i):

#     n = len(sorted_cords)
#     x1cord = sorted_cords[i][0]
#     x2cord = sorted_cords[i - n // 4][0] #- n // 4
#     x3cord = sorted_cords[i - n // 4 * 3][0]
#     x4cord = sorted_cords[i - n // 4 * 2][0]
#     xallcords = [x1cord, x2cord, x3cord, x4cord]


#     return(xallcords)




def cordcalc(i, wha):
    
    zcrd = zrotate(i)
    ycrd = yrotate(i)

    
    sum_cords1 = []
    sum_cords2 = []
    sum_cords3 = []
    sum_cords4 = []





    sum_cords1.append(zcrd[0])
    sum_cords1.append(ycrd[0])

    sum_cords2.append(zcrd[1])
    sum_cords2.append(ycrd[1])

    sum_cords3.append(zcrd[2])
    sum_cords3.append(ycrd[2])

    sum_cords4.append(zcrd[3])
    sum_cords4.append(ycrd[3])

    sum_cords_all = [sum_cords1, sum_cords2, sum_cords3, sum_cords4]

    return sum_cords_all





        























def render():
    sys("mode con: cols=100 lines=26")
    
    for i in range(len(sorted_cords)):
        cordsss = cordcalc(i, all)

        for y in range(-13, 13):
            for x in range(-26, 26):

                if  [x, y] in cordsss:
                    print("#", end = "")
                else:
                    print(" ", end = "")
            print()
        what = input("x y z: ")
        if what == "z":
            cordcalc(i, "z")

render()


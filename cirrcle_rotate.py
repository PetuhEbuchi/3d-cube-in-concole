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
                print("#", end = "") # отрисовка для дебага
                cordinate.append(x)
                cordinate.append(y)
                cords.append(cordinate)
            else: 
                pass
                print(" ", end = "") # отрисовка для дебага
        print("")
    input()
    




    for y in range(-26, 26):
        for x in range(-26, 26):
            cordinate = []
            if 25**2 >= (x**2) + ((y*2)**2)  and 25**2 <= (x**2) + ((y*2)**2)+100:
                print(f"({x}, {y})| ", end = "")

            else: print(" ", end = "")
        print("") # отрисовка для дебага
    input()



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









    first_cords = fst_list + snd_list + trd_list + fth_list

    new_cords = first_cords[18:] + first_cords[:18]

    return new_cords


    # print("\n\n\nall", )
    # print(cords)        # вывод для дебага







sorted_cords = circle_sort()

n = len(sorted_cords)


def zspin(i):

    zcrd1 = sorted_cords[i][0]
    zcrd2 = sorted_cords[i][0]

    zcrd3 = sorted_cords[i][0]
    zcrd4 = sorted_cords[i][0]

    zcrd5 = sorted_cords[i][0]
    zcrd6 = sorted_cords[i][0]

    zcrd7 = sorted_cords[i][0]
    zcrd8 = sorted_cords[i][0]

    zcrdall = [[zcrd1, 0], [zcrd2, 0], [zcrd3, 0], [zcrd4, 0], [zcrd5, 0], [zcrd6, 0], [zcrd7, 0], [zcrd8, 0]]
    

    return zcrdall




def yspin(i):

    ycrd1 = sorted_cords[i][1]
    ycrd2 = sorted_cords[i][1]

    ycrd3 = sorted_cords[i- n // 4 + 1][1]
    ycrd4 = sorted_cords[i- n // 4 + 1][1]


    ycrd5 = sorted_cords[i- n // 4 * 2 + 2][1]
    ycrd6 = sorted_cords[i- n // 4 * 2 + 2][1]

    ycrd7 = sorted_cords[i- n // 4 * 3][1]
    ycrd8 = sorted_cords[i- n // 4 * 3][1]

    

    ycrdall = [[0, ycrd1], [0, ycrd2], [0, ycrd3], [0, ycrd4], [0, ycrd5], [0, ycrd6], [0, ycrd7], [0, ycrd8]]
    

    return ycrdall




zi = 0
yi = 0


def spincalc(i, wha):

    global zi
    global yi

    if zi >= n:
        zi = 0

    if yi >= n:
        yi = 0


    zcords = zspin(zi)
    ycords = yspin(yi)

    if wha == "z":
        

        zi += 1
        for j in range(len(zcords)):

            zcords[j][1] = ycords[j][1]

        

        return zcords
    
    

    elif wha == "y":
        
            
        yi += 1
        for j in range(len(ycords)):

            ycords[j][0] = zcords[j][0]
        
        

        return ycords

    



    










def render():
    stage = "z"

    while True:
        for i in range(n):
            cord = spincalc(i, stage)
            for y in range(-13, 13):
                for x in range(-50, 26):

                    if [x, y] in cord:
                        print("#", end = "")
                    else:
                        print(" ", end = "")


                print()
            what = input("x y z: ")

            if what == "z":
                cord = spincalc(i, "z")
                stage = "z"

            elif what == "y":
                cord = spincalc(i, "y")
                stage = "y"
            else:
                stage = stage
            



render()











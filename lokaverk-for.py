#Sigurður Axel
#7.5.2017


#öll hrutaspil eru hér
hrutaspil = [{"Sokki":[41,108,7,0,17.3,108,144,8.5]},
             {"Freyðir":[46.4,105,7.9,135,17.4,103,118,8.6]},
             {"Vöðvi":[47,100,8,0,17.5,106,112,9]},
             {"Kjói":[48.8,116,8.4,160,17,94,111,8.3]},
             {"Bogi":[49.9,110,8.3,310,17.3,102,116,8.5]},
             {"Falur":[48.3,106,8.2,26,16.9,95,114,8.3]},
             {"Borði":[42,110,8,0,18,104,0,9]},
             {"Bramli":[47.5,104,7.8,357,17.2,106,102,8.4]},
             {"Kaldi":[47.8,100,7.9,218,17.1,135,93,8.4]},
             {"Vorm":[47.6,95,7.8,158,17.3,111,122,8.5]},
             {"Smyrill":[47.8,101,7.9,97,17.2,95,144,8.4]},
             {"Prjónn":[47.5,110,7.8,370,17.5,105,122,8.6]},
             {"Grábotni":[45,102,7.5,0,17.5,106,139,8.5]},
             {"Kóngur":[59,108,8,0,17.5,105,114,8.5]},
             {"Garpur":[48.6,106,8.2,101,17.3,98,116,8.5]},
             {"Broddi":[57,92,75,0,18,99,144,9.5]},
             {"Frakkson":[49.6,110,8.4,325,17.2,106,117,8.4]},
             {"Þróttur":[48,106,7.8,222,17.4,105,121,8.5]},
             {"Bifur":[45.5,96,7.7,407,17.5,110,115,8.7]},
             {"Stáli":[85,102,8,0,17.5,100,130,9]},
             {"Fálki":[51,103,7.5,0,17.5,102,142,9]},
             {"Kjarkur":[48,108,7.5,0,17,108,0,8.5]},
             {"Hólmi":[45,104,7.5,0,18,95,0,9]},
             {"Púki":[49,111,7.7,403,17.3,114,119,8.5]},
             {"Mjöður":[46.4,102,8,210,17.5,103,127,8.6]},
             {"Mókollur":[49.6,111,7.9,135,16.9,122,102,8.2]},
             {"Gotti":[47.2,100,8,182,17.5,102,119,8.6]},
             {"Hrói":[63,107,8,0,17.3,108,108,8.5]},
             {"Dökkvi":[45.5,102,7.8,157,17.2,105,120,8.5]},
             {"Bolli":[51,109,9,0,17.5,111,109,9]},
             {"Týr":[38,96,8,0,17.5,105,131,8.5]},
             {"Papi":[45.6,82,8,428,17.6,106,140,8.7]},
             {"Tengill":[45,94,8,0,17.5,97,145,9]},
             {"At":[45.6,110,7.9,244,17.5,110,139,8.5]},
             {"Grái":[48.3,111,7.9,381,17.4,105,122,8.6]},
             {"Ylur":[47.4,111,8,184,17.2,96,117,8.4]},
             {"Neisti":[47,106,8.5,0,18.5,104,116,9]},
             {"Logi":[53,109,8.5,0,18,101,114,9]},
             {"Kveikur":[49,113,7.8,1085,17.4,106,118,8.6]},
             {"Shrek":[49.5,117,8.1,82,17.3,103,118,8.5]},
             {"Cat":[47.7,98,7.6,193,17.5,100,128,8.6]},
             {"Fannar":[46.4,105,7.9,222,17.4,101,125,8.6]},
             {"Hvellur":[48.8,112,8,552,17.3,96,113,8.6]},
             {"Raftur":[47.1,106,7.8,1406,17.6,112,122,8.6]},
             {"Blossi":[54,108,8.5,0,18,111,113,9]},
             {"Blettur":[44.9,100,7.9,332,17.2,99,109,8.3]},
             {"Mundi":[46,104,7.5,0,16.5,110,126,8.5]},
             {"Hriflon":[49,112,8,0,18,110,124,8.5]},
             {"Skrauti":[45,111,7,0,17.3,98,112,8.5]},
             {"Krókur":[47.5,101,8,218,17.5,92,157,8.7]},
             {"Undri":[49.1,108,8.4,76,17.2,100,109,8.4]},
             {"Ás":[48.8,121,8.1,82,17.2,108,110,8.3]},
            ]


#á eftir að raða þessu randomly


svar1 = " "
while(svar1 != 3):
    print("<---------------------------------------------------------->")
    print("1. Spila")
    print("2. Hvernig á ég að spila???")
    print("3. Hætta")

    svar1 = int(input("Veldu að spila: "))

    if svar1 == 1:

        import random
        #öll spilin eru í röð svo að 0 væri sokki
        stokkur = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
        #listin er randomly breytur með shuffle
        random.shuffle(stokkur)
        #tölur fyrir framan 26 í listanum er fyrir tölvuna og aftan er fyrir spilaran
        com = stokkur[26:]
        player = stokkur[0:26]


        val = " "
        while(val != 9):
            for key,value in hrutaspil[player[0]].items():
                print("<---------------------------------------------------------->")
                print("Þú átt", len(player), "spil eftir")#segir hversu mörg spil þú átt eftir
                print("Tölvan á", len(com), "spil eftir")
                print(key)#skirfar út nafn á fyrsta spil sem spilarin fær
                print("1. Þyngd----------------:",value[0])
                print("2. Mjólkurlagni dætra---:",value[1])
                print("3. Einkunn ullar--------:",value[2])
                print("4. Fjöldi afkvæma-------:",value[3])
                print("5. Einkunn læris--------:",value[4])
                print("6. Frjósemi-------------:",value[5])
                print("7. Gerð/þykkt bakvöðvar-:",value[6])
                print("8. Einkun fyrir malir---:",value[7])
                print("9. Hætta")

                val = int(input("Hvað er val þitt: "))

                if len(com) == 0:#ef tölan á engin spil eftir
                    print("Til hamingju þú vannst leikin")
                    val = 9

                elif len(player) == 0:#ef spilarin á engin spil eftir
                    print("Þú tapar :(")
                    val = 9
                elif val ==1:
                    print("þú valdir þyngd")
                    for key,value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[0]#value 0 er þyngd hjá spilara
                    for key,value in hrutaspil[com[0]].items():
                        þyngdCom = value[0]#value 0 er þyngd hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með hærri þyngd")
                        for key,value in hrutaspil[com[0]].items():
                            print("Þú færð" , key)
                        take = com[0]
                        player.insert(-1,take)#tekur spil frá hinum 
                        del com[0]
                    elif þyngdCom > þyngdPlayer:#spilarinn tapar
                        print("Tölvan var með hærri þyngd")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1,take1)#gefur tölvuni sit spil
                        del player[0]
                    elif þyngdCom == þyngdPlayer:#það er jafntepli
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur innsláttur")

                if val ==2:
                    print("Þú valdir mjólkurlagni dætra")
                    for key,value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[1]#value 1 er dætra hjá spilara
                    for key,value in hrutaspil[com[0]].items():
                        þyngdCom = value[1]#value 1 er dætra hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með hærri dætra")
                        for key,value in hrutaspil[com[0]].items():
                            print("Þú færð" , key)
                        take = com[0]
                        player.insert(-1,take)#tekur spil frá hinum 
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með hærri dætra")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1,take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur innsláttur")

                if val ==3:
                    print("Þú valdir enkunn ullar")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[2]#value 2 er ekunn ullar hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[2]#value 2 er enkunn ullar hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með hærri enkunn ullar")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum 
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með enkunn ullar")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur innsláttur")
                if val ==4:
                    print("Þú valdir fjöldi afkvæma")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[3]#value 3 er fjöldi afkvæma hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[3]#value 3 er fjöldi afkvæma hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með herri fjöldi afkvæma")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með herri fjöldi afkvæma")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur insláttur")

                if val ==5:
                    print("Þú valdir einkunn læris")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[4]#value 4 er einkunn læris hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[4]#value 4 er einkunn læris hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með herri einkunn læris")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með herri einkunn læris")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur insláttur")

                if val ==6:
                    print("Þú valdir frjósemi")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[5]#value 5 er frjósemi hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[5]#value 5 er frjósemi hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með herri frjósemi")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með herri herri frjósemi")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur insláttur")

                if val ==7:
                    print("Þú valdir gerð/þykkt bakvöðvar")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[6]#value 6 er gerð/þykkt bakvöðvar hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[6]#value 6 er gerð/þykkt bakvöðvar hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með herri gerð/þykkt bakvöðvar")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með herri gerð/þykkt bakvöðvar")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur innsláttur")
                if val ==8:
                    print("Þú valdir Einkun fyrir malir")
                    for key, value in hrutaspil[player[0]].items():
                        þyngdPlayer = value[7]#value 7 er Einkun fyrir malir hjá spilara
                    for key, value in hrutaspil[com[0]].items():
                        þyngdCom = value[7]#value 7 er Einkun fyrir malir hjá tölvu
                    if þyngdPlayer > þyngdCom:#spilarin vinur
                        print("Þú varst með herri Einkun fyrir malir")
                        for key, value in hrutaspil[com[0]].items():
                            print("Þú færð", key)
                        take = com[0]
                        player.insert(-1, take)#tekur spil frá hinum
                        del com[0]
                    elif þyngdCom > þyngdPlayer:
                        print("Tölvan var með herri Einkun fyrir malir")
                        for key, value in hrutaspil[player[0]].items():
                            print("Þú missir", key)
                        take1 = player[0]
                        com.insert(-1, take1)#tekur spil frá hinum 
                        del player[0]
                    elif þyngdCom == þyngdPlayer:
                        print("Jafntefli")
                        print("Veldu eithvað annað")
                    else:
                        print("Rangur innsláttur")


    elif svar1 == 2:#Segir hvernig maður á að spila leikinn
        print("Þú færð 26 spil.")
        print("Þú færð 8 valmöguleika til að spila með.")
        print("Ef þú ert með hærri tölu en hann þá færð þú spilið hans.")
        print("Til þess að vinna þarft þú að taka öll spilin hans.")

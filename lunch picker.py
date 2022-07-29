import random
x = 1
while x:
    eat_type = {0:"race_type", 1:"noodle_type", 2:"Brunch_type", 3:"other_type"}
    race_type = {0:"南豐", 1:"土魠魚", 2:"聞香", 3:"唐小鴨"}
    noodle_type = {0:"孩餃", 1:"四海", 2:"八方"}
    Brunch_type = {0:"墨爾", 1:"元之氣", 2:"麥當勞", 3:"丹丹"}
    other_type = {0:"關東煮"}
    a =  random.randint(0,3)
    race_type_len =  random.randint(0,len(race_type)-1)
    noodle_type_len =  random.randint(0,len(noodle_type)-1)
    Brunch_type_len =  random.randint(0,len(Brunch_type)-1)
    other_type_len =  random.randint(0,len(other_type)-1)
    print(eat_type[a])
    print("please input yes or no")
    yn = input("")
    if yn == "yes":
        if eat_type[a] == "race_type":
            print(race_type[race_type_len])
            print("please input yes or no")
            yn_1 = input("")
            if yn_1 == "yes":
                x= 0
            elif yn_1 == "no":
                del race_type[race_type_len]
                x = 1
        elif eat_type[a] == "noodle_type":
            print(noodle_type[noodle_type_len])
            print("please input yes or no")
            yn_2 = input("")
            if yn_2 == "yes":
                x = 0
            elif yn_2 == "no":
                del noodle_type[noodle_type_len]
                print(noodle_type)
                x = 1
        elif eat_type[a] == "Brunch_type":
            print(Brunch_type[Brunch_type_len])
            print("please input yes or no")
            yn_2 = input("")
            if yn_2 == "yes":
                x = 0
            elif yn_2 == "no":
                del Brunch_type[Brunch_type_len]
                x = 1
        if eat_type[a] == "other_type":
            print(other_type[other_type_len])
            x = 0
    elif yn == "no":
        x = 1

f = open("songs.csv").read()
import csv
with open("songs.csv") as f:
    f = f.read().split("\n")
headers = f.pop(0)
main_list = [string.split(";") for string in f]

def data_counter(day,month,year):
    """Функция data_counter считает количество дней
    в двух датах и возвращает их разность в днях
    day - порядкорвый номер дня
    month - порядкорвый номер месяца
    year - порядкорвый номер года

    """

    dat_1 = 12+31+28+31+30+31
    for i in range(1,2023):
        if i%4 == 0:
            dat_1 += 364
        else: dat_1 += 365

    dat_2 = day
    for i in range(1,year):
        if i%4 == 0:
            dat_2 += 364
        else: dat_2 += 365

    for i in range(1,month+1):
        if month == 2 and year%4 == 0:
            dat_2+=29
        elif month == 2 and year%4 != 0:
            dat_2+=29
        elif month in [1,3,5,7,8,10,12]:
            dat_2+=31
        else: dat_2+=30
    return(dat_1-dat_2)




streams_sorted_list = []
for track in main_list:
    s = track[-1].split(".")
    if s[0] == '': continue
    else:
        num1 = int(s[0])
        num2 = int(s[1])
        num3 = int(s[2])
        if int(track[0]) != 0:
            streams_sorted_list.append(track)

        else:
            streams =( data_counter(num1,num2,num3) / (len(track[1])+len(track[2])))*10000
            track[0] = str(streams)
            streams_sorted_list.append(track)



data_streams_sorted_list = []
for track in main_list:
    s = track[-1].split(".")
    if s[0] == '': continue
    else:
        num1 = int(s[0])
        num2 = int(s[1])
        num3 = int(s[2])
        if (num3 == 2002 and num2 <=1 and num1 <= 1) or num3 < 2002:
            if int(track[0]) != 0:
                data_streams_sorted_list.append(track)
            else:
                streams =( data_counter(num1,num2,num3) / (len(track[1])+len(track[2])))*10000
                track[0] = str(round(streams))
                data_streams_sorted_list.append(track)


f = open("songs.csv","w")
f.write(headers+"\n")
for track in streams_sorted_list:
    f.write(";".join(track)+"\n")



f = open("songs_new.csv","w")
f.write(headers+"\n")
for track in data_streams_sorted_list:
    f.write(";".join(track)+"\n")

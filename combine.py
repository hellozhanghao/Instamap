import pprint

pp = pprint.PrettyPrinter(indent=5)

f = open("id_coordinates.csv",'r')

line = f.readline()
id_coordinates_name = {}
while line != "":
    info = line[:-1].split(",")
    id_coordinates_name[info[0]]= [info[1], info[2]]
    line = f.readline()

f = open("id_name.csv","r", errors="ignore")

line = f.readline()
while line!="":
    tag = line.find(",")
    name = line[tag:].replace("\"","").replace(",","").replace("\n","")
    if line[:tag] in id_coordinates_name:
        if len(id_coordinates_name[line[:tag]])!=3:
            id_coordinates_name[line[:tag]].append(name)
    line = f.readline()


to_remove = set()
for id in id_coordinates_name:
    if len(id_coordinates_name[id]) != 3:
        to_remove.add(id)

for id in to_remove:
    id_coordinates_name.pop(id)


f = open("id_media.csv","r")

line = f.readline()

id_media = []
while line!= "":
    info = line.split(",")
    info[3]=info[3][:-1]
    if info[3] == "Error-3":
        info[3] = "5"
    id_media.append(info)
    line = f.readline()

id_media_trim = []
for media in id_media:
    if media[3] != "Error-1" and media[3] != "Error-2" and media[3] != "Error-4" and media[3].isdigit():
        id_media_trim.append(media)

id_media = id_media_trim

f = open("combined_data.csv",'w')
f . write("id,media_code,date_time,num_of_likes,lat,lon,name\n")
result = []
for item in id_media:
    id = item[0]
    if id in id_coordinates_name:
        f.write(id+",")
        f.write(item[1]+",")
        f.write(item[2]+",")
        f.write(item[3]+",")
        f.write(id_coordinates_name[id][0]+",")
        f.write(id_coordinates_name[id][1]+",")
        f.write(id_coordinates_name[id][2]+"\n")

f.close()


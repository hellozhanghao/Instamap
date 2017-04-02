from get_number_of_likes import try_media_likes

start = 17001
end   = 18000

fin = open("instagram_media_data_cleaned.csv",'r')
fout = open("media_data/number_of_likes_"+str(start)+"-"+str(end)+".csv", 'w')

line = fin.readline()

count = 0

while line != '':

    if count < start:
        line = fin.readline()
        count += 1
    else:
        if count == end+1:
            break
        info = line.split(',')
        info[2] = info[2][:-1]

        response = try_media_likes(info[1], max_try=10)
        if response[0] == 'ok':
            info.append(response[1].replace(",",""))
        else:
            info.append("Error-"+str(response[1]))

        print(count, info)
        fout.write(info[0]+","+info[1]+","+info[2]+","+info[3]+'\n')

        line = fin.readline()
        count += 1

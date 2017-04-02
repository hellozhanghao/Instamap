fin = open("instagram_media_data.csv","r",encoding='utf-8', errors='ignore')
fout = open("instagram_media_data_cleaned.csv","w")

line = fin.readline()
while line != '':

    info = line.split(',')
    fout.write(info[0]+","+info[-2]+","+info[-1][1:-2]+'\n')
    # print(info[0]+","+info[-2]+","+info[-1][1:-2])
    line = fin.readline()

fin.close()
fout.close()

from get_number_of_likes import try_media_likes

start = 1
end = 20



fin = open("instagram_media_data_cleaned.csv",'r')

line = fin.readline()
while line != '':
    
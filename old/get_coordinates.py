from geopy.geocoders import Nominatim

geolocator = Nominatim()

fin = open("instagram_locations.csv", "r", encoding='utf-8', errors='ignore')
fout = open("locations_coordinates.csv", "w")

line = fin.readline()




def get_loation(name, max_try):
    for i in range(max_try):
        try:
            location = geolocator.geocode(name + ", Singapore")
            if location is not None:
                return location
        except:
            # print("Exception")
            pass
    return None


count = 0
while line != '':
    count += 1
    tag = line.find(",")
    id = line[:tag]
    name = line[tag + 1:-1]
    location = get_loation(name=name, max_try=5)
    if location is not None:
        ans = ""
        ans += id+","
        ans += name.replace(",", " ") +","
        ans += str(location.latitude) + ","
        ans += str(location.longitude)
        print(str(count)+" "+ans)
        fout.write(ans + "\n")
    else:
        print(str(count)+" Error")

    line = fin.readline()


#
# location = geolocator.geocode("SUTD")
# print(location.address)
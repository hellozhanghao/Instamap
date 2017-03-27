import urllib.request
locations = ['sutd', 'chinatown', 'changiairport','singaporezoo','nus','ntu','sit','angmokio']

for location in locations:
    url = "https://www.instagram.com/explore/tags/" + location+ "/?hl=en"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    webpage = response.read().decode('utf-8')
    # print(webpage)

    tag = webpage.find("See Instagram photos and videos")

    print(location, webpage[tag - 14:tag - 2])
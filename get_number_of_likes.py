import urllib.request


def get_number_of_likes(media_code):
    url = "https://www.instagram.com/p/" + media_code
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request,timeout=10)

    webpage = response.read().decode('utf-8')
    tag = webpage.find("_iuf51 _oajsw")
    if tag == -1: return "error", 1
    webpage = webpage[tag:]

    tag = webpage.find(media_code)
    if tag == -1: return "error", 2
    webpage = webpage[:tag]

    tag = webpage.find("span data-reactid")
    if tag == -1: return "error", 3
    webpage = webpage[tag + 23:]

    tag = webpage.find("</")
    if tag == -1: return "error", 4
    webpage = webpage[:tag]

    return "ok", webpage


def try_media_likes(media_code, max_try):
    for i in range(max_try):
        try:
            # print("try " + str(i))
            result = get_number_of_likes(media_code)
            if result[0] == "ok":
                return result
        except:
            print("Exception")
    return result



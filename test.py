client_id ="b5c8af1bee0f44b8b0054a329107de0a"
client_secret = "6ed3f0a35db34481afb68a7fb3a9aac9"
from instagram.client import InstagramAPI

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=4)
for media in popular_media:
    print(media.images['standard_resolution'].url)
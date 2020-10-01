from pexels_api import API          # pip install pexels_api
import os
import requests

def downloadImage(url, fotoid, arama):
    img_data = requests.get(url).content
    
    with open(f"Download/{arama}/{fotoid}.jpeg", "wb") as img:      # Save to local disk (Download)
        img.write(img_data)

PEXELS_API_KEY = 'your key' # Your api key goes here.
api = API(PEXELS_API_KEY)

search = input("Search something to download / İndirmek için bir kelime arayın: ") # Search for image
if (os.path.exists(f"Download/{search}") == False):         # Don't create any folder if folder exists.
    os.mkdir(f"Download/{search}")
arama = api.search(search)

while True:

    photos = api.get_entries()
    dosyalar = os.listdir(f"Download/{search}")         # Create a list for continue to download

    for photo in photos:
        if (os.path.exists(f"Download/{arama}/{photo.id}.jpeg") == False):    # If photo exists, don't download again

            downloadImage(photo.original, photo.id, search)
    
    if (api.has_next_page == False):
        break

    api.search_next_page()
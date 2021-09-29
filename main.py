

import requests


def send(mysetting):

    import glob

    URL = mysetting.URL
    TOKEN = mysetting.TOKEN
    COLLECTION_NAME = mysetting.COLLECTION_NAME
    DIR_IMAGES = mysetting.DIR_IMAGES
    RECURSIVE = mysetting.RECURSIVE

    if mysetting.recursive == True:
        path_files = glob.glob(DIR_IMAGES + "/*/*.jpg", recursive=RECURSIVE):
    else:
        path_files = glob.glob(DIR_IMAGES + "/*.jpg", recursive=RECURSIVE):

    
    for f in path_files:
        print(f)
        send_image(URL, TOKEN, COLLECTION_NAME, f)

def create_url_postImage(URL, COLLECTION_NAME):
    return URL + "collections/" + COLLECTION_NAME + "/images"

def send_image(URL, TOKEN, COLLECTION_NAME, PATH_IMG):
    
    file = { 'image': open(PATH_IMG, "rb") }
    headers = {
        'authorization': 'Bearer' + ' ' + TOKEN
    }
    
    URL_POST = create_url_postImage(URL, COLLECTION_NAME)
    print(URL_POST)

    res = requests.post(url=URL_POST, headers=headers, files=file)

    print(res.text, res.ok)
    

if __name__ == '__main__':

    import argparse, json
    parser = argparse.ArgumentParser(description = 'send an image to DB')
    parser.add_argment('--setting', '-S', default='.env.json', help = 'path for program that is .json form')
    arg = parser.parse_arg()

    try:
        with open(arg.setting, 'r') as file:
            mysetting = json.load(file)
        send(mysetting)
    except Exception as  e:
        print(e)
    finally:
        print("finished")
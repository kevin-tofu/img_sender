

import requests


def send(mysetting):

    import glob
    import os.path

    URL = mysetting["URL"]
    TOKEN = mysetting["TOKEN"]
    COLLECTION_NAME = mysetting["COLLECTION_NAME"]
    DIR_IMAGES = mysetting["DIR_IMAGES"]
    RECURSIVE = mysetting["RECURSIVE"]

    path_files = list()
    if RECURSIVE == True:
        path_files = glob.glob(DIR_IMAGES + "/*/*.jpg", recursive=RECURSIVE)
    path_files += glob.glob(DIR_IMAGES + "/*.jpg", recursive=False)

    myfields = None
    for fpath in path_files:
        
        dirname = os.path.dirname(fpath)
        myfields = { 'dirname': dirname}

        print(fpath, myfields)
        res = send_image(URL, TOKEN, COLLECTION_NAME, fpath, fields=myfields)
        print(res.text, res.ok)

def create_url_postImage(URL, COLLECTION_NAME):
    return URL + "collections/" + COLLECTION_NAME + "/images"

def send_image(URL, TOKEN, COLLECTION_NAME, PATH_IMG, fields=None):
    
    file = { 'image': open(PATH_IMG, "rb") }
    headers = {
        'authorization': 'Bearer' + ' ' + TOKEN
    }
    
    URL_POST = create_url_postImage(URL, COLLECTION_NAME)
    print(URL_POST)

    if fields is None:
        res = requests.post(url=URL_POST, headers=headers, files=file)
    else:
        res = requests.post(url=URL_POST, headers=headers, files=file, fields=fields)
    return res
    
    

if __name__ == '__main__':

    import argparse, json
    parser = argparse.ArgumentParser(description = 'send an image to DB')
    parser.add_argument('--setting', '-S', default='.env.json', help = 'path for program that is .json form')
    arg = parser.parse_args()

    try:
        with open(arg.setting, 'r') as file:
            mysetting = json.load(file)
        send(mysetting)
    except Exception as  e:
        print(e)
    finally:
        print("finished")
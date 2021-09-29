

if __name__ == '__main__':
    
    from main import send

    url_myplace = ""
    token_my = ""
    collection = ""
    path_dir1 = ""

    setting = {
        "URL": url_myplace,
        "TOKEN": token_my,
        "COLLECTION_NAME": collection,
        "DIR_IMAGES": path_dir1,
        "RECURSIVE": False
    }

    send(setting)
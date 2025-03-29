from clipboard import *
import json

def ads_info(txt_copy):
    dic_ad = json.loads(txt_copy)
    _list = []
    for z in dic_ad:
        if "videoId" in  z:
            _list += [dic_ad[z]]
    id_ad = _list[-1]
    return f"https://www.youtube.com/watch?v={id_ad}"

def main():
    txt_copy = paste()
    url_ad = ads_info(txt_copy)
    print(url_ad)


if __name__ == "__main__" :
    main()
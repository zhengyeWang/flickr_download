import json
import glob
import requests

from flickrapi import FlickrAPI

FLICKR_PUBLIC = '5da5d342025d1d7dafb49eb411b48e98'
FLICKR_SECRET = '2af4389288878875'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_o'#'url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
search = flickr.photos.search(text='people', per_page=1000, extras=extras)
#print(search)

total_page = search['photos']['pages']
print(total_page)
#photos = search['photos']
#photo = search['photos']['photo']
#from pprint import pprint
#pprint(photos)

_name = glob.glob("/Users/wangzhengye/Project/flickr/face/*.jpg")
print(_name)
for j in range(total_page):
    search_page = flickr.photos.search(text='people', per_page=1000, extras=extras, page=j)
    photos = search_page['photos']
    photo = search_page['photos']['photo']
    for i in range(len(photo)):
        #print("url=",photo[i]["url_o"])
        id = photo[i]['id']
        name = ("/Users/wangzhengye/Project/flickr/face/%s.jpg"%(id))
        print("id = ",id)
        print(name)
        if name not in _name:
            print("not in ")
            try:
                res = requests.get('%s'%(photo[i]["url_o"]))
                info_res = flickr.photos_getInfo(photo_id=id)
                print(info_res)
            except:
                continue
            f = open("/Users/wangzhengye/Project/flickr/face/%s.jpg"%(id),'wb')
            f.write(res.content)
            f.close()
            w = open("/Users/wangzhengye/Project/flickr/face_json/%s.json"%(id),'w', encoding="utf-8")
            w.write(json.dumps(info_res,indent=4))
            w.close()
        else:
            print("in")
            continue


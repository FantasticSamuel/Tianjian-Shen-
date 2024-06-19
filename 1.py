import requests
from bs4 import BeautifulSoup
import time
import random

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
    'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'spm_id_from': '333.1007.tianma.1-1-1.click',
    'vd_source': '0f2a77ebbde1ed3c6d855301e2802c28',
}

response = requests.get('https://www.bilibili.com/video/BV1Q34y1u7L9/', params=params, headers=headers).text
q=[]
set_cite=set()
set_cite.add("BV1Q34y1u7L9")
#print(response)
bvids_head=0
bvids_tail=0
i=-1
while True:
    bvids_head=response.find('bvid":"',bvids_tail)
    if bvids_head==-1:
        break
    bvids_tail=response.find('",',bvids_head)
    if bvids_tail==-1:
        break
    if response[bvids_head+7:bvids_tail] in set_cite:
        continue
    q.append((response[bvids_head+7:bvids_tail],i))
    set_cite.add(response[bvids_head+7:bvids_tail])
    i+=1
    #print(response[bvids_head+6:bvids_tail+1])


while len(q)>0:
    bvid,idd=q.pop(0)
    params = {
    'spm_id_from': f'333.788.recommend_more_video.{idd}',
    'vd_source': '0f2a77ebbde1ed3c6d855301e2802c28',
    }
    response = requests.get(f'https://www.bilibili.com/video/{bvid}/', params=params, headers=headers).text
    print(f'https://www.bilibili.com/video/{bvid}/?spm_id_from=333.788.recommend_more_video.{idd}&vd_source=0f2a77ebbde1ed3c6d855301e2802c28')
    bvids_head=0
    bvids_tail=0
    ii=-2
    while True:
        bvids_head=response.find('bvid":"',bvids_tail)
        if bvids_head==-1:
            break
        bvids_tail=response.find('",',bvids_head)
        if bvids_tail==-1:
            break
        ii+=1
        if response[bvids_head+7:bvids_tail] in set_cite:
            continue
        q.append((response[bvids_head+7:bvids_tail],ii))
        set_cite.add(response[bvids_head+7:bvids_tail])
    time.sleep(random.randint(1,3))

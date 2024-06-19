import requests
import json
import time
import requests

cookies = {
    'eai-sess': 'o9gdbrkk9f8jpbbh9cg11m1k45',
    'UUkey': '198337b4226741663fb8a4ef9a2acab1',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'eai-sess=o9gdbrkk9f8jpbbh9cg11m1k45; UUkey=198337b4226741663fb8a4ef9a2acab1',
    'Origin': 'https://yanyuan.pku.edu.cn',
    'Referer': 'https://yanyuan.pku.edu.cn/yywd/wap/default/index',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'order[0][id]': '3',
    'order[0][num]': '1',
    'order[0][name]': '燕逐月',
    'date': '',
}
while True:
    response = requests.post('https://yanyuan.pku.edu.cn/yywd/wap/default/order', cookies=cookies, headers=headers, data=data)
    print(response.text)
    res=json.loads(response.text)
    m=res['m']
    localtime=time.asctime(time.localtime(time.time()))
    print(localtime[11:19])
    starttime="11:59:40"
    endtime="12:01:00"
    if m=="您选购的套餐已部分售罄，请重新选择":
        print("no")
    elif m=="预订时间为12:00到23:55":
        print("not yet")
    else:
        print("yes")
    if localtime[11:19]>=starttime and localtime[11:19]<=endtime:
        time.sleep(0.05)
    else:
        time.sleep(10)
    
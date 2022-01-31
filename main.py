import json
from os import system
import requests
import time
url = "https://api.bilibili.com/x/operational_activity/bnj2022/live/integrate?scene_ids=1,2"
jsonmap = json.loads(requests.get(url).text)
stimes = []
etimes = []
lt = 5
for i in range(len(jsonmap['data']['exam_detail']['bank'])):
    stimes.append(jsonmap['data']['exam_detail']['bank'][i]['start_time'])
    etimes.append(jsonmap['data']['exam_detail']['bank'][i]['end_time'])
system("cls")
while True:
    time0 = time.time()
    if(lt % 5 == 0):
        system("cls")
        # print("\x1b[21A")
        jsonmap = json.loads(requests.get(url).text)
        time1 = time.time()
        timeuse = time1 - time0
        ck = 0
        # print("===========================================")
        print("此次请求时间:", time0)
        print("请求使用时间:", timeuse)
        print("当前所在的题目:", end="")
        for i in range(len(stimes)):
            if time1 > stimes[i] and time1 < etimes[i]:
                print("第", i+1, "题 ", jsonmap['data']
                      ['exam_detail']['bank'][i]['title'])
                ck = i
        ac = 0
        for i in range(4):
            ac += jsonmap['data']['exam_detail']['bank'][ck]['options'][i]['count']
        print("选项: ")

        print("|-A:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][0]['title'])
        print("|---计数:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][0]['count'])
        print("|---比率:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][0]['count']/ac)
        print("|-B:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][1]['title'])
        print("|---计数:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][1]['count'])
        print("|---比率:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][1]['count']/ac)
        print("|-C:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][2]['title'])
        print("|---计数:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][2]['count'])
        print("|---比率:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][2]['count']/ac)
        print("|-D:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][3]['title'])
        print("|---计数:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][3]['count'])
        print("|---比率:", jsonmap['data']['exam_detail']
              ['bank'][ck]['options'][3]['count']/ac)
        Achoice = jsonmap['data']['exam_detail']['bank'][ck]['options'][0]['count']/ac
        Bchoice = jsonmap['data']['exam_detail']['bank'][ck]['options'][1]['count']/ac
        Cchoice = jsonmap['data']['exam_detail']['bank'][ck]['options'][2]['count']/ac
        Dchoice = jsonmap['data']['exam_detail']['bank'][ck]['options'][3]['count']/ac
        choi = "A"
        if Achoice > Bchoice and Achoice > Cchoice and Achoice > Dchoice:
            choi = "A"
        if Bchoice > Achoice and Bchoice > Cchoice and Bchoice > Dchoice:
            choi = "B"
        if Cchoice > Achoice and Cchoice > Bchoice and Cchoice > Dchoice:
            choi = "C"
        if Dchoice > Achoice and Dchoice > Bchoice and Dchoice > Cchoice:
            choi = "D"

        print("根据现在的情况,选", choi, ",因为有", end="")
        if choi == "A":
            print(jsonmap['data']['exam_detail']['bank'][ck]
                  ['options'][0]['count'], "人选它,占", Achoice*100, "%.")
        if choi == "B":
            print(jsonmap['data']['exam_detail']['bank'][ck]
                  ['options'][1]['count'], "人选它,占", Bchoice*100, "%.")
        if choi == "C":
            print(jsonmap['data']['exam_detail']['bank'][ck]
                  ['options'][2]['count'], "人选它,占", Cchoice*100, "%.")
        if choi == "D":
            print(jsonmap['data']['exam_detail']['bank'][ck]
                  ['options'][3]['count'], "人选它,占", Dchoice*100, "%.")
        nesttime = etimes[ck + 1] - time0
        print("还有", int(nesttime), "秒此题截止.")
    nesttime = etimes[ck + 1] - time0
    print("\x1b[1A还有", int(nesttime), "秒此题截止.")
    time.sleep(1)
    lt += 1

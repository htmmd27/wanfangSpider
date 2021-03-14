# -*- coding:UTF-8 -*-
import requests
import json
import time
import csv
# 爬取期刊名称，后续需要随着期刊数量增长更改期刊总数目
if __name__ == '__main__':
    # 万方期刊页面url
    target = "http://c.wanfangdata.com.cn/Category/Magazine/search"
    # cookies可能需要后续更改
    headers = {
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,zh-TW;q=0.6",
        "Cookie": "Hm_lvt_838fbc4154ad87515435bf1e10023fab=1614312081; zh_choose=n; CASTGC=TGT-19294163-mcoQSqubEsJ2OAqtLibDJeYznOZjf0TbknMFLsHMpLY0JJxVFG-my.wanfangdata.com.cn; WFKS.Auth=%7B%22Context%22%3A%7B%22AccountIds%22%3A%5B%22Group.tjsg04%22%2C%22Shibboleth.tjsg04%22%2C%22GTimeLimit.tjsg04%22%5D%2C%22Data%22%3A%5B%7B%22Key%22%3A%22Group.tjsg04.DisplayName%22%2C%22Value%22%3A%22%E5%A4%A9%E6%B4%A5%E5%A4%A7%E5%AD%A6%22%7D%5D%2C%22SessionId%22%3A%222515da81-0068-4148-8eb6-ee8bb2554be1%22%2C%22Sign%22%3A%22yFSXOjpsi5nvx1e3fn4gbFYADYIn6bLCD%2BnebDxv2llaBupxWoSOl61w6zMdLEcg%22%7D%2C%22LastUpdate%22%3A%222021-03-01T00%3A27%3A41Z%22%2C%22TicketSign%22%3A%22%5C%2Fe2hvazihtNyhh8AKFCH9w%3D%3D%22%2C%22UserIp%22%3Anull%7D"
    }
    start_num = 0
    # 存储每类期刊代码 哲学政法0/B 606  社会科学0/C 890  经济财政0/F 1005 教科文艺0/G 2030 基础科学0/N 1125 医药卫生0/R 1522 农业科学0/S 649 工业技术0/T 2842
    # 以上代码用来替换data中的 class_code 字段
    id = 0

    # # 哲学政法0 / B 606
    # with open('./zxzf.csv', 'w', encoding='utf-8',newline="") as f:
    #     writer = csv.writer(f)
    #     while start_num < 606:
    #         # 使用{{}}转义，然后使用format进行数据插入
    #         data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/B","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
    #             start_num)
    #         req = requests.post(url=target, headers=headers, data=data)
    #         req.encoding = 'utf-8'
    #         # 将json转换为数组字典格式
    #         periodicalJson = json.loads(req.text)
    #         periodicalList = periodicalJson.get('value')
    #         time.sleep(2)
    #         for i in periodicalList:
    #             print(id, i.get('Title'))
    #             id += 1
    #             writer.writerow(i.get('Title'))
    #         start_num = start_num + 50
    # f.close()

    # 社会科学0/C 890
    start_num = 0
    with open('./periodicalName/shkx.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 890:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/C","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 经济财政0/F 1005
    start_num = 0
    with open('./periodicalName/jjcz.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 1005:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/F","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 教科文艺0/G 2030
    start_num = 0
    with open('./periodicalName/jkwy.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 2030:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/G","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 基础科学0/N 1125
    start_num = 0
    with open('./periodicalName/jckx.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 1125:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/N","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 医药卫生0/R 1522
    start_num = 0
    with open('./periodicalName/yyws.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 1522:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/R","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 农业科学0/S 649
    start_num = 0
    with open('./periodicalName/nyws.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 649:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/S","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

    # 工业技术0/T 2842
    start_num = 0
    with open('./periodicalName/gyjs.csv', 'w', encoding='utf-8',newline="") as f:
        writer = csv.writer(f)
        while start_num < 2842:
            # 使用{{}}转义，然后使用format进行数据插入
            data = '{{"query":[],"start":{},"rows":50,"sort_field":{{"sort_field":"ImpactFactor"}},"highlight_field":"","pinyin_title":[],"class_code":"0/T","core_periodical":[],"sponsor_region":[],"publishing_period":[],"publish_status":"","return_fields":["Title","Id","CorePeriodical","Award","IsPrePublished"]}}'.format(
                start_num)
            req = requests.post(url=target, headers=headers, data=data)
            req.encoding = 'utf-8'
            # 将json转换为数组字典格式
            periodicalJson = json.loads(req.text)
            periodicalList = periodicalJson.get('value')
            time.sleep(2)
            for i in periodicalList:
                print(id, i.get('Title'))
                id += 1
                writer.writerow(i.get('Title'))
            start_num = start_num + 50
    f.close()

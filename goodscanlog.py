import json
import requests
import interparkapi as park
import merge
import randomdate
import pandas as pd
import glob
import xlrd
import openpyxl
import time


url = "http://book.interpark.com/api/search.api?key="
url += park.key
url += "&output=json"
url += "&queryType=isbn"


def read_excel():
    ret = pd.DataFrame()
    for i in glob.glob('goodscanlog/*.xlsx'):
        df = pd.read_excel(i, skiprows=3, sheet_name='Sheet1').dropna(how='all').dropna(how='all', axis=1)
        ret = ret.append(df, ignore_index=False)

    ret = ret.drop_duplicates(keep=False)
    ret = ret.loc[:, ~ret.columns.str.contains('^Unnamed')]
    return ret


def process_log():
    ret = []
    log = read_excel()

    for i in range(len(log)):
        tmp = dict()
        if type(log.iloc[i, 0]) != str:
            break

        tmp['date'] = randomdate.to_jsdate(log.iloc[i, 0])
        try:
            tmp['id'] = str(int(log.iloc[i, 1]))
        except:
            tmp['id'] = str(log.iloc[i, 1])
        ret.append(tmp)
    return ret


def id_from_log():
    res = read_excel()
    ret = set()

    for i in range(len(res)):
        if type(res.iloc[i, 0]) != str:
            break

        if res.iloc[i, 1] is float:
            ret.add(str(int(res.iloc[i, 1])))
        else:
            ret.add(str(res.iloc[i, 1]))

    return ret


def query_interpark(code: set):
    mydb = []

    for i in code:
        response = requests.get(url + "&query=" + i)
        body = json.loads(response.text)
        if body['returnCode'] != "000":
            print("검색한 id " + i + " 를 조회하는데 실패했습니다.")
            continue

        for j in body['item']:
            mydb.append(j)
        time.sleep(0.2)

    return mydb


if __name__ == "__main__":
    # barcode = id_from_log()
    # tmp = query_interpark(barcode)
    # merge.merge_interpark(tmp)
    f = open('log.json', 'w')
    f.write(json.dumps(process_log(), indent='  '))
    f.close()

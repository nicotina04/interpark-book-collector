import json
import requests
import interparkapi as park
import time
import merge


arg = ['114', '116', '117', '122', '123', '125', '210', '211']
f = open('interparkbookid.json', 'r')
id = json.load(f)
f.close()


def collect_bestseller(tags: list):
    ret = []
    url = "http://book.interpark.com/api/bestSeller.api?key="
    url += park.key
    url += "&categoryId="
    for i in tags:
        if i not in id:
            continue
        response = requests.get(url + i + "&output=json")
        time.sleep(0.1)
        body = json.loads(response.text)

        for j in body['item']:
            ret.append(j)

    return ret


if __name__ == "__main__":
    best = collect_bestseller(arg)
    merge.merge_interpark(best)

import requests
import json
import time
import merge
import interparkapi as park


def collect_title(ar: list, cnt: int):
    url = "http://book.interpark.com/api/search.api?key="
    url += park.key
    url += "&output=json"
    ret = []

    for i in ar:
        response = requests.get(url + "&query=" + i)
        time.sleep(0.1)
        body = json.loads(response.text)
        if body['returnCode'] != "000":
            print(i, "검색 실패")
            continue

        for j in range(min(len(body['item']), cnt)):
            if 'isbn' not in body['item'][j]:
                print(body['item'][j]['title'], "는 id가 없습니다!!!")
            else:
                ret.append(body['item'][j])
    return ret


if __name__ == "__main__":
    words = ['수1', '수2', '개념원리', '완자', '토익', '토플', '텝스', '파이썬', '자바', '미적분학', '유체역학', '열역학']
    words += ['공무원', '통계학', '비문학', '수능 영어', '모의고사', '자료구조', '알고리즘', '항공역학']
    words += ['자이스토리', 'SSEN', '기하', '미적분']
    tmp = collect_title(words, 50)
    merge.merge_interpark(tmp)

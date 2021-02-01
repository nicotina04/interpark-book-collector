import randomdate
import random as rd
import json

f = open('interparkbookdb.json', 'r')
bookdb = json.load(f)
f.close()


def make_log(y: int, m: int):
    ret = dict()
    date = randomdate.gen_date(y, y, m, m)
    randbook = rd.choice(bookdb)
    ret['date'] = date
    ret['id'] = randbook['isbn']
    return ret


def merge_log(ar: list):
    mylog = []

    try:
        f = open('log.json', 'r')
        mylog = json.load(f)
        f.close()
    except:
        print("로그가 존재하지 않습니다.")

    for i in ar:
        mylog.append(i)

    mylog = sorted(mylog, key=lambda e: randomdate.jsdate_to_clock(e['date']))
    with open('log.json', 'w') as f:
        f.write(json.dumps(mylog, indent=2))


if __name__ == "__main__":
    tmp = []
    for i in range(4, 7):
        for j in range(rd.randint(400, 600)):
            tmp.append(make_log(2020, i))
    for i in range(7, 13):
        for j in range(rd.randint(1035, 1657)):
            tmp.append(make_log(2020, i))
    merge_log(tmp)

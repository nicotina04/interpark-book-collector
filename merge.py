import json


def merge_interpark(ar: list):
    mydb = []

    try:
        f = open('interparkbookdb.json', 'r')
        mydb = json.load(f)
        mydb = sorted(mydb, key=lambda e: e['isbn'])
        f.close()
    except:
        print("데이터베이스가 존재하지 않습니다.")

    for i in ar:
        if len(mydb) == 0:
            mydb.append(i)
            continue

        l = 0
        r = len(mydb) - 1
        found = False

        while l <= r:
            m = l + (r - l) // 2

            if mydb[m]['isbn'] == i['isbn']:
                found = True
                mydb[m] = i
                break
            elif mydb[m]['isbn'] < i['isbn']:
                r = m - 1
            else:
                l = m + 1

        if not found:
            mydb.append(i)
            mydb = sorted(mydb, key=lambda e: e['isbn'])
    f = open('interparkbookdb.json', 'w')
    f.write(json.dumps(mydb, indent='  '))
    f.close()

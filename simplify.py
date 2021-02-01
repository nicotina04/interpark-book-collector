import json


def simplify_interpark():
    output = dict()
    db = []
    try:
        f = open('interparkbookdb.json', 'r')
        db = json.load(f)
        f.close()
    except:
        return

    keywords = ['title', 'author', 'publisher', 'categoryId']
    for i in db:
        isbn = i['isbn']
        input = dict()

        for j in keywords:
            try:
                input[j] = i[j]
            except:
                if j == 'categoryId':
                    input[j] = "000"
                else:
                    input[j] = "정보없음"
        output[isbn] = input

    with open('isbn.json', 'w') as f:
        f.write(json.dumps(output, indent='  '))


if __name__ == "__main__":
    simplify_interpark()

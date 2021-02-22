import goodscanlog
import merge
import time
import shutil
import simplify


if __name__ == "__main__":
    print("굳스캔에서 누적한 데이터를 가공하는 과정을 시연합니다.")
    print("프로그램에서 엑셀 로그를 추출합니다.")
    pandaframe = goodscanlog.read_excel()

    print("추출한 로그에서 로그에 기록된 바코드를 다시 한번 추출합니다.")
    time.sleep(0.6)
    barcodes = goodscanlog.id_from_log(pandaframe)

    print("추출한 바코드를 나열합니다.\n")
    print("------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(1)
    idx = 0
    for i in barcodes:
        print(i, end=' ')
        if idx % 10 == 0 and idx != 0:
            print()
        idx += 1
    print()
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\n\n추출한 바코드를 바탕으로 책 정보를 수집합니다.\n")
    time.sleep(0.5)
    bookdata = goodscanlog.query_interpark(barcodes)

    # interparkbookdb.json
    print("책 정보 수집 완료. 출력 및 저장합니다.")
    print("------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.7)
    for i in bookdata:
        print(i)
    merge.merge_interpark(bookdata)

    # isbn.json
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\n수집한 정보에서 데이터 분석에 필요한 요소만 추출한 후 저장합니다.\n")
    time.sleep(0.8)
    simplify.simplify_interpark()

    # log.json
    print("엑셀 로그를 json db로 가공합니다.\n")
    result_data = goodscanlog.process_log(pandaframe)
    goodscanlog.write_log(result_data)
    print("가공된 데이터를 출력 및 저장합니다.\n")
    print("------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.4)
    for i in result_data:
        print(i)

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("\n시연 데이터를 출력했습니다.")
    print("실제 db를 관리자 프로그램과 연동합니다.")
    filenames = ['isbn.json', 'log.json', 'interparkbookdb.json']
    for i in filenames:
        # shutil.copyfile("./fulldata/" + i, "../frontapp/src/assets/" + i)
        shutil.move("./" + i, "../frontapp/src/assets/" + i)
    print("연결 성공. 프로그램을 종료합니다.")

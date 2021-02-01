interpark-book-collector
========================
인터파크에 등록된 도서들의 정보를 수집하는 라이브러리입니다.

## 사전 작업
이 라이브러리를 사용하기 전에 interparkapi.py를 생성해야 합니다.</br>
interparkapi.py에는 다음 변수만 포함하면 됩니다.</br>
```
key = [인터파크에서 발급받은 api키]
```
발급 방법은 [여기][apitutorial] 를 참조하세요.

### bestseller.py
```
collect_bestseller(tags: list)
```
카테고리가 담긴 tags를 인자로 전달합니다.</br>
tags에 담긴 카테고리마다 베스트 셀러를 검색하여 리스트에 담아 반환해줍니다.</br>
인터파크 도서의 카테고리는 [api 문서][interparkdocu]나 [깃허브 저장소][nicotina]에서 찾아볼 수 있습니다.</br>

### goodscanlog.py
사내용 모듈입니다. 다른 사용자에게는 필요 없습니다.

### merge.py
```
merge_interpark(ar: list)
```
기존에 생성한 인터파크 도서 데이터를 수집한 json 파일과 새롭게 수집한 데이터가 담긴 리스트를 병합 후 json 파일로 내보냅니다.

### randomdate.py
사내용 모듈입니다. 다른 사용자에게는 필요 없습니다.

### randomlog.py
사내용 모듈입니다. 다른 사용자에게는 필요 없습니다.

### search.py
```
collect_title(ar: list, cnt: int)
```
키워드가 담긴 리스트 ar과 검색 결과의 수집 상한 cnt를 전달합니다.</br>
메소드를 호출하게 되면 각 키워드마다 인터파크 도서 수집 결과를 가져오게 됩니다.</br>
만약 가져온 도서 데이터 중에 id가 없는 데이터가 있다면 그 도서는 무시합니다.</br>
id가 있다면 해당 데이터를 딕셔너리 형태로 리스트 ret에 추가합니다.</br>
키워드별로 api 호출을 모두 끝내면 ret을 리턴하게 됩니다.</br>

### simplify.py
```
simplify_interpark()
```
수집한 도서 데이터를 불러와 간략하게 만들어 준 후 json 파일로 저장합니다.</br>
가공 후 형식은 다음과 같습니다.</br></br>

key: 도서의 id</br>
value: 제목, 저자, 출판사, 도서의 인터파크 분류

[apitutorial]: https://blog.soobinpark.com/166 "티스토리 블로그"
[interparkdocu]: http://book.interpark.com/bookPark/html/bookpinion/api_booksearch.html "인터파크 api 문서"
[nicotina]: https://github.com/nicotina04/interpark-book-category "인터파크 api json 데이터"

# pip install beautifulsoup4 : beautifulsoup4 패키지 다운로드

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list : 현재 설치되어 있는 패키지 내용에 대해 볼 수 있음
# pip show beautifulsoup4 : beautifulsoup4에 대한 정보를 볼 수 있음
# pip install --upgrade beautifulsoup4 : 최신 버전으로 업데이트
# pip uninstall beautifulsoup4 : 패키지 삭제
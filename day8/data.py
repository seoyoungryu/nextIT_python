import requests
from bs4 import BeautifulSoup #크롤링
import pyautogui  #gui 형성
import openpyxl # 엑셀 파일 만들어 사용하기 위함
# pip install pyautogui
# pip install openpyxl

# 저장할 엑셀 파일 만들기
wb = openpyxl.Workbook()
sheet = wb.active

keyword = pyautogui.prompt("검색어를 입력하세요 >>> ")
lastpage = pyautogui.prompt("마지막 페이지 번호를 입력해주세요")
pageNum = 1

# 엑셀 시트에 열이름 설정해주기
sheet.append(["검색어명", "기사 제목", "기사 링크"])

for i in range(1, int(lastpage)+1):
    print(f"{pageNum} 페이지 입니다.====================") #포맷팅 활용해서 변수 바로 출력하기
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")  #리스트 형태(.news_tit에 기사 제목, 기사 링크)

    for link in links:
        title = link.text           #태그 안에 텍스트 요소(기사 제목)
        url = link.attrs['href']    #href의 속성 값(기사 링크)
        print(title, url)

        sheet.append([keyword, title, url])
    pageNum = pageNum + 1

wb.save("naver_news.xlsx")


# Review_Site
정직한 리뷰사이트
![](./img/logo.png)

## Prerequisite
python 3.7.5

Flask 1.1.2  
Flask-Migrate 2.5.3  
Flask-SQLAlchemy 2.4.4  
SQLAlchemy 1.3.20  

## Install
```
# 가상환경 실행(가상환경 사용 시)
. venv/Scripts/activate

# 의존성 설치
pip install -r requirements.txt

# DB Initialize
flask db init
flask db migrate
flask db upgrade

# Flask 실행
cd review_site
flask run
```
## Feature
- 양질의 리뷰와 그에 대한 최저가 비교 제공
- 양질의 리뷰를 위하여 그에 대한 보상 제공
- 검색 시 연관되는 상품을 보여주어 다양하게 쇼핑 가능

## Issue
- [x] Back-End Tool 선정(Flask)
- [x] API 연결 방안 탐색

# Review_Site
3학년 2학기 소공 / 레포이름대로 정직한 리뷰사이트

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

# Flask 실행
cd review_site
flask run

# DB Initialize
flask db init
flask db migrate
flask db update
```
## Feature
- 양질의 리뷰와 그에 대한 최저가 비교 제공
- 양질의 리뷰를 위하여 그에 대한 보상 제공

## Issue
- [x] Back-End Tool 선정(Flask)
- [ ] API 연결 방안 탐색
- [ ] 비회원 접근 차단
- [ ] 글에 사진 어떻게 넣지?

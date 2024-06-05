# 프로젝트 개요

## 소개
이 프로젝트는 Django를 사용하여 만든 웹 애플리케이션입니다. 주요 기능은 작물 및 연도선택, 생산량 예측, 공시지가 정보 제공 입니다. 
대부분의 코드는 원천 작성하였으며, views의 mapPrice 함수의 공시지가 활용api의 경우 api 제공 사이트인 v-world의 예시 코드를 수정하여 사용하였습니다. 예시코드를 이용해 이미지 파일을 만들어 사용자에게 제공하도록 수정하였습니다. 

## 폴더 구조
src/<br>
├── manage.py<br>
├── map/<br>
│ ├── init.py<br>
│ ├── admin.py<br>
│ ├── apps.py<br>
│ ├── models.py<br>
│ ├── tests.py<br>
│ ├── urls.py<br>
│ ├── views.py<br>
│ └── templates<br>
│    ├──index.html<br>
|    └──mapPrice.html<br>
│ └── myapp/<br>
│ └── base.html<br>
├── myWeb/<br>
│ ├── init.py<br>
│ ├── settings.py<br>
│ ├── urls.py<br>
│ ├── wsgi.py<br>
│ └── asgi.py<br>
├─ db.py<br>
├─ db.sqlite3<br>
├─ Overview.md<br>


## 디렉토리 및 파일 설명

### `manage.py`
- Django 프로젝트를 관리하기 위한 커맨드 라인 유틸리티입니다.

### `map/`
- 프로젝트의 주요 애플리케이션 폴더입니다.
  - `__init__.py`:
  - `admin.py`: Django 관리자 사이트에 모델을 등록합니다.
  - `apps.py`: 어플리케이션 map의 정의 파일 입니다.
  - `models.py`: predict폴더에 저장된 db를 정의합니다.
  - `tests.py`
  - `urls.py`: 애플리케이션의 URL 경로를 정의합니다. 어플리케이션의 패턴을 정의하였는데 작물선택, 지도표현, 공시지가 표현의 패턴을 저장하였습니다.
  - `views.py`: 뷰 로직을 정의하는데 작물선택, 공시지가 api와 이미지 생성, 위도경도 이용의 내용을 포함하였습니다. 
  - `templates/`: 
      - `index.html`: 기본 템플릿으로 사용자가 원하는 정보를 설정할 수 있습니다. html, css, javascript 이용하여 코드작성 하였습니다. 
      - `mapPrice.html`: 팝업 템플릿으로 공시지가와 생산량 정보를 표현하며 코딩하였습니다.

### `myWeb/`
- 프로젝트 설정 및 설정 파일을 포함합니다.
  - `__init__.py`:
  - `settings.py`: Django 프로젝트의 설정을 정의합니다.
  - `urls.py`: 프로젝트의 URL 경로를 정의합니다. 본 프로젝트에서는 'map' 하나의 앱을 사용하였습니다.
  - `wsgi.py`: WSGI 호환 웹 서버에서 사용할 설정입니다.
  - `asgi.py`: ASGI 호환 웹 서버에서 사용할 설정입니다.

### `++`
 - 'db.py': src외부 predict 파일을 이용해 db.sqlite3 생성. 
 - 'db.sqlite3' django에서 제공하는 db 사용. 
 - 'Overview.md' : Src파일에 대한 전반적인 설명입니다.

## 실행 방법

1. **아래 주소로 접속**
   `http://34.47.70.11:8000/`

# A4.3 OSS 프로젝트 제품 구성, 배포 및 운영 자료  

## 1. 프로젝트 제품 구성

- *프로젝트 제품의 구성과 배치 내역을 그림과 글로 설명*  
  
## 2. 프로젝트 제품 배포 방법  
사용 기술
- GCP: 클라우드 인프라 제공
- Django: 웹 애플리케이션 프레임워크
- Gunicorn: WSGI HTTP 서버
- Nginx: 리버스 프록시 및 정적 파일 서버
- Let's Encrypt: 무료 SSL 인증서 제공

배포 절차
1. GCP VM 인스턴스 생성
2. 루트 디렉토리에 레포지토리 클론 (git clone https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09.git)
3. Python 설치 및 환경변수 설정
4. ~\venvs에 가상환경 생성 (python3 -m venv venv) 및 실행 (source venv/bin/activate)<br>
![image](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/137899379/36f8c87a-3c59-4cbb-85d0-d76da62fba5d)<br>
![image](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/137899379/6ab2cc79-824c-45f1-b903-5b1d6d53cd30)
5. 필수 패키지 설치
<pre>
  pip install django
  pip install gunicorn
  sudo apt install nginx
</pre>



## 3. 프로젝트 제품 운영 방법  

- *프로젝트 제품의 시연을 위한 환경구성 및 운영방법 설명*
- *프로젝트 제품의 시연 시나리오 제시*  

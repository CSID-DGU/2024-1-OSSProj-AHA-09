# A4.3 OSS 프로젝트 제품 구성, 배포 및 운영 자료  

## 1. 프로젝트 제품 구성

- *프로젝트 제품의 구성과 배치 내역을 그림과 글로 설명*  
  
## 2. 프로젝트 제품 배포 방법  
### 사용 기술
- GCP: 클라우드 인프라 제공
- Django: 웹 애플리케이션 프레임워크
- Gunicorn: WSGI HTTP 서버
- Nginx: 리버스 프록시 및 정적 파일 서버
- Let's Encrypt: 무료 SSL 인증서 제공

### 배포 절차
1. GCP VM 인스턴스 생성
2. 루트 디렉토리에 레포지토리 클론
<pre>
  git clone https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09.git
</pre>
4. ~\venvs에 가상환경 생성 및 실행
<pre>
  python3 -m venv venv
  source venv/bin/activate
</pre>
![image](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/137899379/36f8c87a-3c59-4cbb-85d0-d76da62fba5d)<br>
![image](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/137899379/6ab2cc79-824c-45f1-b903-5b1d6d53cd30)
5. 필수 패키지 설치
<pre>
  pip install django
  pip install gunicorn
  sudo apt install nginx
</pre>
6. 정적 파일 모으기
<pre>
  python manage.py collectstatic
</pre>
8. 파일 세팅<br>

(~/venvs/myWeb.env)
<pre>
  DJANGO_SETTINGS_MODULE=myWeb.settings
</pre>

(/etc/nginx/sites-available/myWeb)
<pre>
  server {
        listen 80;
        server_name osspcrops.store;
        rewrite        ^ https://$server_name$request_uri? permanent;
  }
  
  server {
          listen 443 ssl;
          server_name osspcrops.store;
  
          ssl_certificate /etc/letsencrypt/live/osspcrops.store/fullchain.pem; # managed by Certbot
          ssl_certificate_key /etc/letsencrypt/live/osspcrops.store/privkey.pem; # managed by Certbot
          include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
  
          location = /favicon.ico { access_log off; log_not_found off; }
  
          location /static {
                  alias /home/hj708951/2024-1-OSSProj-Aha-09/myWeb/static;
          }
  
          location / {
                  include proxy_params;
                  proxy_pass http://osspcrops.store:8000;
          }
  }
</pre>
* 이후 sites-available에 작성한 myWeb 파일 추가 (sudo ln -s /etc/nginx/sites-available/myWeb /etc/nginx/sites-enabled)

(/etc/systemd/system/gunicorn.service)
<pre>
  [Unit]
  Description=gunicorn daemon
  After=network.target
  
  [Service]
  User=hj708951
  Group=hj708951
  WorkingDirectory=/home/hj708951/2024-1-OSSProj-Aha-09/myWeb
  EnvironmentFile=/home/hj708951/venvs/myWeb.env
  ExecStart=/home/hj708951/venvs/venv/bin/gunicorn \
          --workers 2 \
          --bind 0:8000 \
          myWeb.wsgi:application
  
  [Install]
  WantedBy=multi-user.target
</pre>

8. Gunicorn 서비스, Nginx 실행
<pre>
  sudo systemctl start gunicorn.servic
  sudo systemctl start nginx
</pre>


## 3. 프로젝트 제품 운영 방법  

- *프로젝트 제품의 시연을 위한 환경구성 및 운영방법 설명*
- *프로젝트 제품의 시연 시나리오 제시*  

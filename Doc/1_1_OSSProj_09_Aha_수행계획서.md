# A1.1 OSS 프로젝트 수행계획서

## 1. 프로젝트 수행팀 개요

* 수행 학기: 2024-1 
* 프로젝트명: 미국 전역의 옥수수 생산량 예측 지도 
* 팀명: Aha    

구분 | 성명 | 학번 | 소속학과 | 연계전공 | 이메일
------|-------|-------|-------|-------|-------
팀장 | 이현종 | 2019111655 | 바이오환경과학과 | 융합SW연계전공 | hjong1010@dongguk.edu       
팀원 | 임형준 | 2019112520 | 산업시스템공학과 | 융합SW연계전공 | 2019112520@dongguk.edu        
팀원 | 이건희 | 2019110475 | 통계학과 | 융합SW연계전공 | ish8176@dgu.ac.kr        

* 지도교수: (소속)      (성명) 

## 2. 프로젝트 수행계획  

### 2.1 프로젝트 개요

* 선택한 주제에 대해 잘 이해하고 학생 팀의 아이디어를 포함하여 개략적인 설명을 해야한다.  
* 프로젝트의 주제는 무엇인지 대략적인 설명과 해당 주제를 선정하게 된 배경, 해당 프로젝트의 필요성 및 해결 방향 등을 간략히 소개한다.  
* 또한, 달성하고자 하는 목적과 설계하고자 하는 최종 결과가 무엇인지 분명히 드러나도록 상세하게 기술한다.

### 2.2 추진 배경(자료조사 및 요구분석)

#### (1) 개발 배경 및 필요성  
* 기후 변화에 따른 생산량 예측의 필요성
   * 기후변화로 인해 농업 생태계가 어려움을 겪고 있으며 특히 작물 생산량에 대한 관심이 높아지고 있음
   * 농작물 생산량의 변동성이 커짐에 따라 생산 과잉은 악성 재고, 생산 부족은 가격 폭등을 유발하여 생산량 예측의 중요성이 대두되고 있음

* 미국의 농업 수요
   * 미국은 세계 곡물 총 생산량이 중국 다음으로 2위에 해당함
   * 2022년 미국 국내총생산(GDP)에 의하면 미국의 농업, 식품 및 관련 산업은 약 1조 4,200억 달러를 기여했으며 이는 전체 GDP의 5.5%에 해당함

* 농작물 생산량 예측 서비스 개발
   * 농작물 생산예측 웹 서비스를 개발하여 농업 종사자의 효율적인 재고 관리를 보장하고, 농업에 적합한 지역 발견을 도움
   * 농사를 시작하는 사람들에게 농작물 생산량을 예측하는 서비스를 제공하여 좋은 농경지를 선택 할 수 있도록 도움
   * 농작물 생산에 공급을 조절하고, 농업인들에게 최적의 농업환경을 찾아 효율적인 생산을 돕고, 더 나아가 전 지구적인 농작물 생산량 증대 및 안정화를 목표로 함

#### (2) 선행기술 및 사례 분석  
AS_IS<br>
Papers
- [1]"작물 생산량 예측을 위한 머신러닝 기법 활용 연구"에서는 스마트 팜에서 제공하는 여러가지 데이터 중 63개 데이터를 선정하여, 가장 중요한 세 가지 요인을 선정하였음
- [2]"기후변화가 벼의 생산량에 미치는 영향"에서는 기온, 강수량, 일조시간 등 기후와 벼 생산량의 관계를 분석하였음
Patents
- [3]"위성 영상을 이용한 작물 생산량 예측장치", [4]"인공신경망 및 선형 회귀를 이용한 작물 생산량 예측 방법" 과 같은 유사 특허가 존재함
- 본 프로젝트에서는 기존의 모델을 사용하는 것이 아니라 자체적으로 작물 생산량 예측 모델을 만들어 사용하고자 함
Services
- 국내 서비스로는, [5]"기상청 날씨마루" 에서 지역별 농작물 생산량을 예측하는 서비스를 제공함. 예측된 서비스를 이용해 가격 안정 및 수급을 조절할 수 있도록 함
- [6]미국의 경우 지역에 따른 작물의 수확량을 보여주는 서비스는 존재하지만, 이는 실제 어느 지역이 농사에 적합한지를 알 수 있는 지표는 아님
- 농사에 적합한 환경을 임의로 조성하여 작물 생산량을 늘리는 스마트 팜 기술이 존재하지만, 임의로 환경을 조설할 때 추가적인 에너지 소모와 비용이 발생함

TO_BE<br>
- 기존 농경지에서 작물 생산량을 예측하는 것이 아닌 새로운 환경에 분석모델을 적용하여 새로운 농경지를 찾아낼 수 있음
- 미국 대상으로는 기존에 없던 새로운 서비스임
- 스마트 팜과 같은 자본 집약적인 수단 없이 자연 그대로 작물 생산에 적합한 환경을 찾고, 에너지와 비용을 아끼며 최대 효용을 창출할 수 있음
- 사용자는 사용자 친화적인 인터페이스로로 생산량 예측 결과를 쉽게 조회할 수 있음

### 2.3 목표 및 내용  

#### (1) 개발 목표  
* 농사의 수요가 높은 미국 전역을 대상으로, 위도-경도에 따른 예측 농작물 생산량을 제공하는 웹 페이지를 개발하고자 함
* 생산량 예측은 단위면적 당 생산량(Bu/Acre) 를 타겟 값으로, 기상 조건들을 독립 변수로 한 Machine Learning 모델을 제작하여 제공할 예정

#### (2) 개발 내용  
* 최종 설계 결과물 형태
    * 지도가 메인으로 표시되는 웹 페이지 형태로 제공
    * 농작물 선택 탭으로 원하는 농작물 선택 가능
    * 예측 생산량 표시 (알림 창 형태로 표시)

* 최종 설계 결과물의 시스템 구성과 기능 흐름
    * 사용자는 웹 페이지에 제시되는 지도에서 예측 생산량을 알고 싶은 위치 클릭
    * 위치를 위도-경도로 변환하여, 기상 API를 호출하는 것으로 해당 지역의 기상 정보를 얻음
    * 기상 정보를 Machine Learning 모델에 입력하여 구한 예측 생산량을 유저에게 반환

    * 시스템 액티비티 다이어그램
    <img width="550" alt="image" src="https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/137899379/b90389ec-9a4a-41a2-b8c4-2408b17cbb04">
           
#### (3) 대안 도출 및 구현 계획  
* ML 모델 구축
    * 미국 각 주의 기상 데이터, 생산량 데이터를 사용하여 ML 모델 학습
    * 여러 개의 ML 모델 중 가장 성능이 좋은 모델을 선정
    * AutoML을 이용해 한 번에 여러 모델을 학습시킨 후, 제일 성능이 좋은 모델을 선정하는 방법을 최종적으로 선정함

* 웹 페이지 구현
    * Leaflet과 같은 지도 라이브러리를 사용하여 웹 화면에 미국 전역의 지도를 표시
    * JavaScript를 사용하여 특정 위치를 클릭하면 해당 위치의 위도, 경도 데이터를 받아올 수 있도록 함
    * 신속한 개발에 용이한 Django를 사용하여 웹 서버를 구축. 서버는 위도, 경도 데이터를 통해 날씨 api 호출
    * 날씨 api에서 해당 위도-경도의 일사량, 강수량, 토양의 수분 함유량 등, 총 생산량을 예측하는 데 필요한 데이터를 획득
    * 반환 받은 데이터를 ML 모델에 투입하여 최종적으로 생산량 예측 결과를 사용자에게 반환

#### (4) 설계의 현실적 제한요소(제약조건)  
* 농작물 생산량 예측 ML 모델에 사용할 적절한 독립 변수를 선정해야 함
* 적절한 변수를 설정하지 못할 경우 예측 모델의 성능이 떨어질 수 있음
* 생산량에 영향을 미칠 만한 변수들을 도메인 지식과, 데이터 분석을 통해 찾아내야 함
* 미국 전역의 지도를 띄울 경우, 농경지와 도심지의 차이와 같이 현실적으로 농업이 불가능한 지역이 있음

#### (5) 개발 환경  

### Tech Stack

<div align=center>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/django-6DB33F?style=for-the-badge&logo=springboot&logoColor=white">
  <img src="https://img.shields.io/badge/djangorestframework-FF9900?style=for-the-badge&logo=amazon ec2&logoColor=white">
  <br>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black">
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
  <img src="https://img.shields.io/badge/VsCode-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white">
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>
<br>
<br>

### 개발 환경

#### OS
- Microsoft Windows OS

#### Code editor
- VSCode

#### Language
- Python, JavaScript

#### Collaboration
- Notion, Github, Slack, Figma

#### License
- MIT License

#### Backend
- PyCaret AutoML
- django
- django-restframework

#### Frontend
- HTML5, CSS, JavaScript
- Visual Studio Code
<br>

### 2.4  기대효과 
- 농업을 처음 시작하는 사용자는 큰 시간과 비용을 들이지 않고 최적의 입지를 선정할 수 있음
- 농업에 종사중인 사용자는 생산량 예측을 통해 효율적인 공급, 재고 관리가 가능해 짐
- 사용자는 생산량 예측 결과를 사용자 친화적인 인터페이스로로 쉽게 조회할 수 있음

### 2.5  추진일정  
* 세부 작업에 대한 간트챠트  
* 세부 작업 별 구성원의 역할

### 2.6 참고문헌 
[1] 김세원, 김영희. (2021). 작물 생산량 예측을 위한 머신러닝 기법 활용 연구. 한국산학기술학회 논문지, 22(7), 403-408, 10.5762/KAIS.2021.22.7.403
[2] 이윤선, 이승호. (2008). 기후변화가 벼의 생산량에 미치는 영향. 국토지리학회지, 42(3), 405-416.
[3] 위성 영상을 이용한 작물 생산량 예측장치
[4] 인공신경망 및 선형 회귀를 이용한 작물 생산량 예측 방법
[5] 날씨마루 https://bd.kma.go.kr/kma2020/fs/productionSelect1.do?pageNum=5&menuCd=F050102000
[6] USDA https://www.nass.usda.gov/Charts_and_Maps/Crops_County/cr-pr.php

### 2.7 성과창출 계획

항목 | 세부내용 | 예상(달성)시기  
------|------------|-------
Github 등록 |        | 
SW등록 |        | 
시제품 |        | 

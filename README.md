# 프로젝트 명: 농작물 생산량 트렌드


## I. 프로젝트 수행팀 개요

* 수행 학기:  2024-1
* 프로젝트명: 농작물 생산량 트렌드 서비스
* Key Words : *농작물* | *생산량 예측* | *농업 지도* | *공시지가* | *농경지*
      
* 팀명: aha

구분 | 성명 | 학번 | 소속학과 | 연계전공 | 이메일
------|-------|-------|-------|-------|-------
팀장 | 이현종 | 2019111655 | 바이오환경과학과 | 융합SW연계전공 | hjong1010@dongguk.edu       
팀원 | 임형준 | 2019112520 | 산업시스템공학과 | 융합SW연계전공 | 2019112520@dongguk.edu        
팀원 | 이건희 | 2019110475 | 통계학과 | 융합SW연계전공 | ish8176@dgu.ac.kr        

* 지도교수 : 융합SW교육원 이길섭 교수님, 박효순 교수님

## II. 프로젝트 수행 결과  

### 1. 프로젝트 개요  

#### 1.1 개발 동기  

- 기후변화로 인해 농업 생태계가 어려움을 겪고 있으며 특히 작물에 따른 생산량 변동이 심화될 수 있음
- 농작물 생산량의 변동성이 커짐에 따라 생산 과잉은 악성 재고, 생산 부족은 가격 폭등을 유발하여 생산량 예측이 중요함

#### 1.2 개발 목표  

- 한국의 농업지도를 배경으로 기후변화에 따라 변화하는 지역, 작물의 생산량을 예측하여 정보를 제공하는 서비스 개발을 목표로 함

#### 1.3 최종결과물  
- https://osspcrops.store/
- 시연 영상: https://www.youtube.com/watch?v=pHNJq1oRQkk&ab_channel=%ED%98%95%EC%A4%80%EC%9E%84
* 웹 접속 초기 화면
* 작물,연도 선택란 / 지역 내 특정 위치 클릭 시 팝업창
<img width="620" alt="Aha_map page" src="https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/162420581/71ba659c-5d73-4c96-baca-7ab43cff5998">

 - 메인페이지에 희망 작물, 희망 연도를 선택할 수 있도록 하며 선택 학목에 따른 전국적인 생상량 예측값에 대한 분포를 시각적으로 제공
 - 지도에서 희망 지역 선택시 해당 행정구역의 생산량 예측값 제공하며 위도,경도에 따른 공시지가 정보를 함께 제공

#### 1.4 기대 효과  

- 농업을 처음 시작하는 사용자는 큰 시간과 비용을 들이지 않고 최적의 입지를 선정할 수 있음
- 농업에 종사중인 사용자는 생산량 예측을 통해 효율적인 공급, 재고 관리가 가능해 짐
- 사용자는 생산량 예측 결과를 사용자 친화적인 인터페이스로로 쉽게 조회할 수 있음

### 2. 프로젝트 수행 내용  

#### 2.1 프로젝트 진행과정 
- 프로젝트 WBS
<img width="1223" alt="스크린샷 2024-06-08 오후 9 05 50" src="https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/162420581/30eb13f3-eac0-4e47-93b8-e2ada9ea5d4a">


#### 2.2 유스케이스 
![Aha_usecase](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/assets/162420581/0e2508e7-5df4-4120-9bfa-bb673495fb64)

### 3. 프로젝트 자료  

#### 3.1 프로젝트 OSS 구성  

**오픈데이터**
- 기상청 기후변화아 시나리오에 따른 기상정보 예측 데이터
- [기상청 기후정보](http://www.climate.go.kr/home/CCS/contents_2021/35_download.php)
  
**오픈소스**
- v-world 공간 정보지도 공시지가 api
- [V-WORLD](https://www.vworld.kr/dtna/dtna_apiSvcFc_s001.do?apiNum=23)

#### 3.2 프로젝트 주요 문서 
구분 | 내용
------|-------|
보고서 | [수행계획서](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/blob/main/Doc/1_1_OSSProj_09_Aha_수행계획서.md) [중간보고서](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/blob/main/Doc/2_1_OSSProj_09_Aha_중간보고서.md) [최종보고서](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/blob/main/Doc/3_1_OSSProj_09_Aha_최종보고서.md)
발표자료 | [수행계획발표자료](https://github.com/HyunJong00/OSSProjHJL/blob/main/Doc/1_2_OSSProj_09_Aha_수행계획발표자료.pdf) [중간발표자료](https://github.com/HyunJong00/OSSProjHJL/blob/main/Doc/2_2_OSSProj_09_Aha_중간발표자료.pdf) [최종발표자료]()
회의록 | [회의록](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/blob/main/Doc/4_2_OSSProj_09_Aha_회의록.md)
이슈 | [이슈관리](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/issues?q=is%3Aissue+is%3Aclosed)
배포운영 | [제품구성배포운영자료](https://github.com/CSID-DGU/2024-1-OSSProj-Aha-09/blob/main/Doc/4_3_OSSProj_09_Aha_제품구성배포운영자료.md)


#### 3.3 참고자료  

* 날씨마루 : https://bd.kma.go.kr/kma2020/fs/productionSelect1.do?pageNum=5&menuCd=F050102000
* USDA : https://www.nass.usda.gov/Charts_and_Maps/Crops_County/cr-pr.php

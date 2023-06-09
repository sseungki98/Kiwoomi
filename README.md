# Kiwoomi(키우미)
## 키움 Open API+를 이용한 텔레그램 챗봇 프로그램
- <img width="130" alt="image" src="https://github.com/sseungki98/Kiwoomi/assets/89785414/d496a2fd-de4b-4d98-a631-2646406ec86e"><br>
  [키움 오픈 API+](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView) 

- <img width="130" alt="image" src="https://github.com/sseungki98/Kiwoomi/assets/89785414/e109a4c3-bbbc-45b7-9a6f-7aead93261e9"><br>
  [텔레그램](https://telegram.org/?setln=ko)

## 기본 Work Flow
<img width="624" alt="스크린샷 2023-03-28 오후 2 10 50" src="https://user-images.githubusercontent.com/79951703/228134712-bb5a3ff8-c76b-48a1-9a4c-07b8f992fe72.png">

## 기본 제공 기능
- 주식 이름 혹은 코드 입력 시 관련 정보 출력 (현재가, 체결가, 실시간 종가, 전일 대비, 등락률, 시가, 종가 등)
- 조건 검색에 사용될 조건 입력 시 관련 정보 출력
- 주식과 관련된 뉴스나 정보 제공
- ❌ 자동매매에 관한 기능은 제공하지 않음

## How to use?
1. 텔레그램에서 @dku_kiwoomi_bot을 검색한다.
2. 원하는 명령어를 입력하여 관련 정보를 얻는다.(명령어는 문서 확인 혹은 /help를 통해 확인할 수 있음)

## Before Use
- Kiwoom 투자증권 OPEN API+의 신청이 필요함 [신청 페이지](https://www.kiwoom.com/h/customer/download/VOpenApiInfoView)
- KOA Studio를 설치한 뒤, Kiwoom 계정 로그인을 진행해야 함

## 기능 상세

### /help

<img width="377" alt="image" src="https://github.com/sseungki98/Kiwoomi/assets/89785414/da628cc5-a289-4b50-a409-93b109911bb3">
<br>

### /info $name $option
![0000](https://github.com/sseungki98/Kiwoomi/assets/89785414/c2c56051-de5e-49f3-b178-0fde383a59e8)
<br>

### /alarm $name $price 
![12121212](https://github.com/sseungki98/Kiwoomi/assets/89785414/677cb1fb-5854-4aa3-afbe-43ae2af12470)
<br>

### /news $name
<img alt="news" src='https://github.com/sseungki98/Kiwoomi/assets/79951703/18bf0414-6308-43b2-b766-b0b4380513ff'>

## 기술스택🔧
Python

## How to use Script
- 봇 구동은 botCommunicator.py 파일을, 명령어는 Controller.py 파일을 통해 진행한다.
- 새로운 봇을 사용해 해당 기능을 사용하고 싶다면, bot Father을 통해 새로운 봇 토큰을 발급받고, 이를 botCommunicator.py 파일의 bot_token 변수를 변경하면 된다.
- 기능을 추가하고 싶으면 Controller.py에서 새로운 함수를 추가하는 방식으로 진행하면 된다.

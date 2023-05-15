from pykiwoom.kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect()  # 키움 API 접속

condition_list = kiwoom.GetConditionNameList()  # 조건식 목록 조회

# 조건식 목록 출력
for index, name in condition_list:
    print(f"인덱스: {index}, 이름: {name}")

condition_index = 0  # 조회할 조건식의 인덱스
condition_name = condition_list[condition_index][1]  # 선택한 조건식의 이름

# 조건검색 TR 요청
kiwoom.SendCondition("0156", condition_name, condition_index, 0)

# TR 데이터 수신 대기
while kiwoom.condition_search_finished == 0:
    pass

# 검색 결과 종목 코드 조회
code_list = kiwoom.GetCodeListByCondition(condition_name)

# 종목 코드 출력
for code in code_list:
    print(f"종목 코드: {code}")
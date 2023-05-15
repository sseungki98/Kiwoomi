from pykiwoom.kiwoom import Kiwoom
import pandas as pd

kiwoom = Kiwoom()
kiwoom.CommConnect()  # 키움 API 접속


code_name = []
output_list = ['종목코드',
                 '종목명',
                 '결산월',
                 '액면가',
                 '자본금',
                 '상장주식',
                 '신용비율',
                 '연중최고',
                 '시가총액',
                 '시가총액비중',
                 '외인소진률',
                 '대용가'
                 'PER',
                 'EPS',
                 'ROE',
                 'PBR',
                 'EV',
                 'BPS',
                 '매출액',
                 '영업이익',
                 '당기순이익',
                 '250최고',
                 '250최저',
                 '시가',
                 '고가',
                 '저가',
                 '상한가',
                 '하한가',
                 '기준가',
                 '예상체결가',
                 '예상체결수량',
                 '250최고가일',
                 '250최고가대비율',
                 '250최저가일',
                 '250최저가대비율',
                 '현재가',
                 '대비기호',
                 '전일대비',
                 '등락율',
                 '거래량',
                 '거래대비',
                 '액면가단위',
                 '유통주식',
                 '유통비율',
                 ]
# 종목 코드 조회
code_list = kiwoom.GetCodeListByMarket('0')  # 전체 종목 코드 조회
print(code_list)
for code in code_list:
    code_name.append(kiwoom.GetMasterCodeName(code))
code = code_list[0]  # 첫 번째 종목 코드
print(code_name)
# 종목 정보 조회
name = kiwoom.GetMasterCodeName(code)  # 종목 이름
price = kiwoom.GetMasterLastPrice(code)  # 종목 가격
volume = kiwoom.GetMasterListedStockCnt(code)  # 상장 주식 수

print(f"종목명: {name}")
print(f"현재가: {price}")
print(f"상장 주식 수: {volume}")

value_list = kiwoom.block_request("opt10001",
                          종목코드="005930",
                          output="주식기본정보",
                          next=0).to_dict(orient='records')
return_text = ''
for item in value_list[0].items():
    return_text += item[0] + ' : ' + item[1] + '\n'


print(return_text)
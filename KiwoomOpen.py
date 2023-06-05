from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import sys

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.CommConnect()

        self.OnEventConnect.connect(self.event_connect)

    def CommConnect(self):
        self.dynamicCall("CommConnect()")

    def GetConditionLoad(self):
        self.dynamicCall("GetConditionLoad()")

    def GetConditionNameList(self):
        condition_name_list = self.dynamicCall("GetConditionNameList()")
        condition_name_list = condition_name_list.split(';')[:-1]
        return condition_name_list

    def SendCondition(self, screen_no, condition_name, condition_index, search_type):
        self.dynamicCall("SendCondition(QString, QString, int, int)", screen_no, condition_name, condition_index, search_type)

    def OnReceiveTrCondition(self, scrNo, codeList, conditionName, conditionIndex, next):
        code_list = codeList.split(';')[:-1]
        print("조건식:", conditionName)
        print("종목 코드:", code_list)

    def event_connect(self, err_code):
        if err_code == 0:
            print("로그인 성공")

            self.GetConditionLoad()
            condition_name_list = self.GetConditionNameList()
            print("조건식 목록:", condition_name_list)

            screen_no = "9999"
            condition_index = 0
            search_type = 0
            self.SendCondition(screen_no, condition_name_list[condition_index], condition_index, search_type)

        else:
            print("로그인 실패")

app = QApplication(sys.argv)
kiwoom = Kiwoom()

app.exec_()

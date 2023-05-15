from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

def get_condition_codes():
    codes = []
    condition_list = kiwoom.GetConditionNameList()
    for condition in condition_list:
        if condition != "":
            condition_index = int(condition.split("^")[0])
            condition_name = condition.split("^")[1]
            code_list = kiwoom.SendCondition("0101", condition_name, condition_index, 1)
            for code in code_list:
                codes.append(code)
    return codes
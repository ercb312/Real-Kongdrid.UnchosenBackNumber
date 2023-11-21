import json

# json 모듈에서 알고 있어야 할 함수 2가지
# json.loads(byte) => byte를 string으로 바꿔줌
# json.dumps(dict) => dictionary를 string으로 바꿔줌

def save(data:dict|list, path:str="file.json") -> None:
    """
    data를 json 형태로 {path}에 저장한다
    """
    with open(path, "w", encoding="utf8") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=True))

def load(path:str="file.json") -> dict|list:
    """
    {path}에 저장된 json data를 dict 또는 list 형태로 반환(return)
    """
    with open(path, "r", encoding="utf8") as f:
        return json.loads(f.read())


# 딕셔너리로 명단 정리 {번호(10진수):'이름(문자열)'}
backNum = load("backNum.json")
print(backNum)
while(1): 
    #print("0을 입력하면 프로그램이 종료됩니다")
    num = input("확인 할 등번호 (0~99): ")
    # 입력되는 것은 숫자가 아니라 문자열임(print(type(num)) => <class 'str'>) 
    # => 그래서 if문에서 int함수로 정수로 10진수로 바꾼다 
    # 만약 입력받을 때 int()를 써버리면 밑에서 딕셔너리에서 선수를 찾을 때 문제가 생김 
    # bc 딕셔너리에 있는 번호는 문자열로 저장되어있음
    if(int(num) > 99 or int(num) < 0):
        print("0과 99 사이의 정수를 입력해주세요")
        continue
    name = backNum.get(num)
    if(name != None):
        print("등번호가 %s인 콩은 %s입니다" %(num, name))
        continue
    if(name == None):
        print("등번호가 %s인 콩은 없습니다!" %num)
        ans = input("등번호를 %s(으)로 하시겠습니까? (Y/N): " %num)
        if(ans.upper() == 'Y'):
            playerName = input('이름을 입력해주세요: ')
            # backNum = {num:playerName}
            backNum[num] = playerName
            save(backNum, "backNum.json")
            print('콩이 되신 것을 환영합니다! '+backNum.get(num)+'님')
            print('콩나물 선수 명단: ')
            print(backNum)
            break
        if(ans == 'N'):
            continue


"""
CSS 선택자(selector) -> sizzle(공식 명칭)
querySelector -> MDN 으로 보기
"""

#주인 없는 번호와 이름을 입력하지 않으면 while문의 무한반복 
# => 아래 코드를 실행하면 가능하지만 계속 input을 해줘야 한다
'''
while 밖에 end = input('프로그램을 종료하려면 0 / 실행하려면 아무거나 입력: ')
while(end != 0)
각 if문 안에 end = input('프로그램을 종료하려면 0 / 실행하려면 아무거나 입력: ')
'''

'''
end = input('종료하시겠습니까?: ')
if (end = 0):
    break
else:
    continue
'''
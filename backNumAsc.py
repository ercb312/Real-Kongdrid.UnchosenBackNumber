numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 30, 53, 66, 88] #sort로 정리 함
# 딕셔너리로 명단 정리 {번호(10진수):'이름(문자열)'}
backNum = {'1': '정세윤', 2: '손성준', 3: '김시완', 4: '변호준', 5: '이태현', 6: '박민재', 7: '김유찬', 8: '유현석', 9: '박진수', 10: '강민재', 11: '김태우', 12: '정주헌', 13: '서윤명', 14: '장지웅', 15: '김주호', 16: '우익현', 17: '성시훈', 19: '변정훈', 20: '김선준', 30: '김용관', 53: '양 준혁', 66: '박준재', 88: '김영훈'}
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
        if(ans == 'Y'):
            playerName = input('이름을 입력해주세요: ')
            backNum = {num:playerName}
            print('콩이 되신 것을 환영합니다! '+backNum.get(num)+'님')
            print('콩나물 선수 명단: ')
            print(backNum)
            break
        if(ans == 'N'):
            continue


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
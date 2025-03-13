# balance : 통장에 들어있는 기본금액을 담는 변수
# 1.입금, 2.출금 3.영수증 보기, 4.종료 => 입력받을 타입 고민 글자? 숫자? 숫자로 결정
# 숫자로 원하는 기능을 입력할수 있게 만들것 그리고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount:
# withdraw_amount:
# 영수증 기능에 사용되는 데이터 타입은  "list =["입금, 5000, 8000"], ["출금", 3000, 5000]

#영수증 기능 구현을 위한 빈 리스트 선언
receipts = []


balance = 3000



while True:
    num = input("1.입금, 2.출금, 3.영수증 보기, 4.종료 원하는 기능을 숫자로 눌러주세요: ")

    if num =="1":
        deposit_amount = input("입금할 금액을 숫자로 입력해 주세요: ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #첫번째 조건 문자가 입력된건 아닌지 확인 / 0보다 큰 금액을 입력했는지
            balance += int(deposit_amount)
            #영수증에 데이터 넣기
            receipts.append(("입금",deposit_amount, balance))
            print(f"입금금액: {deposit_amount}원 , 잔액: {balance}원 ")
        else:
            print("숫자만 기입하세요")    
    if num =="2":
        pass
    if num =="3":
        pass
    if num =="4":
        print("종료 합니다.")
        break

    if num =="2":
        withdraw_amount = input("출금할 금액을 숫자로 입력해 주세요: ")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0: #첫번째 조건 문자가 입력된건 아닌지 확인 / 0보다 큰 금액을 입력했는지
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount
            #영수증에 데이터 넣기
            receipts.append(("출금",withdraw_amount, balance))
            print(f"출금금액: {withdraw_amount}원 , 잔액: {balance}원 ")
        else:
            print("숫자만 기입하세요")    
    

    if num =="3":
        #리스트에 값이 있을때와 없을때 달랐으면 합니다.
        #값이 있을때 출력결과가 출금: 3000원 | 잔액 : 5000 같이 나왔으면 합니다.
        if receipts:
            print("===영수증===")
            for i in receipts:
                print(f"{i[0]} : {i[1]}원 | 잔액 : {i[2]}")
        else:
            print("거래 내역이 없습니다.")

    if num =="4":
        print("종료 합니다.")
        break
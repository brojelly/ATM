# balance : 통장에 들어있는 기본금액을 담는 변수
# 1.입금, 2.출금 3.영수증 보기, 4.종료 => 입력받을 타입 고민 글자? 숫자? 숫자로 결정
# 숫자로 원하는 기능을 입력할수 있게 만들것 그리고 사용자가 입력한 기능은 num 변수에 담아주세요
# deposit_amount
balance = 3000

while True:
    num = input("1.입금, 2.출금, 3.영수증 보기, 4.종료 원하는 기능을 숫자로 눌러주세요: ")

    if num =="1":
        deposit_amount = input("입금할 금액을 숫자로 입력해 주세요: ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0: #첫번째 조건 문자가 입력된건 아닌지 확인 / 0보다 큰 금액을 입력했는지
            balance += int(deposit_amount)
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
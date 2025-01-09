# 전달값과 반환값
balance = 0 # 잔액

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액는 {}원 입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if(money > balance):
        print("잔액이 부족합니다.")
        return balance
    else:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance - money
        
def withdraw_night(balance, money):
    commission = 100 # 수수료
    return commission, balance - money - commission
balance = deposit(balance, 1000)
balance = withdraw(balance, 1500)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance , 400)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))
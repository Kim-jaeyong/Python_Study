class BigNumErr(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumErr("입력값 {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값 입력")
except BigNumErr as err:
    print("두 자리 이상의 숫자 입력")
    print(err)
# 예외처리 : 에러가 발생했을 때 그에 대해서 처리를 해주는 것
try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자 입력 : ")))
    nums.append(int(input("두 번째 숫자 입력 : ")))
    # nums.append = nums[0] / nums[1]
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류 발생")
    print(err)
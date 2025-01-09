# continue & break
absent = [2, 5] #결석
no_book = [7] #책을 안가져옴

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {}번 학생은 교무실로 따라와".format(student))
        break
    print("{}번 책 읽어봐".format(student))        
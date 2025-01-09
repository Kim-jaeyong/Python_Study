# 가변인자
'''
def profile(name, age, lang1, lang2, lang3):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age), end = " ")
    print(lang1, lang2, lang3)

profile("김재용", 22, "Python", "Java", "C", "C++")
profile("김기용", 15, "Kotlin", "Swift", "")

lang 함수를 추가하거나 ""로 채워야하는 번거로움
'''

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("김재용", 22, "Python", "Java", "C", "C++")
profile("김기용", 15, "Kotlin", "Swift", "")

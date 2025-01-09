# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\
        ".format(name, age, main_lang))

profile("김지안", 20, "파이썬")
profile("김기용", 15, "자바")

def defaultProfile(name, age = 22, main_lang = "C++"):
        print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
        
defaultProfile("김재용")
defaultProfile("신종한")
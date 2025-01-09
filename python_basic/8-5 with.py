import pickle

with open("8-4-1profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # with문을 사용하면 파일을 연 후 자동으로 파일이 닫히므로 close 해 줄 필요 없음
    
with open("8-5-1study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부를 열심히 하고 있습니다")

with open("8-5-1study.txt", "r", encoding="utf8") as sFile:
    print(sFile.read())
# 가지고 있는 데이터를 피클을 이용해 파일에 저장하고 파일에 있는 내용을 불러와서 변수에 저장해서 쓸 수 있음
import pickle
profile_file = open("8-4-1profile.pickle", "wb") # 피클에서는 바이너리 형식으로 처리하기 때문에 인코딩을 지정해줄 필요 없음
profile = {"name":"yong", "age":22, "hobby":["soccer", "golf", "codding"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open("8-4-1profile.pickle", "rb")
pfile = pickle.load(profile_file) # file에 있는 정보를 pfile에 불러오기
print(pfile)
profile_file.close()
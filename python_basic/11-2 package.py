# 패키지 : 모듈들을 모아놓은 집합

# import travel.thailand
# # import travel.thailand.ThailandPackage() -> X
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trips_to = vietnam.VeitnamPackage()
trips_to.detail()
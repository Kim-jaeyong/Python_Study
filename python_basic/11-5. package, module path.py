# 원래 travel이었던 파일을 random 함수가 있는 곳으로 옮김
import inspect
import random
from travel import *

print(inspect.getfile(random))
print(inspect.getfile(thailand))
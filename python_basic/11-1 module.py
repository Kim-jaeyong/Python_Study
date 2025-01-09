# 모듈 : 필요한 것끼리 부품처럼 만들어진 파일
# import theater_module

# theater_module.price(3)
# theater_module.morning_price(4)
# theater_module.soldier_price(2)

# import theater_module as mv 
# mv.price(3)
# mv.morning_price(4)
# mv.soldier_price(2)

# from theater_module import *
# price(3)
# morning_price(4)
# soldier_price(2)

# from theater_module import price, morning_price
# price(3)
# morning_price(4)
# soldier_price(2) -> X

from theater_module import soldier_price as sp 
sp(3)
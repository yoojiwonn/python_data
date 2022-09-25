# import theater_module
# theater_module.price(3)
# theater_module.price_soldier(4) # 4명이서 조조 할인 영화 보러 갔을 떄
# theater_module.price_morning(5)# 5명이서 군인이 영화 보러 갔을 때 

# import theater_module as mv #모듈이름이 길때 이름을 붙여주고 사용 가능 
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# import travel.thailand
# #import travel.thailand.ThailandPackage <- class는 import 에서는 사용할수 없음
# trip_to = travel.thailand.ThailandPackage
# trip_to.detail()

# from travel.thailand import ThailandPackage # from 을 사용하면 import 사용 가능 
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
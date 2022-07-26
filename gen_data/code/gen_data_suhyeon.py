from gen_data import *
import random

def suhyeon():
  reserve=['예약','예매']
  ending=['할래','해줘','해','하려 해','하려하는데 표 있어?']

  """## generate data"""

  #start에서 end로 가는 date dep_time에 출발하는 버스 예약해줘
  bus_list_d_1=[]
  for i in range(800):
      start, end = get_route()
      date = random.choice([get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,2]))])
      dep_time = random.choice([get_dtime_hour(), get_dtime_full_hour(), get_dtime_hour_exact_min(), get_dtime_full_hour_exact_min(), get_dtime_hour_later(), get_dtime_min_later()])
      
      bus_list_d_1.append(start+'에서 '+end+random.choice(['로', '으로'])+' 가는 '+date+dep_time+'에 출발하는 버스 '+random.choice(reserve)+' '+random.choice(ending))

  #start 출발 end 도착 date 출발 시각은 dep_time
  bus_list_d_2=[]
  for i in range(800):
      start, end = get_route()
      date = random.choice([get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,2]))])
      dep_time = random.choice([get_dtime_hour(), get_dtime_full_hour(), get_dtime_hour_exact_min(), get_dtime_full_hour_exact_min(), get_dtime_hour_later(), get_dtime_min_later()])

      bus_list_d_2.append(start+' 출발 '+end+' 도착 '+date+'출발 시각은 '+dep_time)

  #start에서 end 차 dep_time 예약할래
  bus_list_d_3=[]
  for i in range(800):
      start, end = get_route()
      dep_time = random.choice([get_dtime_hour(), get_dtime_full_hour(), get_dtime_hour_exact_min(), get_dtime_full_hour_exact_min(), get_dtime_hour_later(), get_dtime_min_later()])

      bus_list_d_3.append(start+'에서 '+end+random.choice([' ', ' 차 ', ' 버스 ', ' 티켓 '])+dep_time+random.choice(reserve)+' '+random.choice(ending))

  #start에서 end 로 가는 버스 date arr_time 안에 도착하는 걸로 예약해줘
  bus_list_d_4=[]
  for i in range(800):
      start, end = get_route()
      arr_time = random.choice([get_atime_hour(), get_atime_full_hour(), get_atime_hour_exact_min(), get_atime_full_hour_exact_min(), get_atime_hour_later()])

      bus_list_d_4.append(start+'에서 '+end+random.choice(['로 가는 ', ' 도착하는 ', '으로 가는 '])+random.choice(['', '버스 ', '티켓 ', '차 '])+date+arr_time+random.choice([' 안에 ', '내에 ', '까지 '])+random.choice(['도착하는거 예약해줘', '도착하는 걸로', '도착하는 걸로 예약할래']))

  #start에서 end 로 가는 버스 예약할거야. date arr_time 안에 도착하는 걸로.
  bus_list_d_5=[]
  for i in range(800):
      start, end = get_route()
      arr_time = random.choice([get_atime_hour(), get_atime_full_hour(), get_atime_hour_exact_min(), get_atime_full_hour_exact_min(), get_atime_hour_later()])

      bus_list_d_5.append(start+'에서 '+end+random.choice(['로 가는', '으로 가는', '도착하는'])+random.choice([' ', ' 차 ', ' 버스 ', ' 티켓 '])+random.choice(reserve)+random.choice(['할거야.', '할래.', '해줘.'])+ arr_time+random.choice(['에 도착', '에 도착하는 걸로']))

  bus_list=bus_list_d_1+bus_list_d_2+bus_list_d_3+bus_list_d_4+bus_list_d_5

  return bus_list


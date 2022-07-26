from gen_data import *
import random

def dayoon():
  # 데이터 생성
  # 시나리오 1(첫 멘트)

  # 끝 맺음 어휘
  reserve=['예약','예매']
  ending=['할래','해줘','해','하려 해','하려하는데 표 있어?']

  bus_list_d_1=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_1.append(start+'에서 '+end+'로 가는 버스 '+random.choice(reserve)+random.choice(ending))

  bus_list_d_2=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_2.append(end+'로 가는 버스 '+random.choice(reserve)+random.choice(ending)+'. '+start+'에서 출발할꺼야')

  bus_list_d_3=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_3.append(end+'로 가는 버스 '+random.choice(reserve)+random.choice(ending)+'. '+start+'에서 출발하는 걸로')

  bus_list_d_4=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_4.append(end+'로 가는 버스 '+random.choice(reserve)+random.choice(ending)+'. '+start+'출발')

  bus_list_d_5=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_5.append(start+'에서 출발해서 '+end+'로 도착하는 버스 '+random.choice(reserve)+random.choice(ending))

  bus_list_d_6=[]
  for i in range(800):
    start, end = get_route()
    bus_list_d_6.append(start+'출발 '+end+'도착 버스 '+random.choice(reserve)+random.choice(ending))

  bus_list=bus_list_d_1+bus_list_d_2+bus_list_d_3+bus_list_d_4+bus_list_d_5+bus_list_d_6

  # 시나리오 2(변경)
  # 중복 어휘
  reject=['','아니 ','음.. ','음.. 아니 ','아니야 ']
  change=['로','로 바꿀게','로 수정해줘','로 바꿔 줘','로 바꿔 주세요','로 수정할게']
  dep_change=['에 출발','에 출발하는 걸','출발']
  arr_change=['에 도착','도착']

  ###출발 

  #ex.1월 1일 낮 12시 (출발)로 바꿀게, 내일로 바꿀게
  sec_bus_list_1=[]
  for i in range(1000):
    sec_bus_list_1.append(random.choice(reject)+random.choice(['',get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,1]))])+random.choice([get_dtime_hour(),get_dtime_full_hour()])+random.choice(dep_change)+random.choice(change))

  #ex.아니 지금
  sec_bus_list_2=[]
  for i in range(50):
    sec_bus_list_2.append(random.choice(reject)+get_date(2))

  #ex.아니 이번주 월요일 낮 12시 30분으로 바꿀게
  sec_bus_list_3=[]
  for i in range(1000):
    sec_bus_list_3.append(random.choice(reject)+random.choice(['',get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,1]))])+' '+random.choice([get_dtime_hour_exact_min(),get_dtime_full_hour_exact_min()])+'으'+random.choice(change))

  #ex.아니 이번주 월요일 낮 12시 30분 출발로 바꿀게
  sec_bus_list_4=[]
  for i in range(1000):
    sec_bus_list_4.append(random.choice(reject)+random.choice(['',get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,1]))])+' '+random.choice([get_dtime_hour_exact_min(),get_dtime_full_hour_exact_min()])+random.choice(dep_change)+random.choice(change))

  #ex.아니 12시간 뒤 (출발)로 바꿀게
  sec_bus_list_5=[]
  for i in range(100):
    sec_bus_list_5.append(random.choice(reject)+random.choice([get_dtime_hour_later(),get_dtime_min_later()])+random.choice(dep_change)+random.choice(change))

  ### 도착

  #ex.아니 1월 1일 낮 12시 도착으로 바꿀게
  sec_bus_list_6=[]
  for i in range(1000):
    sec_bus_list_6.append(random.choice(reject)+random.choice(['',get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,1]))])+random.choice(['',get_atime_hour(),get_atime_hour_exact_min(),get_atime_hour_later(),get_atime_full_hour(),get_atime_full_hour_exact_min()])+random.choice(arr_change)+'으'+random.choice(change))

  #ex.아니 1월 1일 낮 12시에 도착하는걸로 바꿀게
  sec_bus_list_7=[]
  for i in range(500):
    sec_bus_list_7.append(random.choice(reject)+random.choice(['',get_date_with_day(),get_date_not_exact_int(),get_date(random.choice([0,1]))])+random.choice(['',get_atime_hour(),get_atime_hour_exact_min(),get_atime_hour_later(),get_atime_full_hour(),get_atime_full_hour_exact_min()])+'에 도착하는 걸'+random.choice(change))



  bus_list_change=sec_bus_list_1+sec_bus_list_2+sec_bus_list_3+sec_bus_list_4+sec_bus_list_5+sec_bus_list_6+sec_bus_list_7

  bus_list += bus_list_change

  return bus_list


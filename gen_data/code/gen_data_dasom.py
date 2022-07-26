from gen_data import *
import random

def dasom():
  reserve = ["예약", "예매" ,"티켓 발행", "티켓 예약", "티켓 예매","발권"]
  ending = ['해줘','해주세요','하고싶어','할래','해','하려하는데 표 있어?', '하고싶어요','할게요',"할게"]

  """## generate data"""

  # case1) 목적지만 얘기하는 상황 
  route_list1_1 = []
  for i in range(800):
    start,end = get_route()
    route_list1_1.append(end + "으로 가는 버스 " + random.choice(reserve) + random.choice(ending))

  route_list1_2 = []
  for i in range(800):
    start,end = get_route()
    route_list1_2.append("목적지는" + end + "인 버스 "+ random.choice(reserve) + random.choice(ending))


  route_list1_3 = []
  for i in range(800):
    start,end = get_route()
    route_list1_3.append("도착지는" + end + "인 버스 " +random.choice(reserve) + random.choice(ending))

  route_case1 = route_list1_1 + route_list1_2 + route_list1_3
  
  # case 2) 변경 사항 발생 
  reject=['','아니 ','음.. ','음.. 아니 ','아니야 ']
  change=['로','로 바꿀게','로 수정해줘','로 바꿔 줘','로 바꿔 주세요','로 수정할게','로 변경해주세요', '로 변경해줘']
  dep_change=['에 출발','에 출발하는 걸','출발']
  arr_change=['에 도착으', '에 출발하는 걸', '도착으']

  # 출발지 변경
  route_list2_1 = []
  for i in range(800):
    start,end = get_route()
    route_list2_1.append(random.choice(reject)+"출발지는" + start +random.choice(change))

  route_list2_2 = []
  for i in range(800):
    start,end = get_route()
    route_list2_2.append(random.choice(reject) + start +random.choice(dep_change) + random.choice(change))

  # 출발시간 + 날짜 변경 
  route_list3_1 = []
  for i in range(800):
    date = random.choice([get_date(random.choice([0,2])),get_date_with_day(),get_date_not_exact_int()])
    dep_time = random.choice([get_dtime_hour(),get_dtime_full_hour(),get_dtime_hour_exact_min(),get_dtime_full_hour_exact_min(),get_dtime_hour_later(),get_dtime_min_later()])
    route_list3_1.append(random.choice(reject)+ "출발 시간이랑 날짜는" + dep_time + date + random.choice(change))

  route_list3_2 = []
  for i in range(800):
    date = random.choice([get_date(random.choice([0,2])),get_date_with_day(),get_date_not_exact_int()])
    dep_time = random.choice([get_dtime_hour(),get_dtime_full_hour(),get_dtime_hour_exact_min(),get_dtime_full_hour_exact_min(),get_dtime_hour_later(),get_dtime_min_later()])
    route_list3_2.append(date + dep_time + random.choice(dep_change) + random.choice(change))

  # 도착시간 + 날짜 변경 
  route_list4_1 = []
  for i in range(800):
    date = random.choice([get_date(random.choice([0,2])),get_date_with_day(),get_date_not_exact_int()])
    arr_time = random.choice([get_atime_hour(),get_atime_hour_exact_min(), get_atime_hour_later(),get_atime_full_hour(),get_atime_full_hour_exact_min()])
    route_list4_1.append(random.choice(reject) +date + arr_time + random.choice(arr_change) + random.choice(change))

  route_list4_2 = []
  for i in range(800):
    date = random.choice([get_date(random.choice([0,2])),get_date_with_day(),get_date_not_exact_int()])
    arr_time = random.choice([get_atime_hour(),get_atime_hour_exact_min(), get_atime_hour_later(),get_atime_full_hour(),get_atime_full_hour_exact_min()])
    route_list4_2.append(random.choice(reject) +date+ "에" + arr_time+ random.choice(arr_change) + random.choice(change))


  route_case2 = route_list2_1 + route_list2_2 + route_list3_1 + route_list3_2 + route_list4_1 + route_list4_2

  bus_list=route_case1+route_case2

  return bus_list


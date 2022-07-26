# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import random
from datetime import datetime

# 경로 데이터 생성
PATH = 'data/slot_data_resource'

dep = pd.read_csv(PATH + '/경로.csv')
dep_list=dep.iloc[:,0].unique().tolist()
route=dep.values.tolist()

# 날짜 데이터 생성(1월 1일 ~ 12월 31일)
def date_range(start, end):
    start = datetime.strptime(start, "%m월 %d일")
    end = datetime.strptime(end, "%m월 %d일")
    dates = [date.strftime("%m월 %d일") for date in pd.date_range(start, periods=(end-start).days+1)]
   
    return dates

# 인원 및 날짜 슬롯들
people=['일반',	'중고생', '아동', '국가유공자', '성인', '어른', '어린이', '아기', '애기',	'초등학생', '청소년', '중학생', '고등학생']
date = date_range("1월 1일", "12월 31일")
now=['지금','당장','빨리','현재','최대한 빨리','가장 빠른','가장 빨리', '빨리빨리']
forward_time=['낮','오전','오후','밤','저녁','아침','새벽']
date_exact=['오늘','익일','금일','명일','내일','모레','내일 모레','보름']
date_not_exact=['이번주','다음주','다다음주']
date_not_exact_with_int=['주 뒤','일 뒤','주일 뒤']
day=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

some_date=pd.Series([date, date_exact, now], index=['date', 'date_exact', 'now'])
some_date

# 데이터 생성 함수
def get_route():
  st=random.choice(dep_list)
  match=[i for i in range(len(route)) if route[i][0]==st]
  end=route[random.choice(match)][1]
  return "/DEP;"+st+'/', "/ARR;"+end+'/'

def get_date(i):
  return '/DATE;'+random.choice(some_date[i])+'/'

#ex.이번주 월요일
def get_date_with_day():
  return '/DATE;'+random.choice(date_not_exact)+' '+random.choice(day)+'/'

#ex.1주일 뒤
def get_date_not_exact_int():
  return '/DATE;'+str(np.random.randint(1,6))+random.choice(date_not_exact_with_int)+'/'

#ex. 낮 12시
def get_dtime_hour():
  return '/DEP_TIME;'+random.choice(forward_time)+' '+str(np.random.randint(1,12))+'시'+'/'

#ex. 18시
def get_dtime_full_hour():
  return '/DEP_TIME;'+str(np.random.randint(0,24))+'시'+'/'

#ex. 낮 12시 30분, 낮 12시 반
def get_dtime_hour_exact_min():
  return '/DEP_TIME;'+random.choice(forward_time)+' '+str(np.random.randint(1,12))+'시'+random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

#ex. 18시 30분
def get_dtime_full_hour_exact_min():
  return '/DEP_TIME;'+str(np.random.randint(0,24))+'시'+random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'

#ex. 12시간 뒤
def get_dtime_hour_later():
  return '/DEP_TIME;'+str(np.random.randint(1,12))+random.choice(['시간 뒤','시간 후'])+'/'

#ex. 30분 뒤
def get_dtime_min_later():
  return '/DEP_TIME;'+str(np.random.randint(1,60))+random.choice(['분 뒤','분 후'])+'/'
 
def get_atime_hour():
  return '/ARR_TIME;'+random.choice(forward_time)+' '+str(np.random.randint(1,12))+'시'+random.choice(['',' 반'])+'/'

def get_atime_hour_exact_min():
  return '/ARR_TIME;'+random.choice(forward_time)+' '+str(np.random.randint(1,12))+'시'+str(np.random.randint(1,60))+'분'+'/'

def get_atime_hour_later():
  return '/ARR_TIME;'+str(np.random.randint(1,12))+random.choice(['시간 뒤','시간 후'])+'/'

def get_atime_full_hour():
  return '/ARR_TIME;'+str(np.random.randint(0,24))+'시'+'/'

def get_atime_full_hour_exact_min():
  return '/ARR_TIME;'+str(np.random.randint(0,24))+'시'+random.choice(['반',str(np.random.randint(1,60))+'분'])+'/'
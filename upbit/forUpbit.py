'''
1차 목표 : 업비트 API 를 활용한 자동 매매, 매수 처리

2차 목표 : 어떤 알고리즘으로 매매를 할지, 매수를 할지 정하기

3차 목표 : 결과 피드백하기
'''

def order():
  range_int = len(qurey_240minutes(buy_coin))
  tmp = query_240minutes('KRW-MVL')[0]['low_price']
  low_price = tmp

  for i, price_list in enumerate(query_240minutes(buy_coin)):
    if price_list['low_price'] <= tmp:
      tmp =  price_list['low_price']
      low_price = tmp
      print('Low price in 240 min : ', low_price)
    
  query_price = query_now('KRW-MVL')[0]['trade_price']

  print('4시간 이전 저점: ', + str(low_price))
  print('현재 가격 :', + str)


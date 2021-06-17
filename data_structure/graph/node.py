class StatinNode:
    ''' 지하철 역 노드를 나타내는 클래스 '''
    def __init__(self, name, num_exits):        # 역 이름, 출구 개수
        self.name = name
        self.num_exits = num_exits

    
station_0 = StatinNode('교대역', 14)
station_1 = StatinNode('사당역', 14)
station_2 = StatinNode('종라3가역', 16)
station_3 = StatinNode('서울역', 16)



# 노드들은 파이썬 리스트에 저장
stations = [station_0, station_1, station_2, station_3]

# 지하철 역 노드들을 파이썬 딕셔너리(hash table)에 저장
# stations = {
#     "교대역": station_0,
#     "사당역": station_1,
#     "종로3가역": station_2,
#     "서울역": station_3
# }

print(stations)
import ifcopenshell
import ifcopenshell.util.element
# 해당 속성 전부 불러오는 메서드
from pprint import pprint

if __name__ == '__main__':
    model = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

    walls = model.by_type('IfcWall') # IfcWall이 들어가는 엔티티 전부를 불러옴.... 왜..?

    wall = walls[0]

    for i in wall:
        pprint(i)

    print('---------------')
    pprint(wall.get_info()) # ! 해당 메서드를 사용하면 Element Specific이 나옴
    pprint(ifcopenshell.util.element.get_psets(wall))# ! Element Specific 이외의 정보들이 나옴, 궁굼한건 PSET이 없는건 어떻게 나오는 거지??????

    #pprint(wall.get_info(recursive=True)) # 이건좀 애매 한듯
    pprint(wall.IsDefinedBy) # guid -> 0G$YjylMT3_QYqYpBpSAQC
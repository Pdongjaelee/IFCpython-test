
import ifcopenshell.util.element

# 해당 경로에서 ifc 파일 열기(ex)차고)
file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')


products = file.by_type("IfcProduct")
odj_info = products[0].get_info()
print(odj_info.keys())





# 벽 유형 속성 가져오기
# wall = file.by_type("IfcWindow")[1]
# wall_type = ifcopenshell.util.element.get_type(wall)
#
# psets = ifcopenshell.util.element.get_psets(wall_type)
# print(psets)
#
# psets = ifcopenshell.util.element.get_psets(wall)
# print(psets)
#
# print(ifcopenshell.util.element.get_psets(wall, psets_only=True))
#
# print(ifcopenshell.util.element.get_psets(wall, qtos_only=True))





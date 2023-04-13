import ifcopenshell

# 1. 해당 경로에서 ifc 파일 열기(ex)유류고)
file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_oil_IFC4_Reference_View.ifc')

#
products = file.by_type('IfcProduct')
for product in products :
    print(product.is_a())



# print(file.by_guid('0L$0W65fP6aPyqk5kR7abh'))
# for wall_type in file.by_type("IfcWallType") :
#     print("The wall type element is", wall_type)
#     print("The name wall of the wall type", wall_type.Name)






# print(file.schema)

# 2. IFC 스키마 살표
# print(file.by_guid('2qbG3ptq9EmAuJZLXZIdDN'))



# print(file.by_id(1))


# walls = file.by_type('IFcWall')
# print(len(walls))





# 모든 벽 유형 가져오기
# for wall_type in file.by_type("IfcWallType") :
#     print("The wall type element is", wall_type)
#     print("The name wall of the wall type", wall_type.Name)


# 파일의  ifc 스키마
# print(file.by_guid('2dHAlBcM9FWQwA427Cfhva'))

#파일의 guid로 데이터 가져오기
# print(file.by_guid('0pVAcfXILDMA$q2e0Z$q82'))

# ifc guid로 열기

# # 벽의 수 확인
# wall = file.by_type("IfcWall")
# print(len(wall))

# 요소의 IFC 클래스가 무엇인지 확인
# wall = file.by_type("IfcWall")[0]
# print(wall.is_a())

# 해당 요소 정보 다 가져오기
# wall = file.by_type("IfcWall")[0]
# print(wall.get_info())












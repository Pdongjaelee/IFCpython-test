import ifcopenshell

# 1. 해당 경로에서 ifc 파일 열기(ex)차고) [o]
file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

# 2. 모든 유형의 IFC 클래스 가져오기 및 해당 클래스 나열 [o]
products = file.by_type('IfcProduct')
for product in products :
    print(product.is_a())

# 3. IFC 데이터 속성 가져 오기(IfcEntity 를 type 으로 읽음) [o]
window = file.by_type("IfcWindow")[0]
for definition in window.IsDefinedBy :
    if definition in window.IsDefinedBy :
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            print(property_set.Name)  # Might return Pset_WallCommon


# Element Specific 만 읽음
# print(window.GlobalId)
# print(window.Name)
# print(window.ObjectType)
# print(window.PartitioningType)
# print(window.PredefinedType)
# print(window.OverallHeight)
# print(window.OverallWidth)
# print(window.Tag)

# 4. IFC 데이터 속성 값 가져 오기 [x]
window = file.by_type("IfcWindow")[0]
for property in property_set.HasProperties: # Phasing 값만 가져옴 ?
    property_set = definition.RelatingPropertyDefinition
    if property.is_a('IfcPropertySingleValue'):
        print(property.Name)
        print(property.NominalValue.wrappedValue)


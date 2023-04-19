import ifcopenshell.entity_instance
import ifcopenshell.util.element

# 1. 해당 경로에서 ifc 파일 오픈(ex)차고) [o]
file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

# 2. 모든 유형의 IFC 클래스 가져오기 및 해당 클래스 나열 [o]
products = file.by_type('IfcProduct')
for product in products :
    print(product.is_a())

# 3. IFC 데이터 속성 가져 오기(IfcEntity 를 type 으로 읽음) [o]
window = file.by_type("IfcWindow")[0]
for definition in window.IsDefinedBy :
    if definition in window.IsDefinedBy :
        if definition.is_a('IfcRelDefinesByProperty'):
            property_set = definition.RelatingPropertyDefinition
            print(property_set.Name)  # Might return Pset_WallCommon
            print(property_set.value)


# Element Specific 만 읽음
print(window.GlobalId)
print(window.Name)
print(window.ObjectType)
print(window.PartitioningType)
print(window.PredefinedType)
print(window.OverallHeight)
print(window.OverallWidth)
print(window.Tag)

# 4. IFC 데이터 속성 값 가져 오기 [x]
window = file.by_type("IfcWindow")[0]
for property in property_set.HasProperties: # Phasing 값만 가져옴 ?
    property_set = definition.RelatingPropertyDefinition
    if property.is_a('IfcPropertySingleValue'):
        print(property.Name)
        print(property.NominalValue.wrappedValue)

# 5. IFC 수량이 있는 데이터 값 [X]
#wall = file.by_type('IfcWall')[0]
#for definition in wall.IsDefinedBy:
#    related_data = definition.RelatingPropertyDefinition
#    if related_data.is_a('IfcPropertySet'):
#        pass
#    elif related_data.is_a('IfcElementQuantity'):
#        print_element_quantities(related_data)


# 6. IFC 많은 유형의 수량이 있는 데이터 값 [ ]
def print_element_quantities(element_quantity):
    for quantity in element_quantity.Quantities:
        print(quantity.Name)
        if quantity.is_a('IfcQuantityLength'):
            print(quantity.lengthValue)

# 7. IFC 요소의 배치 ~ 형상 데이터 값 [ ]
if window.ObjectPlacement.PlacementRelTo:
    # Inherit the coordinates of its parents
    pass
local_coordinates = window.ObjectPlacement.RelativePlacement.Location[0]

# 8. IFC 요소 기하학적 표현 일단 패스~ [ ]
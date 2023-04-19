import ifcopenshell.util.element

# 요소의 공간 컨테이너 찾기 ? 컨테이너가 뭐지?
ifc_file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')
wall = ifc_file.by_type("IfcWall")[0]
# Walls are typically located on a storey, equipment might be located in spaces, etc
container = ifcopenshell.util.element.get_container(wall)
# The wall is located on Level 01
print(f"The wall is located on {container.Name}")


# 컨테이너의 모든 요소 가져오기
for storey in ifc_file.by_type("IfcWindow"):
    elements = ifcopenshell.util.element.get_decomposition(storey)
    print(f"There are {len(elements)} located on storey {storey.Name}, they are:")
    for element in elements:
        print(element.Name)
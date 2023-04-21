import multiprocessing
import ifcopenshell
import ifcopenshell.geom

# 수동 파싱?
ifc_file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

unit_scale = ifcopenshell.util.unit.calculate_unit_scale(ifc_file)

for circle in ifc_file.by_type("IfcCircle"):
    # In project length units
    print(circle.Radius)

    # In SI meters
    print(circle.Radius * unit_scale)
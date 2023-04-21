from pprint import pprint
import ifcopenshell.util
from ifcopenshell.util.selector import Selector

ifc = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')
ifc.wrapped_data.types()

print(ifc.types())


# selector = Selector()
# element = selector.parse(ifc, '#2dHAlBcM9FWQwA424pNU1T') # Equivalent to ifc.by_guid('2MLFd4X2f0jRq28Dvww1Vm')
# walls = selector.parse(ifc, '.IfcWall') # This is equivalent to ifc.by_type('IfcWall')
#
# elements = selector.parse(ifc, '.IfcSite[GlobalId = "0L$0W65fP6aPyqk5jauOMM"]')
#
# pprint(selector.get_info()) # ! 해당 메서드를 사용하면 Element Specific이 나옴




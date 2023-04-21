import ifcopenshell
import ifcopenshell.util.element as Element

file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

walls = file.by_type("IfcWall")

objects_data = {}

for wall in walls:
    object_id = wall.id()
    objects_data[object_id] = {
        "ExpressID": wall.id(),
        "GlobalId": wall.GlobalId,
        "Class": wall.is_a(),
        "PredefindType": Element.get_predefined_type(wall),
        "Name": wall.Name,
        "Level": Element.get_container(wall).Name
        if Element.get_container(wall)
        else "",
        "ObjectType":Element.get_type(wall).Name
        if Element.get_type(wall)
        else "",
        "QuantitySets": Element.get_psets(wall, qtos_only=True),
        "PropertySets": Element.get_psets(wall, psets_only=True),
    }
    return objects_data

import pprint
pp = pprint.PrettyPrinter()
data = get_objects_data_by_class(file, "IfcWall")

pp.pprint(data)


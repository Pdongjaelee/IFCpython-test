## ifc -> json 변환 메서드

import ifcopenshell
import ifcopenshell.util.element as Element

file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')

def get_objects_data_by_class(file, class_type):
    objects_data = []
    objects = file.by_type(class_type)
    for object in objects:
        object_id = object.id()
        objects_data.append({
            "ExpressID": object.id(),
            "GlobalId": object.GlobalId,
            "Class": object.is_a(),
            "PredefindType": Element.get_predefined_type(object),
            "Name": object.Name,
            "Level": Element.get_container(object).Name
            if Element.get_container(object)
            else "",
            "ObjectType":Element.get_type(object).Name
            if Element.get_type(object)
            else "",
            "QuantitySets": Element.get_psets(object, qtos_only=True),
            "PropertySets": Element.get_psets(object, psets_only=True),
        })
    return objects_data

import pprint
pp = pprint.PrettyPrinter()
data = get_objects_data_by_class(file, "IfcBuildingStorey")

import json
with open('./models/IfcBuildingStorey.json', 'w') as f:
    json.dump(data, f)

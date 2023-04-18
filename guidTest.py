import ifcopenshell
import ifcopenshell.geom

ifc_file = ifcopenshell.open('C:/Users/USER\PycharmProjects\pythonProject/6_car_IFC4_Reference_View.ifc')
element = ifc_file.by_type('IfcSlab')[0]

settings = ifcopenshell.geom.settings()
shape = ifcopenshell.geom.create_shape(settings, element)


#guid로 해당 속성 값 불러오기[o]
print(ifc_file.by_guid('32IGUQNiD5TQGesHztPxFy'))
# The GUID of the element we processed
#print(shape.guid)

# The ID of the element we processed
#print(shape.id)

# The element we are processing
#print(ifc_file.by_guid(shape.guid))

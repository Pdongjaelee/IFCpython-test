import ifcopenshell
from ifcopenshell.api import run

file = ifcopenshell.open("path/to/your/ifc/file.ifc")

walls = file.by_type("ifcWall")







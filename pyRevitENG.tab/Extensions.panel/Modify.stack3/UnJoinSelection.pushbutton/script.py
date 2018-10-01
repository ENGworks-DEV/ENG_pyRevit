"""
Unjoin selection
Version: 1.0
Date : 01/10/18
Autor: Pablo Derendinger 
pyrevit: 4.5
"""

__title__ = 'Unjoin Selection'


from pyrevit import script
from pyrevit.extensions import extensionmgr


logger = script.get_logger()
logger.set_quiet_mode()

import clr
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
from Autodesk.Revit.UI import * 
app = __revit__.Application
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


def selectElement():
    """Returns the id as an INT of an element selected from a Linked File
    
    Return: Element Id as int
    """
    #Import ObjectType
    from Autodesk.Revit.UI.Selection import Selection
    #Invoke selection method
    choices = uidoc.Selection.PickElementsByRectangle()
    #Execute method

    if choices is not None:
        
        return choices


def UnjoinElement(element):
    from Autodesk.Revit.DB import JoinGeometryUtils
    joined  = JoinGeometryUtils.GetJoinedElements(doc, element)
    for e in joined:
        secondElement = doc.GetElement(e)
        JoinGeometryUtils.UnjoinGeometry(doc, element, secondElement)

def process():
    tr = Transaction(doc, 'Unjoin selection')
    tr.Start()
    selection = selectElement()
    for e in selection:
        UnjoinElement(e)
    tr.Commit()

process()
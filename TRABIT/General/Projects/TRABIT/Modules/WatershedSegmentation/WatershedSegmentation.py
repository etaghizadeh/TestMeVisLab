# ----------------------------------------------------------------------------

# 
#  \file    WatershedSegmentation.py
#  \author  ELHAM TAGHIZADEH
#  \date    2019-02-06
#
#  

# ----------------------------------------------------------------------------

from mevis import *
#from mevis import MLAB, MLABFileManager, MLABFileDialog
from LocalFilePathSupport import populateComboBoxWithDefaultPathVariables

def init():
  ctx.field("SoView2DMarkerEditor.deleteAll").touch()
  ctx.field("inImageFileName").setStringValue("")
  ctx.field("inLabelFileName").setStringValue("")
  onStructureChange()  


def onNewMarkerAdded():
  if ctx.field("SoView2DMarkerEditor.numItems").value >= 1:
    ctx.field("SoCameraInteraction.viewAll").touch()
    
  
def onStructureChange():
  value = ctx.field("inSelectStructure").stringValue()
  if value == "Brain":
    ctx.field("SoView2DMarkerEditor.currentType").setValue(2)
  elif value == "Tumor":
    ctx.field("SoView2DMarkerEditor.currentType").setValue(3)
  elif value == "Corpus Callosum":
    ctx.field("SoView2DMarkerEditor.currentType").setValue(4)
  else:
    ctx.field("SoView2DMarkerEditor.currentType").setValue(1)


def onMenueOpen():
  exp = ctx.expandFilename(ctx.field("inImageFileName").stringValue())
  filename = MLABFileDialog.getOpenFileName(exp, "", "Open file")
  if filename:
    ctx.field("SoView2DMarkerEditor.deleteAll").touch()
    ctx.field("inImageFileName").setStringValue(filename)
    ctx.field("ImageLoad.load").touch()


def onMenueSave():
  exp = ctx.expandFilename(ctx.field("inLabelFileName").stringValue())
  filename = MLABFileDialog.getSaveFileName(exp, "", "Save file")
  if filename:
    ctx.field("inLabelFileName").value = filename
    ctx.field("MLImageFormatSave.save").touch()


def onViewModeChange():
  value = ctx.field("inViewMode").stringValue()
  if value == "all included":
    ctx.field("SoSwitch.whichChild").setValue(0)
  elif value == "mask":
    ctx.field("SoSwitch.whichChild").setValue(1)
  else:
    ctx.field("SoSwitch.whichChild").setValue(2)
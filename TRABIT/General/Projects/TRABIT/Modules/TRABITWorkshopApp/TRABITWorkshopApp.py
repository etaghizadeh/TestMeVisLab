# ----------------------------------------------------------------------------

# 
#  \file    TRABITWorkshopApp.py
#  \author  ELHAM TAGHIZADEH
#  \date    2019-02-06
#
#  

# ----------------------------------------------------------------------------

from mevis import *
from linear import vec3


def init():
  ctx.field("FiberSetFilter3D.autoApply").value = ctx.field("autoApply").value
  ctx.field("FiberSetFilter3D.autoUpdate").value = ctx.field("autoApply").value
  ctx.field("Switch.currentInput").setValue(3)
  onDrawModeChange()
  update()

#def saveAll():
#  pass

def updateAll():
  ctx.field("PreprocessDTI.inUpdate").touch()
  ctx.field("TensorTractography.apply").touch()
  onSeedContourUpdate()
  onTumorContourUpdate()
  ctx.field("FiberSetFilter3D.applyButton").touch()
  
  
def update():
  if ctx.field("autoApply").value:
    updateAll()
    
    
def onAutoApplyChange():
  if ctx.field("autoApply").value:
    updateAll()
  ctx.field("FiberSetFilter3D.autoApply").value = ctx.field("autoApply").value
  ctx.field("FiberSetFilter3D.autoUpdate").value = ctx.field("autoApply").value


def onNewMaskLoaded():
  if ctx.field("autoApply").value:
    updateAll()


def onExcludeMarkersChanged():
  if ctx.field("autoApply").value:
    ctx.field("FiberSetFilter3D.applyButton").touch()


def onSeedContourUpdate():
  ctx.field("ContourSet1Cache.update").touch()
  ctx.field("ContourSet2Cache.update").touch()


def onTumorContourUpdate():
  ctx.field("CSOConvertToImage.apply").touch()
  ctx.field("IsoSurface.apply").touch()
  
  
def onDeletingSeedContours():
  ctx.field("CSOManager.removeAllCSOsAndGroups").touch()
  ctx.field("ContourSet1Cache.clear").touch()
  ctx.field("ContourSet2Cache.clear").touch()

def onDeletingTumorContours():
  ctx.field("CSOManagerTumor.removeAllCSOsAndGroups").touch()
  ctx.field("IsoSurface.apply").touch()
  ctx.field("Switch.currentInput").setValue(3)
  
  
def onDrawModeChange():
  if ctx.field("inDrawMode").stringValue() == "SeedROI":
    ctx.field("SoSwitchDrawMode.whichChild").value = 0  
    ctx.field("SoToggleDTI.on").value = True
  else: 
    ctx.field("SoSwitchDrawMode.whichChild").value = 1
    ctx.field("SoToggleDTI.on").value = False
    
    
def onTumorCSOInterpolation():
  tumorCSO = ctx.field("CSOManagerTumor.outCSOList").object()
  if ctx.field("Switch.currentInput").value == 3:
    for cso in tumorCSO.getCSOs():
      if not cso.isInPlane:
        continue
      for i in range(0, 3):
        Im = ctx.field("OrthoReformat3.output" + str(i)).object()
        ImWMat = Im.voxelToWorldMatrix()
        ImNormal = vec3(ImWMat[0][2], ImWMat[1][2], ImWMat[2][2])
        if abs(vec3(cso.getPlaneNormal()).dot(ImNormal)) > 0.01:
          ctx.field("Switch.currentInput").setValue(i)
          break
  ctx.field("CSOSliceInterpolator.apply").touch()
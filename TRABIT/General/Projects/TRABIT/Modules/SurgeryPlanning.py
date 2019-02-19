# ----------------------------------------------------------------------------

# 
#  \file    SurgeryPlanning.py
#  \author  ELHAM TAGHIZADEH
#  \date    2019-02-18
#
#  

# ----------------------------------------------------------------------------

from mevis import *
from linear import vec3

def onRemoveCSOs():
  ctx.field("CSOManager.removeAllCSOsAndGroups").touch()
  
def onContourModeChange():
  if ctx.field("contourMode").value == "tensorSeeds":
    ctx.field("SoSwitch.whichChild").setValue(1)
  else:
    ctx.field("SoSwitch.whichChild").setValue(0)
    
def onInterpolatingContours():
  csoList = ctx.field("CSOManager1.outCSOList").object()
  for cso in csoList.getCSOs():
    csoNormal = vec3(cso.getPlaneNormal())
    for i in range(0, 3):
      ctx.field("Switch.currentInput").setValue(i)
      image = ctx.field("OrthoReformat3.output" + str(i))
      T = image.voxelToWorldMatrix()
      imageNormal = vec3([T[0][2], T[1][2], T[2][2]])
      if imageNormal.dot(csoNormal) > 0.01:
        break
  ctx.field("CSOSliceInterpolator.apply").touch()
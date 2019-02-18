# ----------------------------------------------------------------------------

# 
#  \file    PreprocessDTI.py
#  \author  ELHAM TAGHIZADEH
#  \date    2019-02-06
#
#  

# ----------------------------------------------------------------------------

from mevis import *


def onMaskImageChange():
  if ctx.field("inImage").object() is None or ctx.field("inAutoApply").value == False:
    return
  updateMask()
  

def onInputImageChange():
  if ctx.field("inAutoApply").value == False:
    return
  Update()


def updateMask():
  if ctx.field("inMaskImage").value:
    ctx.field("Switch.currentInput").setValue(1)
    if ctx.field("inLabel").object() is None:
      ctx.field("SwitchWhichMask.currentInput").setValue(1)
      ctx.field("extractLargestConnectedComponent.update").touch()
    else:
      ctx.field("SwitchWhichMask.currentInput").setValue(0)
    if ctx.field("labelInfo.sizeT").value != 0:
      ctx.field("Replicate.replicationVectorT").setValue(ctx.field("imageInfo.sizeT").value / ctx.field("labelInfo.sizeT").value)
    else:
      ctx.field("Replicate.replicationVectorT").setValue(1)
  else:
    ctx.field("Switch.currentInput").setValue(0)


def Update():
  if ctx.field("inImage").object() is None:
    return
  #ctx.field("ImagePropertyConvert.apply").touch()
  ctx.field("GaussSmoothing.update").touch()
  updateMask()

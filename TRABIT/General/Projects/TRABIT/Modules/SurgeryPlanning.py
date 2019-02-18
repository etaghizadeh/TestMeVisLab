# ----------------------------------------------------------------------------

# 
#  \file    SurgeryPlanning.py
#  \author  ELHAM TAGHIZADEH
#  \date    2019-02-18
#
#  

# ----------------------------------------------------------------------------

from mevis import *

def onRemoveCSOs():
  ctx.field("CSOManager.removeAllCSOsAndGroups").touch()
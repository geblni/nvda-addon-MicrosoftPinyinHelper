#MicrosoftPinyinIme.py
# coding:UTF-8 


from NVDAObjects.behaviors import CandidateItem
import speech
import ui
import api
from globalPluginHandler import GlobalPlugin
from logHandler import log
from NVDAObjects.UIA import UIA


#UIA:AutomationEvent	[SelectionItem_ElementSelected] Sender: ProcessId:8724, ControlType:UIA_ButtonControlTypeId (0xC350), Name:"打", AutomationId:"CandidateList.CandidateButton.0", ClassName:"CandidateButton"  ，372之50项
	#UIA_SelectionItem_ElementSelectedEventId:"UIA_elementSelected",
#创建


class GlobalPlugin(GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):

		if isinstance(obj,UIA) and obj.UIAElement.currentClassName=='CandidateButton':
			log.info(u'类替换成功')
			clsList.insert(0,CandidateButton)
		
		






class CandidateButton(UIA,CandidateItem):

	def event_UIA_elementSelected(self):
		
		
		api.setFocusObject(None)
		ui.message(self.getFormattedCandidateName(1,self.name))
		
# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2021-2022 NV Access Limited


from typing import Optional, Any
from comInterfaces import UIAutomationClient as UIA
from ._remoteOps import highLevel


_dll = None


def initialize(doRemote: bool, UIAClient: UIA.IUIAutomation):
	"""
	Initializes UI Automation remote operations.
	@param doRemote: true if code should be executed remotely, or false for locally.
	@param UIAClient: the current instance of the UI Automation client library running in NVDA.
	"""
	return True


def _remote_msWord_getCustomAttributeValue(
	rfa: highLevel.RemoteFuncAPI,
	remote_docElement: highLevel.RemoteElement,
	remote_textRange: highLevel.RemoteTextRange,
	remote_customAttribID: highLevel.RemoteInt
):
	guid_msWord_extendedTextRangePattern = rfa.newGuid("{93514122-FF04-4B2C-A4AD-4AB04587C129}")
	guid_msWord_getCustomAttributeValue = rfa.newGuid("{081ACA91-32F2-46F0-9FB9-017038BC45F8}")
	remote_customAttribValue = rfa.newNULLVariant()
	with rfa.ifBlock(remote_docElement.isExtensionSupported(guid_msWord_extendedTextRangePattern)):
		rfa.logMessage("docElement supports extendedTextRangePattern")
		remote_extendedTextRangePattern = rfa.newNULLExtensionTarget()
		rfa.logMessage("doing callExtension for extendedTextRangePattern")
		remote_docElement.callExtension(
			guid_msWord_extendedTextRangePattern,
			remote_extendedTextRangePattern
		)
		with rfa.ifBlock(remote_extendedTextRangePattern.isNull()):
			rfa.logMessage("extendedTextRangePattern is null")
			rfa.halt()
		with rfa.elseBlock():
			rfa.logMessage("got extendedTextRangePattern ")
			with rfa.ifBlock(
				remote_extendedTextRangePattern.isExtensionSupported(guid_msWord_getCustomAttributeValue)
			):
				rfa.logMessage("extendedTextRangePattern supports getCustomAttributeValue")
				rfa.logMessage("doing callExtension for getCustomAttributeValue")
				remote_extendedTextRangePattern.callExtension(
					guid_msWord_getCustomAttributeValue,
					remote_textRange,
					remote_customAttribID,
					remote_customAttribValue
				)
				rfa.logMessage("got customAttribValue of ", remote_customAttribValue)
			with rfa.elseBlock():
				rfa.logMessage("extendedTextRangePattern does not support getCustomAttributeValue")
	with rfa.elseBlock():
		rfa.logMessage("docElement does not support extendedTextRangePattern")
	rfa.logMessage("msWord_getCustomAttributeValue end")
	return remote_customAttribValue


def msWord_getCustomAttributeValue(
	docElement: UIA.IUIAutomationElement,
	textRange: UIA.IUIAutomationTextRange,
	customAttribID: int
) -> Optional[Any]:
	customAttribValue = highLevel.execute(
		_remote_msWord_getCustomAttributeValue,
		docElement, textRange, customAttribID,
		remoteLogging=True,
		dumpInstructions=True
	)
	return customAttribValue

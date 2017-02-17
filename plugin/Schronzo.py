import sys
import maya.api.OpenMaya as om

def maya_useNewAPI():
	pass


class Schronzo(om.MPxCommand):
	kPluginCmdName = "schronzo"

	def __init__(self):
		om.MPxCommand.__init__(self)

	@staticmethod
	def cmdCreator():
		return Schronzo()

	def doIt(self, args):
		print("Schronzo lebt!")


def initializePlugin(plugin):
	pluginFn = om.MFnPlugin(plugin)
	try:
		pluginFn.registerCommand(
			Schronzo.kPluginCmdName, Schronzo.cmdCreator
		)
	except:
		sys.stderr.write(
			"Failed to register command: %s\n" % Schronzo.kPluginCmdName
		)
		raise


def uninitializePlugin(plugin):
	pluginFn = om.MFnPlugin(plugin)
	try:
		pluginFn.deregisterCommand(Schronzo.kPluginCmdName)
	except:
		sys.stderr.write(
			"Failed to unregister command: %s\n" % Schronzo.kPluginCmdName
		)
		raise

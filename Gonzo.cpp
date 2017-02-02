#include <maya/MGlobal.h>
//#include <maya/MIOStream.h>
#include <maya/MSimple.h>

DeclareSimpleCommand( gonzo, "Gonzo", "2016");

MStatus gonzo::doIt( const MArgList& )
{
	MGlobal::displayInfo("Gonzo lebt");

	return MS::kSuccess;
}

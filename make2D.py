import rhinoscriptsyntax as rs
import Rhino as rh


"""
breps=rs.GetObjects("brep")


rs.EnableRedraw(False)
a=rs.coerce3dpoint([0,0,0])
b=rs.coerce3dpoint([1,0,0])
c=rs.coerce3dpoint([0,1,0])
plane=rh.Geometry.Plane(a,b,c)
a=rs.XformPlanarProjection(plane)
newcrvs=[]
n=0
m=0.5
for brep in breps:
    project=rs.TransformObjects( brep, a, True)
    crvs=rs.DuplicateEdgeCurves(project)
    stpt=rs.CurveMidPoint(crvs[32])
    line=rs.AddLine([0,n*m,0],[1,n*m,0])
    ref=rs.CurveEditPoints(line)
    orref=rs.CurveEditPoints(crvs[4])
    text=rs.AddText(str(n),[0.1,(n*m+0.05),0],0.05)
    text2=rs.AddText(str(n),stpt,0.2)
    i=0
    for crv in crvs:
        rs.OrientObject(crv,orref,ref)
        rs.ObjectLayer(crv,"reference")
        newcrvs.append(crv)
        i=i+1
        
    n=n+1
    #rs.DeleteObject(project)
    
    rs.ObjectLayer(text,"text")
    rs.DeleteObject(line)
"""

breps=rs.GetObjects("brep")
n=0
m=0.5
i=0
rs.EnableRedraw(False)
for brep in breps:
    crvs=rs.DuplicateEdgeCurves(brep)
    line=rs.AddLine([n*m,0,0],[n*m,1,0])
    ref=rs.CurveEditPoints(line)
    orref=rs.CurveEditPoints(crvs[12])
    text=rs.AddText(str(i),[(n*m+0.01),0.1,0],0.07)
    
    stpt=rs.CurveMidPoint(crvs[12])
    text2=rs.AddText(str(i),stpt,0.2)
    rs.OrientObject(brep,orref,ref,1)
    rs.ObjectLayer(text,"text")
    rs.ObjectLayer(text2,"reference")
    n=n+1
    i=i+1
    
    rs.DeleteObjects(crvs)
    rs.DeleteObject(line)
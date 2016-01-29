#import ./mce.py
import math
from pymclevel import mclevel, box, materials, nbt, TAG_Compound, TAG_String, TAG_Int
from pymclevel.materials import alphaMaterials as m

world = mclevel.fromFile("C:\Users\daniel\AppData\Roaming\.minecraft\saves\Danil's World (Danil)-2")


#offsetx, offsety, offsetz = world.getPlayerPosition('Player')
offsetx = -1133
offsety = 141
offsetz = -1209
offsetx = -550
offsety = 115
offsetz = -1671

numsteps = 300

shape = [(x,y,z) for x in range(-1,101) for y in range(-1,101) for z in range(-1,101)]

for (x,y,z) in shape:
    world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)
    world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)

path = []

for n in range(0,numsteps):
    t = 2*math.pi*n/numsteps
    path.append(((math.sin(4*t+3)*50)+50+offsetx,(math.sin(3*t+4)*50)+50+offsety,(math.sin(5*t+7)*50)+50+offsetz))
    
counter = 0
for (x,y,z) in path:
    xint = int((x))
    yint = int((y))
    zint = int((z))
    dx = int(path[(counter+1)%numsteps][0]) - int(path[(counter)%numsteps][0])
    dy = int(path[(counter+1)%numsteps][1]) - int(path[(counter)%numsteps][1])
    dz = int(path[(counter+1)%numsteps][2]) - int(path[(counter)%numsteps][2])
    ascension = str(-180*math.atan2(dx,dz)/math.pi)
    declination = str(0 - (180*math.asin(dy / math.sqrt(dx**2 + dy**2 + dz**2))/math.pi))
    command = "/tp @e[r=1] ~" + str(int((dx))) + ' ~' + str(int((dy))) + ' ~' + str(int((dz))) + " ~-0.5 ~" #" " + ascension + " ~" + declination
    world.setBlockAt(xint,yint,zint,137)
    chunk = world.getChunk(xint/16, zint/16)
    comm = TAG_Compound()
    comm["id"] = TAG_String("Control")
    comm["x"] = TAG_Int(xint)
    comm["y"] = TAG_Int(yint)
    comm["z"] = TAG_Int(zint)
    comm["Command"] = TAG_String(command)
    if world.tileEntityAt(xint,yint,zint) is not None:
        chunk.TileEntities.remove(world.tileEntityAt(xint,yint,zint))
    chunk.TileEntities.append(comm)
    world.setBlockAt(xint,yint+1,zint,70)
    counter = counter + 1
    
#print path

#shape = [(x,y,z) for x in range(0,100) for y in range(0,100) for z in range(0,100) if (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) % 50 > math.sqrt((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)))]

#for (x,y,z) in shape:
#    if (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) > 17**2) or (1==1):
#        world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 159)
#        world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) % 3 + 8))
#    else:
#        world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 169)
#        world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)

#print len(shape)

#print world.getPlayerPosition('Player')

world.saveInPlace()
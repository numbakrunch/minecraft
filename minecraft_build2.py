#import ./mce.py
import math
from pymclevel import mclevel, box, materials, nbt
from pymclevel.materials import alphaMaterials as m

world = mclevel.fromFile("C:\Users\daniel\AppData\Roaming\.minecraft\saves\Danil's World (Danil) - shrunk")

offsetx = (0-1041)-128
offsety = 0
offsetz = 149-128
#offsetx, offsety, offsetz = world.getPlayerPosition('Player')

#shape = [(x,y,z) for x in range(0,100) for y in range(0,100) for z in range(0,100)]

#for (x,y,z) in shape:
#    world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)

#shape = [(x,y,z) for x in range(0,100) for y in range(0,100) for z in range(0,100) if (((x-65)*(x-65)+(y-80)*(y-80)+(z-60)*(z-60)) - 324) * (((x-20)*(x-20)+(y-40)*(y-40)+(z-50)*(z-50)) - 361) < 500000]
shape = [(x,y,z) for x in range(0,256) for y in range(0,256) for z in range(0,256) if ((x-128)*(x-128)+(y-128)*(y-128)+(z-128)*(z-128)) < 128**2]

for (x,y,z) in shape:
    world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 95)
    world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 9)

print len(shape)

shape = [(x,y,z) for x in range(0,256) for y in range(0,256) for z in range(0,256) if ((x-127)*(x-127)+(y-127)*(y-127)+(z-127)*(z-127)) < 127**2]

for (x,y,z) in shape:
    world.setBlockAt(int(math.floor(x+offsetx+1)), int(math.floor(y+offsety+1)), int(math.floor(z+offsetz+1)), 0)
    #world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 9)

print len(shape)

#print world.getPlayerPosition('Player')

world.saveInPlace()
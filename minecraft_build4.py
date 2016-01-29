#import ./mce.py
import math
from pymclevel import mclevel, box, materials, nbt
from pymclevel.materials import alphaMaterials as m

world = mclevel.fromFile("C:\Users\daniel\AppData\Roaming\.minecraft\saves\Danil's World (Danil)-2")


#offsetx, offsety, offsetz = world.getPlayerPosition('Player')
offsetx = -1140
offsety = 150
offsetz = -1347

shape = [(x,y,z) for x in range(0,100) for y in range(0,100) for z in range(0,100)]

for (x,y,z) in shape:
    world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)
    world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)

shape = [(x,y,z) for x in range(0,100) for y in range(0,100) for z in range(0,100) if (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) % 50 > math.sqrt((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)))]

for (x,y,z) in shape:
    if (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) > 17**2) or (1==1):
        world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 159)
        world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), (((x-50)*(x-50)+(y-50)*(y-50)+(z-50)*(z-50)) % 3 + 8))
    else:
        world.setBlockAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 169)
        world.setBlockDataAt(int(math.floor(x+offsetx)), int(math.floor(y+offsety)), int(math.floor(z+offsetz)), 0)

print len(shape)

#print world.getPlayerPosition('Player')

world.saveInPlace()
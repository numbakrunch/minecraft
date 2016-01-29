#import ./mce.py
from pymclevel import mclevel #, box, materials, nbt
#from pymclevel.materials import alphaMaterials as m

offsetx = 100
offsety = 100
offsetz = 100

world = mclevel.fromFile("C:\Users\dan\AppData\Roaming\.minecraft\saves\Danil's World (Danil) - TEST")

shape = [(x,y,z) for x in range(-50,50) for y in range(-50,50) for z in range(-50,50)]

for (x,y,z) in shape:
    world.setBlockAt(x+offsetx, y+offsety, z+offsetz, 0)

shape = [(x,y,z) for x in range(-50,50) for y in range(-50,50) for z in range(-50,50) if ((x*x+y*y+z*z)%256 < 32)and((x*x+y*y+z*z)%256 > 16)]

for (x,y,z) in shape:
    world.setBlockAt(x+offsetx, y+offsety, z+offsetz, 159)
    world.setBlockDataAt(x+offsetx, y+offsety, z+offsetz, (x*x+y*y+z*z)%3+6)

print len(shape)

world.saveInPlace()
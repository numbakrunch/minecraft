#import ./mce.py
import math
from pymclevel import mclevel, box, materials, nbt, regionfile
from pymclevel.materials import alphaMaterials as m

world = mclevel.fromFile("C:\Users\daniel\AppData\Roaming\.minecraft\saves\Danil's World (Danil) - shrunk")

keeper = []
keeper.append((-5455,1245,-5405,1295)) # Desert Temple
keeper.append((-1324,-1441,-788,-1030)) # Funland
keeper.append((-735, -1930,-80,-1260)) # Becerra City, Notre Dame, St. Basil's
keeper.append((-1043,-1221,-1023,167)) # Funland/Metro2 subway
keeper.append((-1754,0,-395,205)) # Metro West
keeper.append((-340,205,-550,-1600)) # Metro North
keeper.append((-850,220,-300,400)) # Poseidon/Titanic
keeper.append((-1370,420,-970,770)) # Neptune/Stronghold
keeper.append((-320,-240,440,300)) # Metropolis/Sky City
keeper.append((-400,700,250,4200)) # Land of Oz/Ice Jungle
keeper.append((12000,-6160,12800,-3900)) # Desert Metropolis
keeper.append((11900,340,12330,530)) # Chocolate Factory/Ganymede
keeper.append((6780,1980,6870,2060)) # Snow Village
keeper.append((2590,2630,2730,2730)) # Yellowstone Park
keeper.append((4890,3240,4960,3320)) # Dryland
keeper.append((1728,2027,1789,2083)) # Independence Village
keeper.append((-2372,506,-2270,610)) # Western Frontier
keeper.append((73,-2236,125,60)) # Everest House/Skywalk North
keeper.append((-70,-1600,82,-1586)) # Skywalk West
keeper.append((-260,-1172,0,-930)) # Death Valley
keeper.append((-1676,703,-1500,890)) # Shroom Island
keeper.append((-1985,-305,-1903,-221)) # Mimas
keeper.append((3717,660,3777,707)) # East Village
keeper.append((-4033,-2505,-3979,-2435)) # Northwest Territory

print keeper

chunk_objects = world.allChunks

chunks_kept = 0
chunks_deleted = 0
chunks_total = 0
count = 0

chunk_positions = []
for idx, (x,z) in enumerate(chunk_objects):
    chunk_positions.append((x,z))
    chunks_total = chunks_total + 1
    
for (x,z) in chunk_positions:
    count = count + 1
    keep = False
    for (keep_x1,keep_z1,keep_x2,keep_z2) in keeper:
        keep_x_center_chunk = (keep_x1 + keep_x2) / 32
        keep_z_center_chunk = (keep_z1 + keep_z2) / 32
        keep_x_radius_chunk = (abs(keep_x1 - keep_x2) / 32) + 2
        keep_z_radius_chunk = (abs(keep_z1 - keep_z2) / 32) + 2
        #if (abs(x - keep_x/16) < keep_radius/16) and (abs(z - keep_z/16) < keep_radius/16):
        if ((abs(x - keep_x_center_chunk) < keep_x_radius_chunk) and (abs(z - keep_z_center_chunk) < keep_z_radius_chunk)):
            keep = True
    if (count % 1000 == 0):
        print count, "of", chunks_total, "completed."
    if keep:
        chunks_kept = chunks_kept + 1
    else:
        world.deleteChunk(x,z)
        chunks_deleted = chunks_deleted + 1
        
print chunks_kept, "chunks kept"
print chunks_deleted, "chunks deleted"

world.saveInPlace()

#    Chunk commands:
#        createChunks <point> <size>
#        deleteChunks <point> <size>
#        prune <point> <size>
#        relight [ <point> <size> ]


        #thisChunk = world.getChunk(x, z)
        #thisTAG = thisChunk.root_tag 
        #print thisTAG.get("Level").get("LastUpdate").value
        #print 'thisChunk data = ', thisChunk
        #print 'chunkPosition = ', thisChunk.chunkPosition 
        #print 'world = ', thisChunk.world 
        #print 'dirty = ', thisChunk.dirty  
        #print 'SkyLight = ', thisChunk.SkyLight  
        #print 'Biomes = ', thisChunk.Biomes
        #print 'root_tag = ', thisChunk.root_tag 
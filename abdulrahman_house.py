from mcpi import minecraft
from mcpi import block
import random 

mc = minecraft.Minecraft.create()

class abdulrahman_house:
    def __init__(self):        
        return

    def house_1(self,x,y,z):        
        self.rand_x = random.randint(0, 5)
        self.rand_z = random.randint(0, 5)
        self.rand_y = random.randint(0, 3)
 
        self.groundfloor(x,y,z)

    def groundfloor(self,x,y,z):

        #removing things around the area of use 1:
        mc.setBlocks(x +23, y , z +14, x - 15, y +18, z -8, block.AIR)
        # making ground floor for use 1
        mc.setBlocks(x - 9, y - 1, z - 5, x + 12 , y -1, z + 10, block.WOOD_PLANKS)
        #front wall
        mc.setBlocks(x + 8  , y , z -5 , x + 8 , y +4 +self.rand_y, z +10 , block.WOOL)        
        #back wall
        mc.setBlocks(x - 8  , y , z -5 , x - 8 , y +4+self.rand_y, z +10 , block.WOOL)           
        #left wall
        mc.setBlocks(x  -8 , y , z -5 , x + 8 , y +4+self.rand_y, z -5 , block.WOOL)
        #right wall
        mc.setBlocks(x  -8 , y , z +10 , x + 8 , y +4 +self.rand_y , z +10 , block.WOOL)
        # roof ( if self.rand_y > 1)
        if self.rand_y >= 1:
            mc.setBlocks(x - 9, y +4+self.rand_y, z - 5, x + 12, y +4+self.rand_y, z + 10, block.WOOL)
        # doors in t rig wall w/ glassess
        mc.setBlocks(x +1, y , z +10 , x +2 , y +1, z +10 , block.GLASS)
        mc.setBlocks(x   , y , z +10 , x , y +1, z +10 , block.AIR)
        mc.setBlocks(x -2, y , z +10 , x - 1 , y +1, z +10 , block.GLASS)
        mc.setBlock(x    , y +1, z +10 ,block.DOOR_WOOD.id,8)
        mc.setBlock(x    , y , z +10 ,block.DOOR_WOOD.id,0)
        # lights for ground floor

                                            #### **** HAVING ISSUES WITH TORCH FACING NORHT & SOUTH ****  ####
                                            
        g = 0
        for i in range(16):
            mc.setBlock(x  -7  , y +2, z -4 + g ,block.TORCH.id,0)
            g = g +2
            if g >= 14:
                g = 0
                break
        for i in range(16):
            mc.setBlock(x  +7  , y +2, z +4 + g ,block.TORCH.id,2)
            g = g +2
            if g >= 6:
                g = 0
                break
        
        # Bookslf and table     
        if self.rand_y < 1:
            mc.setBlocks(x  -5, y +1,z +7 ,x  -7, y ,z +7,block.BOOKSHELF)
            mc.setBlocks(x  -7, y +3,z +7 ,x  -7, y ,z +9,block.WOOL)
            mc.setBlock(x  -7, y ,z +6 ,block.CRAFTING_TABLE)
            mc.setBlocks(x  -7, y ,z + 5 ,x  -7, y +4,z + 5,block.BOOKSHELF)
            mc.setBlock(x  -7, y ,z +4 ,block.CRAFTING_TABLE)
            mc.setBlocks(x  -7, y ,z + 3 ,x  -7, y +4,z + 3,block.BOOKSHELF)
            mc.setBlock(x  -5, y ,z + 3,block.CHEST.id,3)
            mc.setBlock(x  -4, y ,z + 3,block.CHEST.id,3)
            mc.setBlock(x  -7, y ,z +2 ,block.CRAFTING_TABLE)
            mc.setBlock(x  -4, y ,z +8 ,block.BOOKSHELF)
        else :
            mc.setBlocks(x  -7, y ,z + 3 ,x  -7, y +4,z + 3,block.BOOKSHELF)
            mc.setBlocks(x  -7, y ,z + 5 ,x  -7, y +4,z + 5,block.BOOKSHELF)
            mc.setBlocks(x  -7, y ,z + 7 ,x  -7, y +4,z + 7,block.BOOKSHELF)
            mc.setBlocks(x  -7, y ,z + 9 ,x  -7, y +4,z + 9,block.BOOKSHELF)
            mc.setBlock(x  -5, y ,z + 3,block.CHEST.id,3)
            mc.setBlock(x  -4, y ,z + 3,block.CHEST.id,3)
            mc.setBlock(x  -7, y ,z +4 ,block.CRAFTING_TABLE)
            mc.setBlock(x  -7, y ,z +6 ,block.CRAFTING_TABLE)
            mc.setBlock(x  -7, y ,z +8 ,block.CRAFTING_TABLE)
        # Bedroom
        mc.setBlocks(x  -7, y ,z +2 , x -2, y +4+self.rand_y, z +2, block.WOOL)
        mc.setBlocks(x  -6, y ,z +2 , x -6, y +4+self.rand_y, z +2, block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -4, y ,z +2 , x -4, y +4+self.rand_y, z +2, block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -2, y ,z +2 , x -2, y +4+self.rand_y, z +2, block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -2, y ,z +2 , x -2, y +4+self.rand_y, z +2, block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -2, y ,z +1 , x -2, y +4+self.rand_y, z -3, block.WOOL)
        mc.setBlocks(x  -2, y ,z  , x -2, y +4+self.rand_y, z , block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -2, y ,z -2, x -2, y +4+self.rand_y, z -2 , block.GLOWING_OBSIDIAN)
        mc.setBlocks(x  -2, y+2 ,z -4, x -2, y +4+self.rand_y, z -4 , block.GLOWING_OBSIDIAN)
        g = 0
        for i in range(16):
            mc.setBlock(x  -1  , y +3, z +2 + g ,block.TORCH.id,0)
            g = g -2
            if g <= -7:
                g = 0
                break
        mc.setBlock(x -3 , y , z -2  , block.BED.id,11)
        mc.setBlock(x -4 , y , z -2  , block.BED.id,3)
        mc.setBlock(x -3 , y , z   , block.BED.id,11)
        mc.setBlock(x -4 , y , z   , block.BED.id,3)
        mc.setBlock(x -7 , y , z -2  , block.CHEST.id,5)
        mc.setBlock(x -7 , y , z   , block.CHEST.id,5)    
        # Kitchen
        mc.setBlocks(x +3, y , z +3 , x +3, y +4 , z +9 , block.WOOL )
        mc.setBlocks(x +3, y , z +3 , x +7, y +4 , z +3 , block.WOOL )
        mc.setBlocks(x +3, y+2 , z +5 , x +3, y +2 , z +8 , block.AIR )
        mc.setBlocks(x +3, y+1 , z +5 , x +3, y +1 , z +8 , block.AIR )
        mc.setBlocks(x +4, y+1 , z +3 , x +7, y +2 , z +3 , block.AIR )
        mc.setBlocks(x +3, y, z +4 ,x +3, y+2, z +4 , block.AIR)
        mc.setBlock(x +6, y, z +9 , block.FURNACE_ACTIVE.id)
        mc.setBlock(x +5, y, z +9 , block.FURNACE_ACTIVE.id)
        # living room
        mc.setBlock(x  +2, y ,z -4 ,block.WOOD_PLANKS)
        mc.setBlock(x  +3, y ,z -4 ,block.STAIRS_WOOD.id,3)
        mc.setBlock(x  +4, y ,z -4 ,block.STAIRS_WOOD.id,3)
        mc.setBlock(x  +5, y ,z -4 ,block.WOOD_PLANKS)

        ff = FirstFloor()
        ff.first_floor(x,y,z,self.rand_y)

class FirstFloor:
    def first_floor(self,x,y,z, rand_y):


                                                            ####  ***** FIRST FLOOR ***** ####
        if rand_y < 1:                
            # variation for first floor
            item_rand = random.randint(0,1)            
            if item_rand == 0:
                # variation 0  = Glass walls
                # front wall
                mc.setBlocks(x + 8  , y +4+rand_y, z -5 , x + 8 , y +9+rand_y, z +10 , block.GLASS)       
                # back wall
                mc.setBlocks(x - 8  , y +4+rand_y, z -5 , x - 8 , y +9+rand_y, z +10 , block.GLASS)
                # left wall
                mc.setBlocks(x -8  , y +4+rand_y, z -5 , x + 8 , y +9+rand_y, z -5 , block.GLASS)
                # rig wall
                mc.setBlocks(x -8 , y +4+rand_y, z +10 , x + 8 , y +9+rand_y, z +10 , block.GLASS)
                # floor
                mc.setBlocks(x - 9, y +4+rand_y, z - 5, x + 12, y +4+rand_y, z + 10, block.WOOD_PLANKS)
                # roof
                mc.setBlocks(x - 9, y +9+rand_y, z - 5, x + 12, y +9+rand_y, z + 10, block.WOOD_PLANKS)
            elif item_rand == 1:
                # variation 1 = Stone walls                
                # front wall
                mc.setBlocks(x + 8  , y +4+rand_y, z -5 , x + 8 , y +9+rand_y, z +10 , block.STONE_BRICK)            
                # back wall
                mc.setBlocks(x - 8  , y +4+rand_y, z -5 , x - 8 , y +9+rand_y, z +10 , block.STONE_BRICK)                
                # left wall
                mc.setBlocks(x  -8 , y +4+rand_y, z -5 , x + 8 , y +9+rand_y, z -5 , block.STONE_BRICK)
                # windows for t left wall
                mc.setBlocks(x +6, y +6+rand_y, z -5, x +1 , y +7+rand_y, z -5, block.GLASS)
                mc.setBlocks(x -6, y +6+rand_y, z -5, x -5 , y +7+rand_y, z -5, block.GLASS)
                # rig wall
                mc.setBlocks(x  -8  , y +4+rand_y, z +10 , x + 8 , y +9+rand_y, z +10 , block.STONE_BRICK)
                # windows for t rig wall
                mc.setBlocks(x +6, y +6+rand_y, z +10, x +5 , y +7+rand_y, z +10, block.GLASS)
                mc.setBlocks(x -6, y +6+rand_y, z +10, x -5 , y +7+rand_y, z +10, block.GLASS)            
                # floor
                mc.setBlocks(x - 9, y +4+rand_y, z - 5, x + 12, y +4+rand_y, z + 10, block.STONE_BRICK)
                # roof
                mc.setBlocks(x - 9, y +9+rand_y, z - 5, x + 12, y +9+rand_y, z + 10, block.STONE_BRICK)

            # stairs facing left ( in my view)
            # variation 0 for y 
            if rand_y == 0:
                mc.setBlock(x  -3, y  ,z +9 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -4, y +1 ,z +9 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -5, y +1,z +9 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -3, y  ,z +8 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -4, y +1 ,z +8 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -5, y +1,z +8 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +1,z +9 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +1,z +8 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +2,z +7 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +2,z +7 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -6, y +3,z +6 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +3,z +6 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -6, y +4,z +5 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +4,z +5 ,block.STAIRS_WOOD.id,3)
                mc.setBlocks(x -5, y +4 ,z +9 , x -6 , y +4,z +6, block.AIR )
            elif rand_y == 1:
                mc.setBlock(x  -3, y  ,z +9 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -4, y +1 ,z +9 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -5, y +1,z +9 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -3, y  ,z +8 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -4, y +1 ,z +8 ,block.STAIRS_WOOD.id,1)
                mc.setBlock(x  -5, y +1,z +8 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +1,z +9 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +1,z +8 ,block.STAIRS_WOOD.id,6)
                mc.setBlock(x  -6, y +2,z +7 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +2,z +7 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -6, y +3,z +6 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +3,z +6 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -6, y +4,z +5 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +4,z +5 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -6, y +5,z +4 ,block.STAIRS_WOOD.id,3)
                mc.setBlock(x  -5, y +5,z +4 ,block.STAIRS_WOOD.id,3)
                mc.setBlocks(x -5, y +4+rand_y ,z +9 , x -6 , y +4+rand_y,z +6-rand_y, block.AIR )

        # Door for balcony 
            mc.setBlock(x  +8 , y +6, z -2 ,block.DOOR_WOOD.id,8)
            mc.setBlock(x  +8 , y +5, z -2 ,block.DOOR_WOOD.id,0)
        # Fence for first floor
            mc.setBlocks(x +12, y +5, z +10 ,x +9, y +5,z +10, block.FENCE_NETHER_BRICK)
            mc.setBlocks(x +12, y +5, z -5 ,x +12, y +5,z + 10, block.FENCE_NETHER_BRICK)
            mc.setBlocks(x +12, y +5, z -5 ,x +9, y +5,z -5, block.FENCE_NETHER_BRICK)                
            mc.setBlock(x  + 12 , y +5, z -5 ,block.NETHER_BRICK)
            mc.setBlock(x  + +9 , y +5, z -5 ,block.NETHER_BRICK)
            mc.setBlock(x  + 12 , y +5, z +10 ,block.NETHER_BRICK)
            mc.setBlock(x  + +9 , y +5, z +10 ,block.NETHER_BRICK)

            # ligs for first floor 
                                            #### **** VING ISSUES WITTORCFACING NORT& SOUT****  #### 
            g = 0
            for i in range(16):
                mc.setBlock(x  -7  , y +7, z -4 + g ,block.TORCH.id,0)
                g = g +2
                if g >= 14:
                    g = 0
                    break
            for i in range(16):
                mc.setBlock(x  +7  , y +7, z -4 + g ,block.TORCH.id,2)
                g = g +2
                if g >= 14:
                    g = 0
                    break
            
            # Bedroom in first floor
            mc.setBlocks(x  -7, y +4,z +2 , x -2, y +8, z +2, block.WOOL)
            mc.setBlocks(x  -6, y +4,z +2 , x -6, y +8, z +2, block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -4, y +4,z +2 , x -4, y +8, z +2, block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -2, y +4,z +2 , x -2, y +8, z +2, block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -2, y +4,z +2 , x -2, y +8, z +2, block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -2, y +4,z +1 , x -2, y +8, z -3, block.WOOL)
            mc.setBlocks(x  -2, y +4,z  , x -2, y +8, z , block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -2, y +4,z -2, x -2, y +8, z -2 , block.GLOWING_OBSIDIAN)
            mc.setBlocks(x  -2, y+2 ,z -4, x -2, y +8, z -4 , block.GLOWING_OBSIDIAN)            
            # Door for bedroom in first floor
            mc.setBlock(x  -6, y +6,z +2, block.DOOR_DARK_OAK.id,8) 
            mc.setBlock(x  -6, y +5,z +2, block.DOOR_DARK_OAK.id,0) 
            # TV and sofa in first floor
            mc.setBlocks(x -2 , y +5,z +9, x +5, y +5, z+9, block.WOOL)
            mc.setBlocks(x  , y +6,z +9, x +3, y +8, z+9, block.OBSIDIAN)
            mc.setBlocks(x  , y +5,z +5 ,x +2 , y +5,z +5, block.STAIRS_NETHER_BRICK.id,3)
            mc.setBlock(x  , y +5,z +5, block.NETHER_BRICK)
            mc.setBlock(x +3 , y +5,z +5, block.NETHER_BRICK)
            mc.setBlock(x -1 , y +6,z +9, block.TORCH.id,2)
            mc.setBlock(x +4 , y +6,z +9, block.TORCH.id)
            mc.setBlock(x -1 , y +7,z +9, block.TORCH.id,2)
            mc.setBlock(x +4 , y +7,z +9, block.TORCH.id)

if __name__ == '__main__':
    player_pos = mc.player.getTilePos()
    x, y, z = player_pos

    abdulrahmanHouse = abdulrahman_house()
    abdulrahmanHouse.house_1(x, y, z)
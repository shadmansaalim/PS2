from mcpi import minecraft
from mcpi import block
import time
import math
import random

mc = minecraft.Minecraft.create()

class omkhokharhouse:
    def __init__(self):
        return

    def house_generator(self, x, y, z):

        self.random_length = random.randint(0, 4)
        self.random_width = random.randint(0, 3)
        self.random_height = random.randint(0, 3)
       
        self.createhouse(x, y, z)

    def createhouse(self, x, y, z):

        #create base under house 
        mc.setBlocks(x + 2, y, z + 2, x + 20, y + 50, z + 22, block.AIR.id)
        mc.setBlocks(x + 3, y - 1, z + 3, x + 20, y - 1, z + 21, block.STONE.id)
        mc.setBlocks(x + 21, y, z - 4, x + 39, y + 50, z + 22, block.AIR.id)
        mc.setBlocks(x + 21, y - 1, z - 3 , x + 39, y - 1, z + 21, block.STONE.id)
        mc.setBlocks(x + 40, y, z - 2, x + 62, y + 50, z + 22, block.AIR.id)
        mc.setBlocks(x + 40, y - 1, z , x + 61, y - 1, z + 21, block.STONE.id)

        '''bedroom 1'''

        if self.random_length <= 2:
            #walls
            mc.setBlocks(x + 4 + self.random_length, y, z + 4, x + 20, y + 8, z + 20 - self.random_width, block.WOOL.id)  
            #door space
            mc.setBlocks(x + 11, y + 1 , z + 4, x + 12, y + 3 + self.random_height, z + 4, block.AIR.id)         
            #windows front
            mc.setBlocks(x + 11, y + 3, z + 4, x + 12, y + 3 + self.random_height, z + 4, block.BEDROCK_INVISIBLE.id)
            #stairs
            mc.setBlocks(x + 11, y , z+3, x + 12, y, z+3, block.STAIRS_WOOD.id, 2)           
        elif self.random_length >= 3:
            #walls
            mc.setBlocks(x + 4 + self.random_length, y, z + 4, x + 20, y + 8, z + 20 - self.random_width, block.WOOD.id, 3)
            #door space
            mc.setBlocks(x + 11, y + 1 , z + 4, x + 12, y + 2, z + 1, block.AIR.id)
            #stairs
            mc.setBlocks(x + 11, y , z+3, x + 12, y, z+3, block.STAIRS_COBBLESTONE.id, 2) 

        #area inside
        mc.setBlocks(x + 5 + self.random_length, y + 1, z + 5, x + 19, y + 7, z + 19 - self.random_width, block.AIR.id)
        #floor
        mc.setBlocks(x + 5 + self.random_length, y, z + 5, x + 19, y, z + 19 - self.random_width, block.WOOL.id, 3)         
        #door
        mc.setBlock(x + 11 , y + 2, z + 4, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 11 , y + 1, z + 4, block.DOOR_WOOD.id, 4)
        mc.setBlock(x + 12 , y + 2, z + 4, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 12 , y + 1, z + 4, block.DOOR_WOOD.id, 3)
        #window side
        mc.setBlocks(x + 4 + self.random_length, y + 2, z + 8, x + 4 + self.random_length, y + 6, z + 15, block.GLASS.id)
        #window back
        mc.setBlocks(x + 8 + self.random_length, y + 2, z + 20 - self.random_width, x + 15, y + 6, z + 20 - self.random_width, block.GLASS.id)

        ''' living room '''

        if self.random_length <= 2:
            # walls
            mc.setBlocks(x + 20, y, z + 10, x + 40, y + 8, z + 20 - self.random_width, block.OBSIDIAN.id)          
            #window front
            mc.setBlocks(x + 25 - self.random_length, y + 2, z + 10, x + 35 + self.random_length, y + 5 + self.random_height, z + 10, block.BEDROCK_INVISIBLE.id)
            #window back
            mc.setBlocks(x + 26, y + 2, z + 20 - self.random_width, x + 35, y + 5, z + 20 - self.random_width, block.GLASS.id)            
        elif self.random_length >= 3:
            # walls
            mc.setBlocks(x + 20, y, z + 10, x + 40, y + 8, z + 20 - self.random_width, block.GLASS.id)

        #floor
        mc.setBlocks(x + 21, y, z + 11, x + 39, y, z + 19 - self.random_width, block.WOOL.id, 14)
        mc.setBlocks(x + 20, y, z + 13, x + 20, y, z + 18 - self.random_width, block.WOOL.id, 14)
        #living room and bedrooom 1 gap
        mc.setBlocks(x + 20, y + 1, z + 13, x + 20, y + 6, z + 18 - self.random_width, block.AIR.id)
        #area inside
        mc.setBlocks(x + 21, y + 1, z + 11, x + 39, y + 7, z + 19 - self.random_width, block.AIR.id)

        ''' bedroom 2 '''

        if self.random_length <= 2:
            #walls
            mc.setBlocks(x + 40, y, z + 1, x + 60 - self.random_length, y + 8, z + 20 - self.random_width, block.SANDSTONE.id)
            #door space
            mc.setBlocks(x + 50, y + 1 , z + 1, x + 51, y + 3 + self.random_height, z + 1, block.AIR.id) 
            #windows front
            mc.setBlocks(x + 50, y + 3, z + 1, x + 51, y + 3+ self.random_height, z + 1, block.BEDROCK_INVISIBLE.id)    
            #stairs
            mc.setBlocks(x + 50, y , z, x + 51, y, z, block.STAIRS_WOOD.id, 2)       
        elif self.random_length >= 3:
            #walls
            mc.setBlocks(x + 40, y, z + 1, x + 60 - self.random_length, y + 8, z + 20 - self.random_width, block.WOOD.id, 2)
            #door space
            mc.setBlocks(x + 50, y + 1 , z + 1, x + 51, y + 2, z + 1, block.AIR.id)
            #stairs
            mc.setBlocks(x + 50, y , z, x + 51, y, z, block.STAIRS_COBBLESTONE.id, 2)

        #floor
        mc.setBlocks(x + 41, y, z + 2, x + 59 - self.random_length, y, z + 19 - self.random_width, block.WOOL.id, 12)           
        #floor between living and bedroom
        mc.setBlocks(x + 40, y, z + 13, x + 40, y, z + 18 - self.random_width, block.WOOL.id, 14)
        #living room and bedroom 2 gap
        mc.setBlocks(x + 40, y + 1, z + 13, x + 40, y + 6, z + 18 - self.random_width, block.AIR.id)
        #area inside
        mc.setBlocks(x + 41, y + 1, z + 2, x + 59 - self.random_length, y + 7, z +19 - self.random_width, block.AIR.id)
        #door
        mc.setBlock(x + 50, y + 2, z + 1, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 50, y + 1, z + 1, block.DOOR_WOOD.id, 4)
        mc.setBlock(x + 51, y + 2, z + 1, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 51, y + 1, z + 1, block.DOOR_WOOD.id, 3)
        #window side
        mc.setBlocks(x + 60 - self.random_length, y + 2, z + 6, x + 60 - self.random_length, y + 6, z + 15, block.GLASS.id)
        #window back
        mc.setBlocks(x + 46, y + 2, z + 20 - self.random_width, x + 55, y + 6, z + 20 - self.random_width, block.GLASS.id)

        #ladders
        mc.setBlocks(x + 21, y, z + 9, x + 21, y + 8, z + 9, block.LADDER.id)
        mc.setBlocks(x + 39, y, z + 9, x + 39, y + 8, z + 9, block.LADDER.id)

        room_interiors = RoomInteriors()
        room_interiors.furniture(x, y, z, self.random_length, self.random_width)

        house_roof = Roof()
        house_roof.roof(x, y, z, self.random_length, self.random_width, self.random_height)

        house_stairs = Stairs()
        house_stairs.stairs(x,y,z, self.random_length)

class RoomInteriors:
    def furniture(self, x, y, z, random_length, random_width):

        ''' bedroom 1 interiors '''

        if random_length <= 2:
            #stone slabs
            mc.setBlocks(x + 5 + random_length, y + 1, z + 19 - random_width, x + 5 + random_length, y + 7, z + 19 - random_width, block.STONE_SLAB.id,3)
            mc.setBlocks(x + 19, y + 1, z + 19 - random_width, x + 19, y + 7, z + 19 - random_width, block.STONE_SLAB.id,3)            
            #webs
            mc.setBlocks(x + 5 + random_length, y + 7, z + 5, x + 17, y + 7, z + 5, block.COBWEB.id)    
        elif random_length >= 3:
            pass

        #bookshelf
        mc.setBlocks(x + 5 + random_length, y + 1, z + 5, x + 5 + random_length, y + 5, z + 7, block.BOOKSHELF.id)
        #sofa
        mc.setBlocks(x + 5 + random_length, y + 1, z + 11 - random_width, x + 5 + random_length, y + 1, z + 17 - random_width,block.STAIRS_NETHER_BRICK.id, 1)
        mc.setBlock(x + 5 + random_length, y + 1, z + 11 -random_width,block.OBSIDIAN)        
        mc.setBlocks(x + 6 +random_length, y + 1, z + 17 -random_width, x + 7 + random_length, y + 1, z + 17 - random_width,block.STAIRS_NETHER_BRICK.id, 2)
        mc.setBlock(x + 5 + random_length, y + 1, z + 17 -random_width, block.OBSIDIAN)
        mc.setBlock(x + 8 + random_length, y + 1, z + 17 -random_width, block.OBSIDIAN)
        #table
        mc.setBlocks(x + 7 + random_length, y + 1, z + 12 - random_width, x + 8 + random_length, y + 1, z + 15 - random_width, block.STONE_SLAB.id, 1)
        #torch
        n = 0
        for i in range(12):
            mc.setBlock(x + 5 + random_length, y + 7, z + 8 + n - random_width, block.TORCH.id, 1)
            n = n + 2
            if n >= 12:
                n = 0
                break
        #bed
        mc.setBlocks(x + 10 + random_length, y + 1, z + 19 - random_width, x + 12 + random_length, y + 1, z + 19 - random_width, block.WOOL.id, 6)
        mc.setBlocks(x + 10 + random_length, y + 1, z + 16 - random_width, x + 12 + random_length, y + 1, z + 18 - random_width, block.STONE_SLAB.id, 2)

        ''' living room  interiors'''     

        #torch
        n = 0
        for i in range(20):
            mc.setBlock(x + 21 + n, y + 6, z + 19 - random_width, block.TORCH.id, 4)
            n = n +2
            if n >= 20:
                n = 0
                break

        n = 0
        for i in range(20):
            mc.setBlock(x + 21 + n, y + 6, z + 11, block.TORCH.id, 3)
            n = n +2
            if n >= 20:
                n = 0
                break
        #stone slabs
        mc.setBlocks(x + 21, y + 1, z + 19 - random_width, x + 21, y + 4, z + 19 - random_width, block.STONE_SLAB.id,7)
        mc.setBlocks(x + 39, y + 1, z + 19 - random_width, x + 39, y + 4, z + 19 - random_width, block.STONE_SLAB.id,7)
        #furnace
        mc.setBlocks(x + 29, y + 1, z + 11, x + 32, y + 1, z + 11, block.FURNACE_ACTIVE.id, 3)
        #chest
        mc.setBlock(x + 21, y + 1, z + 11, block.CHEST.id, 3)
        mc.setBlock(x + 39, y + 1, z + 11, block.CHEST.id, 3)
        #table
        mc.setBlocks(x + 28, y + 1, z + 19 - random_width, x + 32, y + 1, z + 19 - random_width, block.CRAFTING_TABLE.id)

        ''' bedroom 2 interiors '''

        if random_length <= 2:
            #stone slabs
            mc.setBlocks(x + 41, y + 1, z + 19 - random_width, x + 41, y + 7, z + 19 - random_width, block.STONE_SLAB.id,2)
            mc.setBlocks(x + 59 - random_length, y + 1, z + 19 - random_width, x + 59 - random_length, y + 7, z + 19 - random_width, block.STONE_SLAB.id,2)
            #webs
            mc.setBlocks(x + 43, y + 7, z + 2, x + 59 - random_length, y + 7, z + 2, block.COBWEB.id)
        elif random_length >=3:
            pass
        
        #bookshelf
        mc.setBlocks(x + 59 - random_length, y + 1, z + 2, x + 59 - random_length, y + 5, z + 4, block.BOOKSHELF.id)
        #torch
        n = 0
        for i in range(12):
            mc.setBlock(x + 59 - random_length, y + 7, z + 7 + n - random_width, block.TORCH.id, 2)
            n = n + 2
            if n >= 12:
                n = 0
                break
        #sofa
        mc.setBlocks(x + 59 - random_length, y + 1, z + 9  - random_width, x + 59 - random_length, y + 1, z + 17 - random_width, block.STAIRS_WOOD.id, 0)
        mc.setBlocks(x + 52 - random_length, y + 1, z + 9  - random_width, x + 59 - random_length, y + 1, z + 9  - random_width, block.STAIRS_WOOD.id, 3)
        mc.setBlocks(x + 52 - random_length, y + 1, z + 9  - random_width, x + 52 - random_length, y + 1, z + 10 - random_width, block.WOOD_PLANKS.id)
        mc.setBlocks(x + 59 - random_length, y + 1, z + 17 - random_width, x + 58 - random_length, y + 1, z + 17 - random_width, block.WOOD_PLANKS.id)
        mc.setBlocks(x + 58 - random_length, y + 1, z + 10 - random_width, x + 58 - random_length, y + 1, z + 16 - random_width, block.STONE_SLAB.id, 2)
        mc.setBlocks(x + 53 - random_length, y + 1, z + 10 - random_width, x + 58 - random_length, y + 1, z + 10 - random_width, block.STONE_SLAB.id, 2)
        mc.setBlock(x + 59 - random_length, y + 1, z + 9 - random_width, 5)
        #table
        mc.setBlocks(x + 53 - random_length, y + 1, z + 12 - random_width, x + 56 - random_length, y + 1, z + 16 - random_width, block.STONE_SLAB.id, 2)
        #bed
        mc.setBlocks(x + 47 - random_length, y + 1, z + 19 - random_width, x + 50 - random_length, y + 1, z + 19 - random_width, block.WOOL.id, 1)
        mc.setBlocks(x + 47 - random_length, y + 1, z + 16 - random_width, x + 50 - random_length, y + 1, z + 18 - random_width, block.STONE_SLAB.id, 2)

class Roof:
    def roof(self, x, y, z, random_length, random_width, random_height):

        ''' roof top '''

        if random_length <= 2:
            #bedroom 1
            mc.setBlocks(x + 4 + random_length, y  + 9, z + 4, x + 20, y + 9 + random_height, z + 20 - random_width, block.IRON_BLOCK.id)            
            #bedroom 2
            mc.setBlocks(x + 40, y + 9, z + 1, x + 60 - random_length, y + 9 + random_height, z + 20 - random_width, block.IRON_BLOCK.id)
            #living room
            mc.setBlocks(x + 20, y + 9, z + 10, x + 40, y + 9 + random_height, z + 20 - random_width, block.IRON_BLOCK.id)
            #setting bricks
            mc.setBlocks(x + 5 + random_length, y + 9, z + 5, x + 19, y + 9, z + 19 - random_width, block.BRICK_BLOCK.id)
            mc.setBlocks(x + 41, y + 9, z + 2, x + 59 - random_length, y + 9, z +19 - random_width, block.BRICK_BLOCK.id)
            mc.setBlocks(x + 21, y + 9, z + 11, x + 39, y + 9, z + 19 - random_width, block.BRICK_BLOCK.id)
            mc.setBlocks(x + 20, y + 9, z + 11, x + 20, y + 9, z + 19 - random_width, block.BRICK_BLOCK.id)
            mc.setBlocks(x + 40, y + 9, z + 11, x + 40, y + 9, z + 19 - random_width, block.BRICK_BLOCK.id)
        elif random_length >= 3:
            #bedroom 1
            mc.setBlocks(x + 4 + random_length, y  + 9, z + 4, x + 20, y + 9 + random_height, z + 20 - random_width, block.OBSIDIAN.id)
            #bedroom 2
            mc.setBlocks(x + 40, y + 9, z + 1, x + 60 - random_length, y + 9 + random_height, z + 20 - random_width, block.OBSIDIAN.id)
            #living room
            mc.setBlocks(x + 20, y + 9, z + 10, x + 40, y + 9 + random_height, z + 20 - random_width, block.OBSIDIAN.id)
            #setting bricks on rooftop
            mc.setBlocks(x + 5 + random_length, y + 9, z + 5, x + 19, y + 9, z + 19 - random_width, block.STONE_BRICK.id)
            mc.setBlocks(x + 41, y + 9, z + 2, x + 59 - random_length, y + 9, z +19 - random_width, block.STONE_BRICK.id)
            mc.setBlocks(x + 21, y + 9, z + 11, x + 39, y + 9, z + 19 - random_width, block.STONE_BRICK.id)
            mc.setBlocks(x + 20, y + 9, z + 11, x + 20, y + 9, z + 19 - random_width, block.STONE_BRICK.id)
            mc.setBlocks(x + 40, y + 9, z + 11, x + 40, y + 9, z + 19 - random_width, block.STONE_BRICK.id)

        #removingxtra gaps
        mc.setBlocks(x + 5 + random_length, y + 10, z + 5, x + 19, y + 10 + random_height, z + 19 - random_width, block.AIR.id)
        mc.setBlocks(x + 41, y + 10, z + 2, x + 59 - random_length, y + 10 + random_height, z +19 - random_width, block.AIR.id)
        mc.setBlocks(x + 21, y + 10, z + 11, x + 39, y + 10 + random_height, z + 19 - random_width, block.AIR.id)
        mc.setBlocks(x + 20, y + 10 + random_height, z + 11, x + 20, y + 10, z + 19 - random_width, block.AIR.id)
        mc.setBlocks(x + 40, y + 10 + random_height, z + 11, x + 40, y + 10, z + 19 - random_width, block.AIR.id)
        mc.setBlocks(x + 21, y + 10, z + 10, x + 21, y + 11 + random_height, z + 10, block.AIR.id)
        mc.setBlocks(x + 39, y + 10, z + 10, x + 39, y + 11 + random_height, z + 10, block.AIR.id)
        #stairs at roof
        mc.setBlock(x + 21, y + 9, z + 10, block.STAIRS_COBBLESTONE.id, 2)
        mc.setBlock(x + 39, y + 9, z + 10, block.STAIRS_COBBLESTONE.id, 2)
        #setting torch on top
        mc.setBlock(x + 4 + random_length, y + 10 + random_height, z + 4, block.TORCH.id, 5)
        mc.setBlock(x + 4 + random_length, y + 10 + random_height, z + 20 - random_width, block.TORCH.id, 5)
        mc.setBlock(x + 20, y + 10 + random_height, z + 4, block.TORCH.id, 5)
        mc.setBlock(x + 22, y + 10 + random_height, z + 10, block.TORCH.id, 5)
        mc.setBlock(x + 38, y + 10 + random_height, z + 10, block.TORCH.id, 5)
        mc.setBlock(x + 40, y + 10 + random_height, z + 10, block.TORCH.id, 5)
        mc.setBlock(x + 60 - random_length, y + 10 + random_height, z + 1, block.TORCH.id, 5)
        mc.setBlock(x + 60 - random_length, y + 10 + random_height, z + 20 - random_width, block.TORCH.id, 5)

class Stairs:
    def stairs(self,x,y,z, random_length):

        #stairs bedroom1
        mc.setBlocks(x + 18, y + 8, z + 5, x + 19, y + 9, z + 9, block.AIR.id)

        if random_length <=2:

            i = 0
            j = 0
            for _ in range(8):
                mc.setBlocks(x + 18, y + 1, z + 12 - i, x + 19, y + 1 + j, z + 13 - i, block.WOOD_PLANKS.id)
                i += 1
                j += 1

            i = 0
            j = 0
            for _ in range(9):
                mc.setBlocks(x + 18, y + 1 + j, z + 13 - i, x + 19, y + 1 + j, z + 13 -i, block.STAIRS_WOOD.id,3)
                i += 1
                j += 1

        elif random_length >= 3:

            i = 0
            j = 0
            for _ in range(8):
                mc.setBlocks(x + 18, y + 1, z + 12 - i, x + 19, y + 1 + j, z + 13 - i, block.COBBLESTONE.id)
                i += 1
                j += 1

            i = 0
            j = 0
            for _ in range(9):
                mc.setBlocks(x + 18, y + 1 + j, z + 13 - i, x + 19, y + 1 + j, z + 13 -i, block.STAIRS_COBBLESTONE.id,3)
                i += 1
                j += 1

        #stairs bedroom2
        mc.setBlocks(x + 41, y + 8, z + 2, x + 42, y + 9 , z + 6, block.AIR.id)

        if random_length <= 2:

            i = 0
            j = 0
            for _ in range(8):
                mc.setBlocks(x + 41, y + 1, z + 9 - i, x + 42, y + 1 + j, z + 10 - i, block.COBBLESTONE.id)
                i += 1
                j += 1

            i = 0
            j = 0
            for _ in range(9):
                mc.setBlocks(x + 41, y + 1 + j, z + 10 - i, x + 42, y + 1 + j, z + 10 -i, block.STAIRS_COBBLESTONE.id,3)
                i += 1
                j += 1

        elif random_length >= 3:

            i = 0
            j = 0
            for _ in range(8):
                mc.setBlocks(x + 41, y + 1, z + 9 - i, x + 42, y + 1 + j, z + 10 - i, block.WOOD_PLANKS.id)
                i += 1
                j += 1

            i = 0
            j = 0
            for _ in range(9):
                mc.setBlocks(x + 41, y + 1 + j, z + 10 - i, x + 42, y + 1 + j, z + 10 -i, block.STAIRS_WOOD.id,3)
                i += 1
                j += 1

        #covering stairs of bedroom1
        if random_length <= 2:
            mc.setBlocks(x + 17, y + 10, z + 4, x + 20, y + 12, z + 10, block.IRON_BLOCK.id)
        elif random_length >= 3:
            mc.setBlocks(x + 17, y + 10, z + 4, x + 20, y + 12, z + 10, block.OBSIDIAN.id)

        mc.setBlocks(x + 18, y + 10, z + 5, x + 19, y + 11, z + 9, block.AIR.id)
        mc.setBlocks(x + 17, y + 10, z + 5, x + 17, y + 11, z + 5, block.AIR.id)
        mc.setBlock(x + 17, y + 11, z + 5, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 17, y + 10, z + 5, block.DOOR_WOOD.id, 4)

        #covering stairs of bedroom2
        if random_length <= 2:
            mc.setBlocks(x + 40, y + 10, z + 1, x + 43, y + 12, z + 7, block.IRON_BLOCK.id)
        elif random_length >= 3:
            mc.setBlocks(x + 40, y + 10, z + 1, x + 43, y + 12, z + 7, block.OBSIDIAN.id)

        mc.setBlocks(x + 41, y + 10, z + 2, x + 42, y + 11, z + 6, block.AIR.id)
        mc.setBlock(x + 43, y + 11, z + 2, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 43, y + 10, z + 2, block.DOOR_WOOD.id, 4)        
            
if __name__ == '__main__':
    player_pos = mc.player.getTilePos()
    x, y, z = player_pos

    omkhokhar_house = omkhokharhouse()
    omkhokhar_house.house_generator(x, y, z)
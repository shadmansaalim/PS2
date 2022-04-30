from mcpi import minecraft
from mcpi import block
import time
import math
import random

mc = minecraft.Minecraft.create()

def get_position_click():
    hits = mc.events.pollBlockHits()
    for hit in hits:
        mc.postToChat("You hit block ({},{},{})".format(hit.pos.x,hit.pos.y,hit.pos.z))

        # Player position
        player_pos = mc.player.getTilePos()
        x, y, z = player_pos
        # mc.postToChat("Your position is ({},{},{})".format(x, y, z))

        x, y, z = [8920, 2, 23949] 

        mc.postToChat("Difference is ({}, {}, {})".format(hit.pos.x - math.floor(x), hit.pos.y - math.floor(y), hit.pos.z - math.floor(z)))

class BlacksmithHouse:
    def __init__(self):        
        return

    def generate_structure(self, x, y, z):
        self.random_length_offset = random.randint(0, 5)
        self.random_width_offset = random.randint(0, 5)
        self.random_height_offset = random.randint(0, 3)

        # No offsets
        # self.random_length_offset = 0
        # self.random_width_offset = 0
        # self.random_height_offset = 0

        self.create_house(x, y, z)
        pool = Pool()
        pool.create_pool(x+self.random_length_offset, y, z)

    def create_house(self, x, y, z):
        # Clears space for build
        mc.setBlocks(x-6, y, z-6, x+6+self.random_length_offset, y+50, z-20-self.random_width_offset, block.AIR.id)

        # Creates build foundation
        mc.setBlocks(x-6, y-1, z-7, x+6+self.random_length_offset, y-1, z-15-self.random_width_offset, block.COBBLESTONE.id)

        # Creates base stone brick foundation
        mc.setBlocks(x+5+self.random_length_offset, y-1, z-8, x-1, y+3+self.random_height_offset, z-14-self.random_width_offset, block.STONE_BRICK.id)

        # Creates floor below entrance door
        mc.setBlock(x, y-1, z-8, block.WOOD_PLANKS.id)
        # Creates the entrance door
        mc.setBlock(x, y+1, z-8, block.DOOR_SPRUCE.id, 8)
        mc.setBlock(x, y, z-8, block.DOOR_SPRUCE.id, 3)

        # Creates window at front face
        hasWindow = random.randint(0,1)
        if hasWindow == 1:
            mc.setBlocks(x+4, y+1, z-8, x+4+self.random_length_offset, y+2+self.random_height_offset, z-8, block.STAINED_GLASS.id, 8)

        # Creates two window at left face
        hasWindow = random.randint(0,1)
        if hasWindow == 1:
            mc.setBlocks(x+5+self.random_length_offset, y+1, z-10, x+5+self.random_length_offset, y+2+self.random_height_offset, z-10, block.STAINED_GLASS.id, 8)
            mc.setBlocks(x+5+self.random_length_offset, y+1, z-12, x+5+self.random_length_offset, y+2+self.random_height_offset, z-12-self.random_width_offset, block.STAINED_GLASS.id, 8)

        # Creates window at back face
        hasWindow = random.randint(0,1)
        if hasWindow == 1:
            mc.setBlocks(x+3+self.random_length_offset, y+1, z-14-self.random_width_offset, x+1, y+2+self.random_height_offset, z-14-self.random_width_offset, block.STAINED_GLASS.id, 8)

        # Creates blacksmith area
        blacksmith_area = BlacksmithArea()
        blacksmith_area.create_blacksmith_area(x, y, z)

        # Clear inner first floor
        mc.setBlocks(x, y, z-9, x+4+self.random_length_offset, y+3+self.random_height_offset, z-13-self.random_width_offset, block.AIR.id)

        # Creates first floor
        floor = Floor()
        floor.create_first_floor(x, y, z, self.random_length_offset, self.random_width_offset)
        
        # Creates second floor
        floor.create_second_floor(x, y, z, self.random_length_offset, self.random_height_offset, self.random_width_offset)
    
        # Creates roof
        mc.setBlocks(x+4+self.random_length_offset, y+9+self.random_height_offset, z-9, x, y+9+self.random_height_offset, z-13-self.random_width_offset, block.WOOD_PLANKS.id, 1)
        mc.setBlocks(x+3+self.random_length_offset, y+10+self.random_height_offset, z-10, x+1, y+10+self.random_height_offset, z-12-self.random_width_offset, block.WOOD_PLANKS.id, 1)

        # Creates chimney
        mc.setBlocks(x-1, y, z-9, x-2, y+11+self.random_height_offset, z-10, block.STONE_BRICK.id)
        mc.setBlocks(x-1, y+12+self.random_height_offset, z-9, x-2, y+12+self.random_height_offset, z-10, block.NETHERRACK)
        mc.setBlocks(x-1, y+13+self.random_height_offset, z-9, x-2, y+13+self.random_height_offset, z-10, 51)

        # Adds first floor ladder 
        mc.setBlocks(x, y, z-13-self.random_width_offset, x, y+4+self.random_height_offset, z-13-self.random_width_offset, block.LADDER.id, 3)

class BlacksmithArea:
    def create_blacksmith_area(self, x, y, z):
        # Creates entrance to blacksmith at right face
        # Creates black stained window
        hasWindow = random.randint(0,1)
        if hasWindow == 1:
            mc.setBlocks(x-1, y, z-11, x-1, y+2, z-13, block.STAINED_GLASS.id, 15)
        else:
            mc.setBlocks(x-1, y, z-11, x-1, y+2, z-13, block.STONE_BRICK.id, 15)
        # Creates spruce door
        mc.setBlock(x-1, y+1, z-12, block.DOOR_SPRUCE.id, 8)
        mc.setBlock(x-1, y, z-12, block.DOOR_SPRUCE.id, 5)

        # Creates blacksmith land
        # Clears blacksmith space
        mc.setBlocks(x-2, y, z-14, x-5, y+1, z-10, block.AIR.id)
        # Creates stone slabs border
        mc.setBlocks(x-2, y, z-14, x-5, y, z-10, 44)
        # Creates stone slabs flooring
        mc.setBlocks(x-1, y-1, z-10, x-5, y-1, z-14, 1)
        # Clears stone slabs blocking floor area
        mc.setBlocks(x-2, y, z-11, x-4, y, z-13,block.AIR.id)
        # Creates anvil
        mc.setBlock(x-4, y, z-13, 145)
        # Creates rail
        mc.setBlock(x-4, y, z-12, 66, 1)
        # Creates furnance
        mc.setBlock(x-4, y, z-11, block.FURNACE_ACTIVE.id, 5)

class Floor():
    def create_first_floor(self, x, y, z, random_length_offset, random_width_offset):
        # Set inner first floor flooring
        mc.setBlocks(x, y-1, z-9, x+4+random_length_offset, y-1, z-13-random_width_offset, block.WOOD_PLANKS.id)

        # Inner floor decoration
        mc.setBlock(x+4+random_length_offset, y, z-13-random_width_offset, block.BOOKSHELF.id)
        mc.setBlock(x+4+random_length_offset, y+1, z-13-random_width_offset, block.TORCH.id, 5)
        mc.setBlock(x+4+random_length_offset, y, z-9, block.CRAFTING_TABLE.id)
        mc.setBlock(x+3+random_length_offset, y, z-13-random_width_offset, block.BED.id, 10)
        mc.setBlock(x+3+random_length_offset, y, z-12-random_width_offset, block.BED.id, 2)
        mc.setBlock(x+2+random_length_offset, y, z-13-random_width_offset, block.BED.id, 10)
        mc.setBlock(x+2+random_length_offset, y, z-12-random_width_offset, block.BED.id, 2)

    def create_second_floor(self, x, y, z, random_length_offset, random_height_offset, random_width_offset):
        # Creates second floor front face
        # Creates outer fences
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-7, x-1, y+4+random_height_offset, z-7, block.FENCE.id)
        mc.setBlocks(x+6+random_length_offset, y+4+random_height_offset, z-8, x+6+random_length_offset, y+4+random_height_offset, z-14-random_width_offset, block.FENCE.id)
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-15-random_width_offset, x-1, y+4+random_height_offset, z-15-random_width_offset, block.FENCE.id)
        mc.setBlocks(x-2, y+4+random_height_offset, z-8, x-2, y+4+random_height_offset, z-14-random_width_offset, block.FENCE.id)
        # Creates foundation
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-8, x-1, y+8+random_height_offset, z-14-random_width_offset, block.WOOD_PLANKS.id, 1)
        # Creates inner fences
        mc.setBlocks(x+4+random_length_offset, y+7+random_height_offset, z-8, x, y+7+random_height_offset, z-8, block.FENCE.id)
        mc.setBlocks(x+5+random_length_offset, y+7+random_height_offset, z-13-random_width_offset, x+5+random_length_offset, y+7+random_height_offset, z-9, block.FENCE.id)
        mc.setBlocks(x+4+random_length_offset, y+7+random_height_offset, z-14-random_width_offset, x, y+7+random_height_offset, z-14-random_width_offset, block.FENCE.id)
        mc.setBlocks(x-1, y+7+random_height_offset, z-13-random_width_offset, x-1, y+7+random_height_offset, z-9, block.FENCE.id)
        # Creates spruce log bottom border
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-8, x-1, y+4+random_height_offset, z-8, 17, 5) # 5, 9
        # Creates oak pillars
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-8, x+5+random_length_offset, y+7+random_height_offset, z-8, 17)
        mc.setBlocks(x-1, y+4+random_height_offset, z-8, x-1, y+7+random_height_offset, z-8, 17)

        # Creates second floor left face
        # Creates oak pillars 
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-14-random_width_offset, x+5+random_length_offset, y+7+random_height_offset, z-14-random_width_offset, 17)
        # Creates spruce log bottom border
        mc.setBlocks(x+5+random_length_offset, y+4+random_height_offset, z-9, x+5+random_length_offset, y+4+random_height_offset, z-13-random_width_offset, 17, 9)

        # Creates second floor back face
        # Creates oak pillars 
        mc.setBlocks(x-1, y+4+random_height_offset, z-14-random_width_offset, x-1, y+7+random_height_offset, z-14-random_width_offset, 17)
        # Creates spruce log bottom border
        mc.setBlocks(x+4+random_length_offset, y+4+random_height_offset, z-14-random_width_offset, x, y+4+random_height_offset, z-14-random_width_offset, 17, 5)

        # Creates second floor right face
        # Creates spruce log bottom border
        mc.setBlocks(x-1, y+4+random_height_offset, z-9, x-1, y+4+random_height_offset, z-13-random_width_offset, 17, 9)

        # Clears inside of second floor
        mc.setBlocks(x+4+random_length_offset, y+5+random_height_offset, z-8, x, y+6+random_height_offset, z-14-random_width_offset, block.AIR.id)
        mc.setBlocks(x+4+random_length_offset, y+7+random_height_offset, z-9, x, y+7+random_height_offset, z-13-random_width_offset, block.AIR.id)
        mc.setBlocks(x+5+random_length_offset, y+5+random_height_offset, z-9, x-1, y+6+random_height_offset, z-13-random_width_offset, block.AIR.id)

class Pool():
    def create_pool(self, x, y, z):
        depth = random.randint(2, 6)
        length_offset = random.randint(0, 3)
        width_offset = random.randint(0, 3)

        # length_offset = 0
        # width_offset = 0

        # Clears area for pool
        mc.setBlocks(x+7, y, z-6, x+13+length_offset, y+50, z-20-width_offset, block.AIR.id)

        # Creates pool foundation
        mc.setBlocks(x+7, y-1, z-7, x+13+length_offset, y-1, z-15-width_offset, block.COBBLESTONE.id)

        # Creates filled pool box
        mc.setBlocks(x+7, y-1, z-8, x+12+length_offset, y-depth, z-14-width_offset, block.SANDSTONE.id)
        # Creates fences around pool box
        mc.setBlocks(x+7, y, z-8, x+12+length_offset, y, z-14-width_offset, block.FENCE.id)
        # Clears space within pool
        mc.setBlocks(x+8, y+1, z-9, x+11+length_offset, y-depth+1, z-13-width_offset, block.AIR.id)
        # Fixes bug with fences
        mc.setBlock(x+7, y, z-15-width_offset, block.STONE.id)
        mc.setBlock(x+7, y, z-15-width_offset, block.AIR.id)
        mc.setBlock(x+7, y, z-7, block.STONE.id)
        mc.setBlock(x+7, y, z-7, block.AIR.id)
        # Creates entrance to pool
        mc.setBlocks(x+9, y, z-8, x+10+length_offset, y, z-8, block.AIR.id)
        # Creates glowstone flooring
        mc.setBlocks(x+10+length_offset, y-depth, z-10, x+9, y-depth, z-12-width_offset, block.GLOWSTONE_BLOCK.id)
        # Fills pool with water
        mc.setBlocks(x+11+length_offset, y-1, z-13-width_offset, x+8, y-1, z-9, block.WATER_STATIONARY.id)

if __name__ == '__main__':
    player_pos = mc.player.getTilePos()
    x, y, z = player_pos

    blacksmith_house = BlacksmithHouse()
    blacksmith_house.generate_structure(x, y, z)

    while True: 
        get_position_click()
        time.sleep(0.1)
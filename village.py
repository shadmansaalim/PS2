# Useful imports
from mcpi import minecraft
from mcpi import block
import time
import math
import random

# House imports
from blacksmith_house import BlacksmithHouse
from omkhokhar_house import omkhokharhouse
from omkhokhar_pool import omkhokharpool
from abdulrahman_house import abdulrahman_house
from abdulrahman_pool import abdulrahman_pool
from khaled_house import khaled_house


def spawn_village():
    player_pos = mc.player.getPos()
    x, y, z = player_pos

    random_y_offset = random.randint(0, 5)

    # Creates blacksmith house
    random_x_offset_1 = random.randint(-2, 4)
    random_z_offset_1 = random.randint(-10, 0)

    blacksmith_house = BlacksmithHouse()
    blacksmith_house.generate_structure(x+65+random_x_offset_1, y, z-2+random_z_offset_1)  

    # Creates 2nd house
    random_x_offset_2 = random.randint(-5, 15)
    random_z_offset_2 = random.randint(0, 10)

    omkhokhar_house = omkhokharhouse()
    omkhokhar_house.house_generator(x + 10 + random_x_offset_2, y - 5 - random_y_offset, z + 23 + random_z_offset_2 + random_y_offset)

    omkhokhar_pool = omkhokharpool()
    omkhokhar_pool.createpool(x + 11 + random_x_offset_2, y - 5 - random_y_offset, z + 25 + random_z_offset_2 + random_y_offset)

    # Creates 3rd house
    random_x_offset_3 = random.randint(-10, 5)
    random_z_offset_3 = random.randint(-10, 0)

    abdulrahmanHouse = abdulrahman_house()
    abdulrahmanHouse.house_1(x+15+random_x_offset_3, y, z-20+random_z_offset_3)
    abdulrahmanPool = abdulrahman_pool()
    abdulrahmanPool.pool(x+15+random_x_offset_3, y, z+random_z_offset_3)

    # Creates 4th house
    random_x_offset_4 = random.randint(0, 4)
    random_z_offset_4 = random.randint(-3, 2)

    khaledHouse = khaled_house()
    khaledHouse.house_generator(x+100+random_x_offset_4+random_y_offset, y+5+random_y_offset, z-5+random_z_offset_4)

    beneath = mc.getBlock(x, mc.getHeight(x, z), z)  # block ID

    if beneath == 12 or beneath ==24 or beneath == 159 or beneath == 172:
        ''' Creating Land'''
        mc.setBlocks(x+21+random_x_offset_2, y-6, z+3, x+61+random_x_offset_2, y+50, z+7+random_y_offset+random_z_offset_2, block.AIR.id)
        mc.setBlocks(x+21+random_x_offset_2, y-8, z+3, x+61+random_x_offset_2, y-1, z+7+random_y_offset+random_z_offset_2, block.SANDSTONE.id)

    else:

        ''' Creating Park'''
        mc.setBlocks(x-5, y-1, z-3, x+88+random_x_offset_4, y+50, z-8, block.AIR.id)        
        mc.setBlocks(x-5, y-1, z-3, x+88+random_x_offset_4, y-1, z-8, block.GRASS.id)
        mc.setBlocks(x+21+random_x_offset_2, y-6, z+3, x+61+random_x_offset_2, y+50, z+7+random_y_offset+random_z_offset_2, block.AIR.id)
        mc.setBlocks(x+21+random_x_offset_2, y-8, z+3, x+61+random_x_offset_2, y-1, z+7+random_y_offset+random_z_offset_2, block.GRASS.id)
        #trees
        mc.setBlocks(x-3, y, z-5, x-3, y+2, z-5, block.WOOD.id,2)
        mc.setBlocks(x-5, y+3, z-7, x-1, y+3, z-3, block.WOOL.id, 1)
        mc.setBlocks(x-4, y+4, z-6, x-2, y+4, z-4, block.WOOL.id, 1)
        mc.setBlocks(x-3, y+5, z-5, x-3, y+5, z-5, block.WOOL.id, 1)
        mc.setBlocks(x+11+random_x_offset_3, y, z-5, x+11+random_x_offset_3, y+1, z-5, block.WOOD.id,2)
        mc.setBlocks(x+10+random_x_offset_3, y+2, z-6, x+12+random_x_offset_3, y+2, z-4, block.WOOL.id, 1)
        mc.setBlocks(x+11+random_x_offset_3, y+3, z-5, x+11+random_x_offset_3, y+3, z-5, block.WOOL.id, 1)

    ''' Generating road'''  

    # Creates main road
    mc.setBlocks(x-5, y-1, z-2, x+89+random_x_offset_4, y+50, z+2, block.AIR.id)
    mc.setBlocks(x-5, y-1, z-2, x+89+random_x_offset_4, y-1, z+2, block.COBBLESTONE.id)
    # Entrance to stairs
    mc.setBlocks(x+89+random_x_offset_4, y-1, z-4, x+96+random_x_offset_4+random_y_offset, y+50, z+4, block.AIR.id)
    mc.setBlocks(x+89+random_x_offset_4, y-1, z-4, x+89+random_x_offset_4, y-1, z+4, block.COBBLESTONE.id)
    # Starting point
    mc.setBlock(x, y-1, z, block.GLOWSTONE_BLOCK.id)
    
    # Creates road to abdul's house
    mc.setBlocks(x+12+random_x_offset_3, y-1, z-3, x+18+random_x_offset_3, y+50, z-3, block.AIR.id)
    mc.setBlocks(x+12+random_x_offset_3, y-1, z-3, x+18+random_x_offset_3, y-1, z-3, block.COBBLESTONE.id)  
    mc.setBlocks(x+13+random_x_offset_3, y-1, z-4, x+17+random_x_offset_3, y+50, z-4, block.AIR.id)
    mc.setBlocks(x+13+random_x_offset_3, y-1, z-4, x+17+random_x_offset_3, y-1, z-4, block.COBBLESTONE.id)              
    mc.setBlocks(x+14+random_x_offset_3, y-1, z-3, x+16+random_x_offset_3, y+50, z-7+random_z_offset_3, block.AIR.id)
    mc.setBlocks(x+14+random_x_offset_3, y-1, z-3, x+16+random_x_offset_3, y-1, z-9+random_z_offset_3, block.COBBLESTONE.id)

    # Creates road to blacksmith house
    mc.setBlocks(x+64+random_x_offset_1, y-1, z-3, x+66+random_x_offset_1, y+50, z-8+random_z_offset_1, block.AIR.id)
    mc.setBlocks(x+64+random_x_offset_1, y, z-9+random_z_offset_1, x+66+random_x_offset_1, y+3, z-9+random_z_offset_1, block.AIR.id)
    mc.setBlocks(x+64+random_x_offset_1, y-1, z-3, x+66+random_x_offset_1, y-1, z-9+random_z_offset_1, block.COBBLESTONE.id)
    mc.setBlocks(x+63+random_x_offset_1, y-1, z-4, x+67+random_x_offset_1, y+50, z-4, block.AIR.id)
    mc.setBlocks(x+63+random_x_offset_1, y-1, z-4, x+67+random_x_offset_1, y-1, z-4, block.COBBLESTONE.id)
    mc.setBlocks(x+62+random_x_offset_1, y-1, z-3, x+68+random_x_offset_1, y+50, z-3, block.AIR.id)
    mc.setBlocks(x+62+random_x_offset_1, y-1, z-3, x+68+random_x_offset_1, y-1, z-3, block.COBBLESTONE.id)

    # Creates fountain at center
    
    mc.setBlocks(x+41, y, z-1, x+41, y, z+1, block.MOSS_STONE.id)
    mc.setBlocks(x+42, y, z-2, x+44, y, z-2, block.MOSS_STONE.id)
    mc.setBlocks(x+45, y, z-1, x+45, y, z+1, block.MOSS_STONE.id)
    mc.setBlocks(x+44, y, z+2, x+42, y, z+2, block.MOSS_STONE.id)
    mc.setBlocks(x+43, y, z, x+43, y+3, z, block.MOSS_STONE.id)
    mc.setBlocks(x+43, y, z, x+43, y+3, z, block.GLOWSTONE_BLOCK.id)
    mc.setBlock(x+43, y+4, z, block.WATER_FLOWING.id)

    mc.setBlocks(x+40, y-1, z-3, x+46, y+50, z-3, block.AIR.id)
    mc.setBlocks(x+41, y-1, z-4, x+45, y+50, z-4, block.AIR.id)
    mc.setBlocks(x+40, y-1, z-3, x+46, y-1, z-3, block.COBBLESTONE.id)
    mc.setBlocks(x+41, y-1, z-4, x+45, y-1, z-4, block.COBBLESTONE.id)

    mc.setBlocks(x+40, y-1, z+3, x+46, y+50, z+3, block.AIR.id)
    mc.setBlocks(x+41, y-1, z+4, x+45, y+50, z+4, block.AIR.id)
    mc.setBlocks(x+40, y-1, z+3, x+46, y-1, z+3, block.COBBLESTONE.id)
    mc.setBlocks(x+41, y-1, z+4, x+45, y-1, z+4, block.COBBLESTONE.id)
            
    # Creates road to khokhar's house
    mc.setBlocks(x+40+random_x_offset_2, y-1, z+6+random_z_offset_2, x+46+random_x_offset_2, y+50, z+6+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+40+random_x_offset_2, y-1, z+6+random_z_offset_2, x+46+random_x_offset_2, y-1, z+6+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+41+random_x_offset_2, y-1, z+5+random_z_offset_2, x+45+random_x_offset_2, y+50, z+5+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+41+random_x_offset_2, y-1, z+5+random_z_offset_2, x+45+random_x_offset_2, y-1, z+5+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+42+random_x_offset_2, y-1, z+3, x+44+random_x_offset_2, y+50, z+9+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+42+random_x_offset_2, y-1, z+3, x+44+random_x_offset_2, y-1, z+9+random_z_offset_2, block.COBBLESTONE.id)        

    # left side
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+7+random_z_offset_2, x+59+random_x_offset_2, y+50, z+7+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+7+random_z_offset_2, x+59+random_x_offset_2, y-1, z+7+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+8+random_z_offset_2, x+60+random_x_offset_2, y+50, z+8+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+8+random_z_offset_2, x+60+random_x_offset_2, y-1, z+8+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+9+random_z_offset_2, x+61+random_x_offset_2, y+50, z+9+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+45+random_x_offset_2, y-1, z+9+random_z_offset_2, x+61+random_x_offset_2, y-1, z+9+random_z_offset_2, block.COBBLESTONE.id)

    mc.setBlocks(x+58+random_x_offset_2, y-1, z+10+random_z_offset_2, x+61+random_x_offset_2, y+50, z+10+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+58+random_x_offset_2, y-1, z+10+random_z_offset_2, x+61+random_x_offset_2, y-1, z+10+random_z_offset_2, block.COBBLESTONE.id)  
    mc.setBlocks(x+59+random_x_offset_2, y-1, z+11+random_z_offset_2, x+61+random_x_offset_2, y+50, z+11+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+59+random_x_offset_2, y-1, z+11+random_z_offset_2, x+61+random_x_offset_2, y-1, z+11+random_z_offset_2, block.COBBLESTONE.id)  
    mc.setBlocks(x+60+random_x_offset_2, y-1, z+12+random_z_offset_2, x+61+random_x_offset_2, y+50, z+17+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+60+random_x_offset_2, y-1, z+12+random_z_offset_2, x+61+random_x_offset_2, y-1, z+17+random_z_offset_2, block.COBBLESTONE.id)  

    mc.setBlocks(x+60+random_x_offset_2, y-2, z+17+random_z_offset_2, x+61+random_x_offset_2, y+50, z+17+random_z_offset_2,block.AIR.id)     
    mc.setBlocks(x+60+random_x_offset_2, y-2, z+17+random_z_offset_2, x+61+random_x_offset_2, y-1, z+17+random_z_offset_2,block.COBBLESTONE.id)
    
    #creating stairs for left side
    
    mc.setBlocks(x + 60 +random_x_offset_2, y - 6 - random_y_offset, z + 18+random_z_offset_2, x + 61 +random_x_offset_2, y + 50, z + 22+random_z_offset_2+random_y_offset, 0)
    mc.setBlocks(x + 60 +random_x_offset_2, y - 6 - random_y_offset, z + 22+random_z_offset_2+random_y_offset, x + 61 +random_x_offset_2, y - 6 - random_y_offset, z + 22+random_z_offset_2+random_y_offset,block.COBBLESTONE.id)
    
    i = 0
    j = 0
    for _ in range(4+random_y_offset):
        mc.setBlocks(x+60+random_x_offset_2, y - 6-random_y_offset, z + 20 - i+random_z_offset_2+random_y_offset, x+61+random_x_offset_2, y-6+j-random_y_offset, z+21-i+random_z_offset_2+random_y_offset, block.COBBLESTONE.id)
        i += 1
        j += 1

    i = 0
    j = 0
    for _ in range(5+random_y_offset):
        mc.setBlocks(x+60+random_x_offset_2, y - 5 + j-random_y_offset, z + 21 - i+random_z_offset_2+random_y_offset, x+61+random_x_offset_2, y-5+j-random_y_offset, z+21-i+random_z_offset_2+random_y_offset, block.STAIRS_COBBLESTONE.id,3)
        i += 1
        j += 1

    # right side
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+9+random_z_offset_2, x+41+random_x_offset_2, y+50, z+9+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+9+random_z_offset_2, x+41+random_x_offset_2, y-1, z+9+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+22+random_x_offset_2, y-1, z+8+random_z_offset_2, x+41+random_x_offset_2, y+50, z+8+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+22+random_x_offset_2, y-1, z+8+random_z_offset_2, x+41+random_x_offset_2, y-1, z+8+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+23+random_x_offset_2, y-1, z+7+random_z_offset_2, x+41+random_x_offset_2, y+50, z+7+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+23+random_x_offset_2, y-1, z+7+random_z_offset_2, x+41+random_x_offset_2, y-1, z+7+random_z_offset_2, block.COBBLESTONE.id)

    mc.setBlocks(x+21+random_x_offset_2, y-1, z+11+random_z_offset_2, x+23+random_x_offset_2, y+50, z+11+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+11+random_z_offset_2, x+23+random_x_offset_2, y-1, z+11+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+10+random_z_offset_2, x+24+random_x_offset_2, y+50, z+10+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+10+random_z_offset_2, x+24+random_x_offset_2, y-1, z+10+random_z_offset_2, block.COBBLESTONE.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+12+random_z_offset_2, x+22+random_x_offset_2, y+50, z+16+random_z_offset_2, block.AIR.id)
    mc.setBlocks(x+21+random_x_offset_2, y-1, z+12+random_z_offset_2, x+22+random_x_offset_2, y-1, z+16+random_z_offset_2, block.COBBLESTONE.id)

    mc.setBlocks(x+21+random_x_offset_2, y-6, z+17+random_z_offset_2, x+22+random_x_offset_2, y-1, z+17+random_z_offset_2,block.COBBLESTONE.id)
    
    #creating stairs for right side
    mc.setBlocks(x + 21 + random_x_offset_2, y - 6 - random_y_offset, z + 17 + random_z_offset_2, x + 22 + random_x_offset_2, y + 50, z + 24+random_z_offset_2+random_y_offset, block.AIR.id)
    mc.setBlocks(x + 21 + random_x_offset_2, y - 6 - random_y_offset, z + 21 + random_z_offset_2 + random_y_offset, x + 22 + random_x_offset_2, y-6 - random_y_offset, z+25+random_z_offset_2+random_y_offset,block.COBBLESTONE.id)
    mc.setBlocks(x+21+random_x_offset_2, y-6, z+17+random_z_offset_2, x+22+random_x_offset_2, y-1, z+17+random_z_offset_2,block.COBBLESTONE.id)
    mc.setBlocks(x+21+random_x_offset_2, y-2, z+17+random_z_offset_2, x+22+random_x_offset_2, y-6-random_y_offset, z+18+random_z_offset_2, block.COBBLESTONE.id)

    i = 0
    j = 0
    for _ in range(4+random_y_offset):
        mc.setBlocks(x+21+random_x_offset_2, y - 6-random_y_offset, z + 21 - i+random_z_offset_2+random_y_offset, x+22+random_x_offset_2, y-6+j-random_y_offset, z+21-i+random_z_offset_2+random_y_offset, block.COBBLESTONE.id)
        i += 1
        j += 1

    i = 0
    j = 0
    for _ in range(5+random_y_offset):
        mc.setBlocks(x+21+random_x_offset_2, y - 5 + j - random_y_offset, z + 21 - i+random_z_offset_2+random_y_offset, x+22+random_x_offset_2, y-5+j-random_y_offset, z+21-i+random_z_offset_2+random_y_offset, block.STAIRS_COBBLESTONE.id,3)
        i += 1
        j += 1

    # Creates foundation for elevated house
    mc.setBlocks(x+95+random_x_offset_4+random_y_offset, y, z-13, x+134+random_x_offset_4+random_y_offset, y+4+random_y_offset, z+18, block.COBBLESTONE.id)

    # Creates stair blocks for elevated house
    i = 0
    j = 0
    for _ in range(4+random_y_offset):
        mc.setBlocks(x+91+i+random_x_offset_4, y, z-4, x+91+i+random_x_offset_4, y+j, z+4, block.COBBLESTONE.id)
        i += 1
        j += 1

    i = 0
    j = 0
    for _ in range(5+random_y_offset):
        mc.setBlocks(x+90+i+random_x_offset_4, y+j, z-4, x+90+i+random_x_offset_4, y+j, z+4, block.STAIRS_COBBLESTONE.id)
        i += 1
        j += 1

    # Create road to decor area
    mc.setBlocks(x+48, y-1, z-3, x+52, y+50, z-8, block.AIR.id)
    mc.setBlocks(x+48, y-1, z-3, x+52, y-1, z-8, block.COBBLESTONE.id)

    # Generates trees, cactuses, and decorations
    # Creates decor area
    if beneath == 12 or beneath == 24 or beneath == 159 or beneath == 172:
        mc.setBlocks(x+46, y-1, z-9, x+54, y+50, z-21, block.AIR.id)
        mc.setBlocks(x+46, y-1, z-9, x+54, y-1, z-21, block.SAND.id)
        mc.setBlocks(x+46, y-2, z-9, x+54, y-2, z-21, block.SANDSTONE.id)
        # Creates cactus
        mc.setBlocks(x+48, y, z-13, x+48, y+5, z-13, block.CACTUS.id)

        mc.setBlocks(x+53, y, z-15, x+53, y+3, z-15, block.CACTUS.id)

        mc.setBlocks(x+50, y, z-19, x+50, y+2, z-19, block.CACTUS.id)

        ''' Creating Sand Dunes'''
        #khokhar left road
        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+5, x+92+random_x_offset_4, y+50, z+22+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+3, x+88+random_x_offset_4, y+50, z+5, block.AIR.id)

        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+2, x+95+random_x_offset_4, y-6-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.SANDSTONE.id)
        mc.setBlocks(x+63+random_x_offset_2, y-5-random_y_offset, z+2, x+94+random_x_offset_4, y-5-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+64+random_x_offset_2, y-4-random_y_offset, z+3, x+93+random_x_offset_4, y-4-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+65+random_x_offset_2, y-3-random_y_offset, z+3, x+92+random_x_offset_4, y-3-random_y_offset, z+19+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+66+random_x_offset_2, y-2-random_y_offset, z+3, x+91+random_x_offset_4, y-2-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+67+random_x_offset_2, y-1-random_y_offset, z+4, x+90+random_x_offset_4, y-1-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+68+random_x_offset_2, y  -random_y_offset, z+5, x+89+random_x_offset_4, y  -random_y_offset, z+16+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+69+random_x_offset_2, y+1-random_y_offset, z+6, x+88+random_x_offset_4, y+1-random_y_offset, z+15+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+70+random_x_offset_2, y+2-random_y_offset, z+7, x+87+random_x_offset_4, y+2-random_y_offset, z+14+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+71+random_x_offset_2, y+3-random_y_offset, z+8, x+86+random_x_offset_4, y+3-random_y_offset, z+13+random_z_offset_2+random_y_offset, block.SAND.id)

        #khokhar right road
        mc.setBlocks(x-5, y-6-random_y_offset, z+3, x+20+random_x_offset_2,  y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x-5, y-6-random_y_offset, z+2, x+20+random_x_offset_2,  y-6-random_y_offset, z+25+random_z_offset_2+random_y_offset, block.SANDSTONE.id)
        mc.setBlocks(x-4, y-5-random_y_offset, z+2, x+19+random_x_offset_2,  y-5-random_y_offset, z+24+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x-3, y-4-random_y_offset, z+2, x+18+random_x_offset_2,  y-4-random_y_offset, z+23+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x-2, y-3-random_y_offset, z+3, x+17+random_x_offset_2,  y-3-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x-1, y-2-random_y_offset, z+3, x+16+random_x_offset_2,  y-2-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x  , y-1-random_y_offset, z+4, x+15+random_x_offset_2,  y-1-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+1, y  -random_y_offset, z+5, x+14+random_x_offset_2,  y  -random_y_offset, z+19+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+2, y+1-random_y_offset, z+6, x+13+random_x_offset_2,  y+1-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+3, y+2-random_y_offset, z+7, x+12+random_x_offset_2, y+2-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+4, y+3-random_y_offset, z+8, x+11+random_x_offset_2, y+3-random_y_offset, z+16+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+5, y+4-random_y_offset, z+9, x+10+random_x_offset_2, y+4-random_y_offset, z+15+random_z_offset_2+random_y_offset, block.SAND.id)
        
        #khokhar between both roads
        mc.setBlocks(x+25+random_x_offset_2, y-6, z+10+random_z_offset_2, x+57+random_x_offset_2,  y+50, z+22+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6-random_y_offset, z+23+random_z_offset_2, x+30+random_x_offset_2,  y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6, z+12+random_z_offset_2, x+24+random_x_offset_2, y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+24+random_x_offset_2, y, z+11+random_z_offset_2, x+24+random_x_offset_2, y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+21+random_x_offset_2, y, z+8+random_z_offset_2, x+24+random_x_offset_2, y+50, z+8+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x+58+random_x_offset_2, y-6, z+12+random_z_offset_2, x+59+random_x_offset_2, y+50, z+23+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+58+random_x_offset_2, y, z+11+random_z_offset_2, x+58+random_x_offset_2, y+50, z+23+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+61+random_x_offset_2, y, z+8+random_z_offset_2, x+59+random_x_offset_2, y+50, z+8+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x+23+random_x_offset_2, y-6, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-6-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.SANDSTONE.id)
        mc.setBlocks(x+23+random_x_offset_2, y-5, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-5-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+23+random_x_offset_2, y-4, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-4-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+23+random_x_offset_2, y-3, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-3-random_y_offset, z+19+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+24+random_x_offset_2, y-2, z+10+random_z_offset_2, x+58+random_x_offset_2,  y-2-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+25+random_x_offset_2, y-1, z+10+random_z_offset_2, x+57+random_x_offset_2,  y-1-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.SAND.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6-random_y_offset, z+23+random_z_offset_2, x+30+random_x_offset_2,  y-6-random_y_offset, z+25+random_z_offset_2+random_y_offset, block.SANDSTONE.id)
        #cactus
        mc.setBlocks(x+26+random_x_offset_2, y, z+12+random_z_offset_2, x+26+random_x_offset_2, y+8, z+12+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+56+random_x_offset_2, y, z+12+random_z_offset_2, x+56+random_x_offset_2, y+6, z+12+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+36+random_x_offset_2, y, z+12+random_z_offset_2, x+36+random_x_offset_2, y+4, z+12+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+46+random_x_offset_2, y, z+12+random_z_offset_2, x+46+random_x_offset_2, y+7, z+12+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+31+random_x_offset_2, y, z+16+random_z_offset_2, x+31+random_x_offset_2, y+2, z+16+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+41+random_x_offset_2, y, z+16+random_z_offset_2, x+41+random_x_offset_2, y+5, z+16+random_z_offset_2, block.CACTUS.id)
        mc.setBlocks(x+51+random_x_offset_2, y, z+16+random_z_offset_2, x+51+random_x_offset_2, y+3, z+16+random_z_offset_2, block.CACTUS.id)
    
    else:
        mc.setBlocks(x+46, y-1, z-9, x+54, y+50, z-21, block.AIR.id)
        mc.setBlocks(x+46, y-1, z-9, x+54, y-1, z-21, block.GRASS.id)
        # Creates trees
        mc.setBlocks(x+47, y+3, z-12, x+49, y+3, z-14, block.WOOL.id, 6)
        mc.setBlocks(x+48, y, z-13, x+48, y+4, z-13, block.WOOD.id)
        mc.setBlock(x+48, y+4, z-12, block.WOOL.id, 6)
        mc.setBlock(x+47, y+4, z-13, block.WOOL.id, 6)
        mc.setBlock(x+48, y+4, z-14, block.WOOL.id, 6)
        mc.setBlock(x+49, y+4, z-13, block.WOOL.id, 6)
        mc.setBlock(x+48, y+5, z-13, block.WOOL.id, 6)

        mc.setBlocks(x+52, y+2, z-14, x+54, y+2, z-16, block.WOOL.id, 6)
        mc.setBlocks(x+53, y, z-15, x+53, y+2, z-15, block.WOOD.id)
        mc.setBlock(x+53, y+3, z-15, block.WOOL.id, 6)

        mc.setBlocks(x+51, y+1, z-20, x+49, y+1, z-18, block.WOOL.id, 6)
        mc.setBlocks(x+50, y, z-19, x+50, y+2, z-19, block.WOOD.id)
        mc.setBlock(x+50, y+2, z-18, block.WOOL.id, 6)
        mc.setBlock(x+51, y+2, z-19, block.WOOL.id, 6)
        mc.setBlock(x+50, y+2, z-20, block.WOOL.id, 6)
        mc.setBlock(x+49, y+2, z-19, block.WOOL.id, 6)
        mc.setBlock(x+50, y+3, z-19, block.WOOL.id, 6)


        ''' Creating Hills'''
        #khokhar left road
        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+5, x+94+random_x_offset_4, y+50, z+22+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+3, x+88+random_x_offset_4, y+50, z+5, block.AIR.id)

        mc.setBlocks(x+62+random_x_offset_2, y-6-random_y_offset, z+2, x+95+random_x_offset_4, y-6-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+63+random_x_offset_2, y-5-random_y_offset, z+2, x+94+random_x_offset_4, y-5-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+64+random_x_offset_2, y-4-random_y_offset, z+3, x+93+random_x_offset_4, y-4-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+65+random_x_offset_2, y-3-random_y_offset, z+3, x+92+random_x_offset_4, y-3-random_y_offset, z+19+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+66+random_x_offset_2, y-2-random_y_offset, z+3, x+91+random_x_offset_4, y-2-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+67+random_x_offset_2, y-1-random_y_offset, z+4, x+90+random_x_offset_4, y-1-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+68+random_x_offset_2, y  -random_y_offset, z+5, x+89+random_x_offset_4, y  -random_y_offset, z+16+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+69+random_x_offset_2, y+1-random_y_offset, z+6, x+88+random_x_offset_4, y+1-random_y_offset, z+15+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+70+random_x_offset_2, y+2-random_y_offset, z+7, x+87+random_x_offset_4, y+2-random_y_offset, z+14+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+71+random_x_offset_2, y+3-random_y_offset, z+8, x+86+random_x_offset_4, y+3-random_y_offset, z+13+random_z_offset_2+random_y_offset, block.GRASS.id)

        #khokhar right road
        mc.setBlocks(x-5, y-6-random_y_offset, z+3, x+20+random_x_offset_2,  y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x-5, y-6-random_y_offset, z+2, x+20+random_x_offset_2,  y-6-random_y_offset, z+25+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x-4, y-5-random_y_offset, z+2, x+19+random_x_offset_2,  y-5-random_y_offset, z+24+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x-3, y-4-random_y_offset, z+2, x+18+random_x_offset_2,  y-4-random_y_offset, z+23+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x-2, y-3-random_y_offset, z+3, x+17+random_x_offset_2,  y-3-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x-1, y-2-random_y_offset, z+3, x+16+random_x_offset_2,  y-2-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x  , y-1-random_y_offset, z+4, x+15+random_x_offset_2,  y-1-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+1, y  -random_y_offset, z+5, x+14+random_x_offset_2,  y  -random_y_offset, z+19+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+2, y+1-random_y_offset, z+6, x+13+random_x_offset_2,  y+1-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+3, y+2-random_y_offset, z+7, x+12+random_x_offset_2, y+2-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+4, y+3-random_y_offset, z+8, x+11+random_x_offset_2, y+3-random_y_offset, z+16+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+5, y+4-random_y_offset, z+9, x+10+random_x_offset_2, y+4-random_y_offset, z+15+random_z_offset_2+random_y_offset, block.GRASS.id)
        
        #khokhar between both roads
        mc.setBlocks(x+25+random_x_offset_2, y-6, z+10+random_z_offset_2, x+57+random_x_offset_2,  y+50, z+22+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6-random_y_offset, z+23+random_z_offset_2, x+30+random_x_offset_2,  y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6, z+12+random_z_offset_2, x+24+random_x_offset_2, y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+24+random_x_offset_2, y, z+11+random_z_offset_2, x+24+random_x_offset_2, y+50, z+25+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+21+random_x_offset_2, y, z+8+random_z_offset_2, x+24+random_x_offset_2, y+50, z+8+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x+58+random_x_offset_2, y-6, z+12+random_z_offset_2, x+59+random_x_offset_2, y+50, z+23+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+58+random_x_offset_2, y, z+11+random_z_offset_2, x+58+random_x_offset_2, y+50, z+23+random_z_offset_2+random_y_offset, block.AIR.id)
        mc.setBlocks(x+61+random_x_offset_2, y, z+8+random_z_offset_2, x+59+random_x_offset_2, y+50, z+8+random_z_offset_2+random_y_offset, block.AIR.id)

        mc.setBlocks(x+23+random_x_offset_2, y-6, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-6-random_y_offset, z+22+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+23+random_x_offset_2, y-5, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-5-random_y_offset, z+21+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+23+random_x_offset_2, y-4, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-4-random_y_offset, z+20+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+23+random_x_offset_2, y-3, z+10+random_z_offset_2, x+59+random_x_offset_2,  y-3-random_y_offset, z+19+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+24+random_x_offset_2, y-2, z+10+random_z_offset_2, x+58+random_x_offset_2,  y-2-random_y_offset, z+18+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+25+random_x_offset_2, y-1, z+10+random_z_offset_2, x+57+random_x_offset_2,  y-1-random_y_offset, z+17+random_z_offset_2+random_y_offset, block.GRASS.id)
        mc.setBlocks(x+23+random_x_offset_2, y-6-random_y_offset, z+23+random_z_offset_2, x+30+random_x_offset_2,  y-6-random_y_offset, z+25+random_z_offset_2+random_y_offset, block.GRASS.id)
        #trees
        mc.setBlocks(x+26+random_x_offset_2, y, z+13+random_z_offset_2, x+26+random_x_offset_2, y+2, z+13+random_z_offset_2, block.WOOD.id)
        mc.setBlocks(x+24+random_x_offset_2, y+3, z+11+random_z_offset_2, x+28+random_x_offset_2, y+3, z+15+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+25+random_x_offset_2, y+4, z+12+random_z_offset_2, x+27+random_x_offset_2, y+4, z+14+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+26+random_x_offset_2, y+5, z+13+random_z_offset_2, x+26+random_x_offset_2, y+5, z+13+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+56+random_x_offset_2, y, z+13+random_z_offset_2, x+56+random_x_offset_2, y+2, z+13+random_z_offset_2, block.WOOD.id)
        mc.setBlocks(x+54+random_x_offset_2, y+3, z+11+random_z_offset_2, x+58+random_x_offset_2, y+3, z+15+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+55+random_x_offset_2, y+4, z+12+random_z_offset_2, x+57+random_x_offset_2, y+4, z+14+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+56+random_x_offset_2, y+5, z+13+random_z_offset_2, x+56+random_x_offset_2, y+5, z+13+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+36+random_x_offset_2, y, z+13+random_z_offset_2, x+36+random_x_offset_2, y+2, z+13+random_z_offset_2, block.WOOD.id)
        mc.setBlocks(x+34+random_x_offset_2, y+3, z+11+random_z_offset_2, x+38+random_x_offset_2, y+3, z+15+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+35+random_x_offset_2, y+4, z+12+random_z_offset_2, x+37+random_x_offset_2, y+4, z+14+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+36+random_x_offset_2, y+5, z+13+random_z_offset_2, x+36+random_x_offset_2, y+5, z+13+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+46+random_x_offset_2, y, z+13+random_z_offset_2, x+46+random_x_offset_2, y+2, z+13+random_z_offset_2, block.WOOD.id)
        mc.setBlocks(x+44+random_x_offset_2, y+3, z+11+random_z_offset_2, x+48+random_x_offset_2, y+3, z+15+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+45+random_x_offset_2, y+4, z+12+random_z_offset_2, x+47+random_x_offset_2, y+4, z+14+random_z_offset_2, block.WOOL.id, 1)
        mc.setBlocks(x+46+random_x_offset_2, y+5, z+13+random_z_offset_2, x+46+random_x_offset_2, y+5, z+13+random_z_offset_2, block.WOOL.id, 1)

    # Creates bench
    mc.setBlocks(x+48, y, z-10, x+52, y, z-10, block.STAIRS_STONE_BRICK.id, 3)
    mc.setBlocks(x+36, y, z+5, x+24+random_x_offset_2, y, z+5, block.STAIRS_STONE_BRICK.id,2)
    mc.setBlocks(x+50+random_x_offset_2, y, z+5, x+58+random_x_offset_2, y, z+5, block.STAIRS_STONE_BRICK.id,2)

    

    ''' Pillars below village '''

    #main road
    mc.setBlocks(x+42, y-2, z-1, x+44, y-100, z+1, block.WOOD.id)
    mc.setBlocks(x+87+random_x_offset_4, y-2, z-1, x+89+random_x_offset_4, y-100, z+1, block.WOOD.id)
    mc.setBlocks(x+14+random_x_offset_3, y-2, z-1, x+16+random_x_offset_3, y-100, z+1, block.WOOD.id)
    mc.setBlocks(x+64+random_x_offset_1, y-2, z-1, x+66+random_x_offset_1, y-100, z+1, block.WOOD.id)
    #khokhar house
    mc.setBlocks(x+42+random_x_offset_2, y-2, z+7+random_z_offset_2, x+44+random_x_offset_2, y-100, z+9+random_z_offset_2, block.WOOD.id) 
    #left side khokhar house
    mc.setBlocks(x+59+random_x_offset_2, y-2, z+9+random_z_offset_2, x+61+random_x_offset_2, y-100, z+11+random_z_offset_2, block.WOOD.id)
    #right side khokhar house
    mc.setBlocks(x+21+random_x_offset_2, y-2, z+9+random_z_offset_2, x+23+random_x_offset_2, y-100, z+11+random_z_offset_2, block.WOOD.id)
    #abdul's house 
    mc.setBlocks(x+24+random_x_offset_3, y-2, z-13+random_z_offset_3, x+26+random_x_offset_3, y-100, z-11+random_z_offset_3, block.WOOD.id)
    mc.setBlocks(x+24+random_x_offset_3, y-2, z-24+random_z_offset_3, x+26+random_x_offset_3, y-100, z-22+random_z_offset_3, block.WOOD.id)
    mc.setBlocks(x+7+random_x_offset_3, y-2, z-13+random_z_offset_3, x+9+random_x_offset_3, y-100, z-11+random_z_offset_3, block.WOOD.id)
    mc.setBlocks(x+7+random_x_offset_3, y-2, z-24+random_z_offset_3, x+9+random_x_offset_3, y-100, z-22+random_z_offset_3, block.WOOD.id)
    #blacksmith's house
    mc.setBlocks(x+68+random_x_offset_1, y-2, z-14+random_z_offset_1, x+70+random_x_offset_1, y-100, z-16+random_z_offset_1, block.WOOD.id)
    mc.setBlocks(x+60+random_x_offset_1, y-2, z-10+random_z_offset_1, x+62+random_x_offset_1, y-100, z-12+random_z_offset_1, block.WOOD.id)
    #khaled's house
    mc.setBlocks(x+97+random_x_offset_4+random_y_offset, y-1, z-9, x+99+random_x_offset_4+random_y_offset, y-100, z-11, block.WOOD.id)
    mc.setBlocks(x+97+random_x_offset_4+random_y_offset, y-1, z+14, x+99+random_x_offset_4+random_y_offset, y-100, z+16, block.WOOD.id)
    mc.setBlocks(x+130+random_x_offset_4+random_y_offset, y-1, z+14, x+132+random_x_offset_4+random_y_offset, y-100, z+16, block.WOOD.id)
    mc.setBlocks(x+130+random_x_offset_4+random_y_offset, y-1, z-9, x+132+random_x_offset_4+random_y_offset, y-100, z-11, block.WOOD.id)
    #khokhar's house
    mc.setBlocks(x+67+random_x_offset_2, y-7-random_y_offset, z+24+random_z_offset_2+random_y_offset, x+69+random_x_offset_2, y-100, z+26+random_z_offset_2+random_y_offset, block.WOOD.id)
    mc.setBlocks(x+67+random_x_offset_2, y-7-random_y_offset, z+39+random_z_offset_2+random_y_offset, x+69+random_x_offset_2, y-100, z+42+random_z_offset_2+random_y_offset, block.WOOD.id)
    mc.setBlocks(x+15+random_x_offset_2, y-7-random_y_offset, z+27+random_z_offset_2+random_y_offset, x+17+random_x_offset_2, y-100, z+29+random_z_offset_2+random_y_offset, block.WOOD.id)
    mc.setBlocks(x+15+random_x_offset_2, y-7-random_y_offset, z+39+random_z_offset_2+random_y_offset, x+17+random_x_offset_2, y-100, z+42+random_z_offset_2+random_y_offset, block.WOOD.id)


if __name__ == '__main__':
    mc = minecraft.Minecraft.create()

    spawn_village()
    
import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time
import random

mc = minecraft.Minecraft.create()

class khaled_house:
    def __init__(self):
        return

    def house_generator(self,x,y,z):
                
        #clear area around the house 
        mc.setBlocks(x - 7, y, z - 8, x + 40, y + 50, z + 26, block.AIR)        
        #building house 
        #left wall
        mc.setBlocks(x + 1, y, z, x + 20, y + 4, z, block.STONE_BRICK)
        #back wall
        mc.setBlocks(x + 21, y, z, x + 21, y + 4, z + 20, block.STONE_BRICK)
        #right wall
        mc.setBlocks(x + 1, y, z + 20, x + 20, y + 4, z + 20, block.STONE_BRICK)
        #front wall
        mc.setBlocks(x + 1, y, z, x + 1, y + 4, z + 20, block.STONE_BRICK)
        #making place for doors
        mc.setBlocks(x + 1, y + 1, z + 17, x + 1, y + 2, z + 17, block.AIR)
        #house floor 
        mc.setBlocks(x + 2, y, z + 1, x + 20, y, z +19, block.WOOD_PLANKS.id,0)
        #stairs leadind to the house entrance
        mc.setBlock(x, y, z + 17, block.STAIRS_WOOD.id,0) 
        mc.setBlock(x, y, z + 17, block.STAIRS_WOOD.id,0)
        #door
        mc.setBlock(x + 1, y + 2, z + 17, block.DOOR_WOOD.id, 8)
        mc.setBlock(x + 1, y + 1, z + 17, block.DOOR_WOOD.id, 4)
        #first floor roof
        mc.setBlocks(x + 2, y + 4, z + 1, x + 20, y + 4, z + 19, block.WOOD_PLANKS.id,0)
        #adding glass to the front wall
        mc.setBlocks(x + 1, y + 1, z + 1, x + 1, y + 3, z + 15, block.GLASS)

        #outside stairs
        mc.setBlocks(x + 1, y, z - 1, x + 1, y, z - 2, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 2, y + 1, z - 1, x + 2, y + 1, z - 2, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 3, y + 2, z - 1, x + 3, y + 2, z - 2, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 4, y + 3, z - 1, x + 4, y + 3, z - 2, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 5, y + 4, z - 1, x + 5, y + 4, z - 2, block.STAIRS_WOOD.id,8)
        #wall left of the stairs
        mc.setBlocks(x + 1, y, z - 3, x + 21, y + 4, z - 3, block.STONE_BRICK)
        #wall behind the stairs outside
        mc.setBlocks(x + 21, y, z - 1, x + 21, y + 4, z - 3, block.STONE_BRICK)
        #outside stairs path
        mc.setBlocks(x + 6, y + 4, z - 1, x + 20, y + 4, z - 2, block.WOOD_PLANKS.id,0)
        #remove some stone brick near the outside stairs
        mc.setBlocks(x + 6, y + 4, z, x + 20, y + 4, z, block.WOOD_PLANKS.id,0)
        #small garden under the front glass
        mc.setBlocks(x, y, z, x - 3, y, z, block.WOOD_PLANKS.id,0)
        mc.setBlocks(x - 3, y, z, x - 3, y, z + 16, block.WOOD_PLANKS.id,0)
        mc.setBlocks(x, y, z + 16, x - 3, y, z + 16, block.WOOD_PLANKS.id,0)
        mc.setBlocks(x, y, z + 1, x - 2, y, z + 15, block.GRASS)

        secondfloor = SecondFloor()
        secondfloor.second_floor(x,y,z)

        pool = Pool()
        pool.swimmingpool(x,y,z)

        furniture = Furniture()
        furniture.decor(x,y,z)

class SecondFloor:
    def second_floor(self, x, y, z):
        #second floor stone wall

        #left wall
        mc.setBlocks(x + 2, y + 5, z + 1, x + 18, y + 8, z + 1, block.STONE_BRICK)
        mc.setBlocks(x + 3, y + 5, z + 1, x + 16, y + 7, z + 1, block.AIR)
        mc.setBlocks(x + 3, y + 5,z + 1, x + 16 , y + 7, z + 1, block.GLASS)
        #back wall
        mc.setBlocks(x + 18, y + 5, z + 2, x + 18, y + 8, z + 19, block.STONE_BRICK)
        mc.setBlocks(x + 18, y + 5, z + 4, x + 18, y + 7, z + 16, block.AIR)
        mc.setBlocks(x + 18, y + 5, z + 4, x + 18, y + 7, z + 16, block.GLASS)
        mc.setBlocks(x + 18, y + 5, z + 9, x + 18, y + 7, z + 11, block.AIR)
        #right wall
        mc.setBlocks(x + 2, y + 5, z + 19, x + 18, y + 8, z + 19, block.STONE_BRICK)
        #front wall
        mc.setBlocks(x + 2, y + 5, z + 2, x + 2, y + 8, z + 19, block.STONE_BRICK)
        mc.setBlocks(x + 2, y + 5, z + 2, x + 2, y + 7, z + 18, block.AIR)
        mc.setBlocks(x + 2, y + 5, z + 2, x + 2, y + 7, z + 18, block.GLASS)
        #roof
        mc.setBlocks(x + 3, y + 8 ,z + 2, x + 18, y + 8, z + 19, block.STONE_BRICK)
        #first floor removing back wall
        mc.setBlocks(x + 22, y + 1, z + 1, x + 22, y + 3, z + 19, block.AIR)
        mc.setBlocks(x + 21, y, z + 1, x + 21, y, z + 19, block.AIR)
        #floor
        mc.setBlocks(x + 21, y, z + 1, x + 21, y, z + 19, block.WOOD_PLANKS)
        #extending the back wall length
        mc.setBlocks(x + 22, y, z -3, x + 22, y + 4, z + 3, block.STONE_BRICK)
        mc.setBlocks(x + 22, y, z + 17, x + 22, y + 4, z + 20, block.STONE_BRICK)
        mc.setBlocks(x + 22, y, z + 4, x + 22, y, z + 16, block.WOOD_PLANKS)
        #adding glass
        mc.setBlocks(x + 22, y + 1, z + 4, x + 22, y + 3, z + 8, block.GLASS)
        mc.setBlocks(x + 22, y + 1, z + 12, x + 22, y + 3, z + 16, block.GLASS)
        mc.setBlocks(x + 21, y + 1, z + 5, x + 21, y + 3, z + 17, block.AIR)
        #extending 2nd floor length 
        mc.setBlocks(x + 22, y + 4, z + 4, x + 22, y + 4, z + 16, block.STONE_BRICK)
        #adding wood
        mc.setBlocks(x + 21, y + 1, z + 1, x + 21, y + 3, z + 3, block.WOOD_PLANKS)
        mc.setBlocks(x + 21, y + 1, z + 17, x + 21, y + 3, z + 19, block.WOOD_PLANKS)

class Pool:
    def swimmingpool(self,x,y,z):

        #adding path to back garden 
        mc.setBlocks(x + 23, y, z + 9, x + 33, y, z + 11, block.WOOD_PLANKS)
        #borders for back garden
        mc.setBlocks(x + 33, y, z - 3, x + 33, y, z + 20, block.WOOD_PLANKS)
        mc.setBlocks(x + 23, y, z -3, x + 32, y, z - 3, block.WOOD_PLANKS)
        mc.setBlocks(x + 23, y, z + 20, x + 32, y, z + 20, block.WOOD_PLANKS)
        mc.setBlocks(x + 23, y, z - 2, x + 23, y, z + 8, block.WOOD_PLANKS)
        mc.setBlocks(x + 23, y, z + 12, x + 23, y, z + 19, block.WOOD_PLANKS)
        #grass for back garden
        mc.setBlocks(x + 23, y, z - 2, x + 32, y, z + 8, block.GRASS)
        mc.setBlocks(x + 23, y, z + 12, x + 32, y, z + 19, block.GRASS)
        #swiming pool
        mc.setBlocks(x + 25, y, z -1, x + 31, y - 5, z + 7, block.WOOL)
        mc.setBlocks(x + 26, y, z, x + 30, y - 4, z + 6, block.AIR)
        mc.setBlocks(x + 26, y, z, x + 30, y - 4, z + 6, block.WATER)
        #pool fence
        mc.setBlocks(x + 25, y + 1, z - 1, x + 31, y + 1, z - 1, block.FENCE)    
        mc.setBlock(x + 24, y + 1, z - 1, block.WOOD)
        mc.setBlock(x + 24, y + 1, z - 1, block.AIR)

        mc.setBlocks(x + 25, y + 1, z, x + 25, y + 1, z + 1, block.FENCE)  
        mc.setBlock(x + 25, y + 1, z - 2, block.WOOD)
        mc.setBlock(x + 25, y + 1, z - 2, block.AIR)

        mc.setBlocks(x + 25, y + 1, z + 7, x + 31, y + 1, z + 7, block.FENCE) 
        mc.setBlock(x + 24, y + 1, z + 7, block.WOOD)
        mc.setBlock(x + 24, y + 1, z + 7, block.AIR)

        mc.setBlocks(x + 25, y + 1, z + 5, x + 25, y + 1, z + 6, block.FENCE) 
        mc.setBlock(x + 25, y + 1, z + 8, block.WOOD)
        mc.setBlock(x + 25, y + 1, z + 8, block.AIR)
        mc.setBlock(x + 25, y + 1, z + 4, block.WOOD)
        mc.setBlock(x + 25, y + 1, z + 4, block.AIR)

        mc.setBlocks(x + 31, y + 1, z, x + 31, y + 1, z + 6, block.FENCE) 
        mc.setBlock(x + 31, y + 1, z - 2, block.WOOD)
        mc.setBlock(x + 31, y + 1, z - 2, block.AIR)
        mc.setBlock(x + 31, y + 1, z + 8, block.WOOD)
        mc.setBlock(x + 31, y + 1, z + 8, block.AIR)

class Furniture:
    def decor(self,x,y,z):

        #staircase from first floor to second floor
        mc.setBlocks(x + 12, y + 4, z + 17, x + 15, y + 4, z + 18, block.AIR)
        mc.setBlocks(x + 12, y + 1, z + 17, x + 12, y + 1, z + 18, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 13, y + 2, z + 17, x + 13, y + 2, z + 18, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 14, y + 3, z + 17, x + 14, y + 3, z + 18, block.STAIRS_WOOD.id,8)
        mc.setBlocks(x + 15, y + 4, z + 17, x + 15, y + 4, z + 18, block.STAIRS_WOOD.id,8)
        #book shelf near stairs
        mc.setBlocks(x + 12, y + 1, z + 19, x + 20, y + 3, z + 19, block.BOOKSHELF)
        mc.setBlocks(x + 13, y + 1, z + 17, x + 13, y + 1, z + 18, block.BOOKSHELF)
        mc.setBlocks(x + 14, y + 1, z + 17, x + 14, y + 2, z + 18, block.BOOKSHELF)
        mc.setBlocks(x + 15, y + 1, z + 17, x + 20, y + 3, z + 18, block.BOOKSHELF)
        #furniture first floor
        #tv
        mc.setBlocks(x + 5, y + 1, z + 19, x + 9, y + 3, z + 19, block.WOOD_PLANKS)
        mc.setBlocks(x + 6, y + 1, z + 19, x + 8, y + 3, z + 19, block.AIR)
        mc.setBlocks(x + 6, y + 1, z + 19, x + 8, y + 1, z + 19, block.BOOKSHELF)
        mc.setBlocks(x + 6, y + 2, z + 19, x + 8, y + 3, z + 19, block.WOOL.id,15)
        #sofa
        mc.setBlocks(x + 3, y + 1, z + 4, x + 10, y + 1, z + 4, block.STAIRS_WOOD.id,3)
        mc.setBlocks(x + 11, y + 1, z + 4, x + 11, y + 1, z + 5, block.STAIRS_WOOD.id,0)
        mc.setBlocks(x + 3, y + 1, z + 5, x + 3, y + 1, z + 12, block.STAIRS_WOOD.id,1)
        mc.setBlocks(x + 3, y + 1, z + 13, x + 4, y + 1, z + 13, block.STAIRS_WOOD.id,2)
        mc.setBlocks(x + 4, y + 1, z + 5, x + 10, y + 1, z + 5, block.WOODEN_SLAB)
        mc.setBlocks(x + 4, y + 1, z + 6, x + 4, y + 1, z + 12, block.WOODEN_SLAB)
        #table
        mc.setBlocks(x + 7, y + 1, z + 8, x + 10, y + 1, z + 11, block.WOODEN_SLAB)
        # small wood wall
        mc.setBlocks(x + 13, y + 1, z + 1, x + 13, y + 3, z + 5, block.WOOD.id,1)
        #reading area 
        mc.setBlocks(x + 14, y + 1, z + 1, x + 20, y + 3, z + 1, block.BOOKSHELF)
        mc.setBlocks(x + 14, y + 1, z + 2, x + 14, y + 3, z + 5, block.BOOKSHELF)
        mc.setBlocks(x + 16, y + 1, z + 3, x + 19, y + 1, z + 3, block.STAIRS_WOOD.id,3)
        mc.setBlocks(x + 20, y + 1, z + 3, x + 20, y + 1, z + 4, block.STAIRS_WOOD.id,0)
        mc.setBlocks(x + 16, y + 1, z + 4, x + 16, y + 1, z + 5, block.STAIRS_WOOD.id,1)
        mc.setBlocks(x + 17, y + 1, z + 4, x + 19, y + 1, z + 4 ,block.WOODEN_SLAB)
        #backgarden chairs
        mc.setBlocks(x + 30, y +  1, z + 17, x + 30, y + 1, z + 18, block.STAIRS_WOOD)  
        mc.setBlock(x + 29, y + 1, z + 17, block.STAIRS_WOOD.id,3)
        mc.setBlock(x + 29, y + 1, z + 18, block.STAIRS_WOOD.id,2)

        mc.setBlocks(x + 30, y +  1, z + 13, x + 30, y + 1, z + 14, block.STAIRS_WOOD)  
        mc.setBlock(x + 29, y + 1, z + 13, block.STAIRS_WOOD.id,3)
        mc.setBlock(x + 29, y + 1, z + 14, block.STAIRS_WOOD.id,2)

        mc.setBlocks(x + 25, y +  1, z + 13, x + 25, y + 1, z + 14, block.STAIRS_WOOD.id,1)  
        mc.setBlock(x + 26, y + 1, z + 13, block.STAIRS_WOOD.id,3)
        mc.setBlock(x + 26, y + 1, z + 14, block.STAIRS_WOOD.id,2)

        mc.setBlocks(x + 25, y +  1, z + 17, x + 25, y + 1, z + 18, block.STAIRS_WOOD.id,1)  
        mc.setBlock(x + 26, y + 1, z + 17, block.STAIRS_WOOD.id,3)
        mc.setBlock(x + 26, y + 1, z + 18, block.STAIRS_WOOD.id,2)

        #second floor
        #wood wall near bed
        mc.setBlocks(x + 10, y + 5, z + 15, x + 11, y + 7, z + 15, block.WOOD.id,1)
        mc.setBlocks(x + 11, y + 5, z + 16, x + 11, y + 7, z + 18, block.WOOD.id,1)
        mc.setBlocks(x + 10, y + 5, z + 16, x + 10, y + 6, z + 18, block.CHEST.id,4)
        #sofa 
        mc.setBlocks(x + 5, y + 5, z + 4, x + 10, y + 5,z + 4, block.STAIRS_WOOD.id,3)
        mc.setBlocks(x + 11, y + 5, z + 4, x + 11, y + 5, z + 5, block.STAIRS_WOOD)
        mc.setBlocks(x + 5, y + 5, z + 5, x + 5, y + 5,z + 10, block.STAIRS_WOOD.id,1)
        mc.setBlocks(x + 5, y + 5, z + 11, x + 6, y + 5, z + 11, block.STAIRS_WOOD.id,2)
        mc.setBlocks(x + 6, y + 5, z + 5 , x + 6, y + 5, z + 10, block.WOODEN_SLAB)
        mc.setBlocks(x + 7, y + 5, z + 5 , x + 10, y + 5, z + 5, block.WOODEN_SLAB)
        #table 
        mc.setBlocks(x + 8, y + 5, z + 7 , x + 8, y + 5, z + 10, block.WOODEN_SLAB)
        #tourches
        mc.setBlock(x + 3, y + 2, z + 1, block.TORCH.id,3)
        mc.setBlock(x + 5, y + 2, z + 1, block.TORCH.id,3)
        mc.setBlock(x + 7, y + 2, z + 1, block.TORCH.id,3)
        mc.setBlock(x + 9, y + 2, z + 1, block.TORCH.id,3)
        mc.setBlock(x + 11, y + 2, z + 1, block.TORCH.id,3)

        mc.setBlock(x + 13, y + 2, z + 6, block.TORCH.id,3)
        mc.setBlock(x + 14, y + 2, z + 6, block.TORCH.id,3)

        mc.setBlock(x + 16, y + 2, z + 2, block.TORCH.id,3)
        mc.setBlock(x + 19, y + 2, z + 2, block.TORCH.id,3)

        mc.setBlock(x + 5, y + 2, z + 18, block.TORCH.id,4)
        mc.setBlock(x + 9, y + 2, z + 18, block.TORCH.id,4)

        mc.setBlock(x + 15, y + 2, z + 16, block.TORCH.id,4)
        mc.setBlock(x + 20, y + 2, z + 16, block.TORCH.id,4)

        mc.setBlock(x + 4, y + 6, z + 18, block.TORCH.id,4)
        mc.setBlock(x + 6, y + 6, z + 18, block.TORCH.id,4)
        mc.setBlock(x + 8, y + 6, z + 18, block.TORCH.id,4)

        mc.setBlock(x + 14, y + 6, z + 18, block.TORCH.id,4)
        mc.setBlock(x + 16, y + 6, z + 18, block.TORCH.id,4)

if __name__ == '__main__':
    player_pos = mc.player.getTilePos()
    x, y, z = player_pos

    house = khaled_house()
    house.house_generator(x, y, z)

import mcpi.minecraft as minecraft
import mcpi.block as block
import random 

mc = minecraft.Minecraft.create()

class abdulrahman_pool:
    def __init__(self):        
        return

    def pool(self,x,y,z):

        h = mc.player.getTilePos()
        h.x = x 
        h.y = y 
        h.z = z -20
        
        # making swimming pool
        mc.setBlocks(h.x +13 , h.y +5 ,h.z -5,h.x +20 , h.y-5 ,h.z+6,block.GLASS)
        mc.setBlocks(h.x +14 , h.y +4,h.z -4 ,h.x +19 , h.y-4 ,h.z+5,block.AIR)
        
        # making fence for swimming pool                                       
        mc.setBlocks(h.x +13 , h.y  ,h.z -5,h.x +13 , h.y+2 ,h.z+6,block.AIR)

        # fence gate
        mc.setBlocks(h.x +13 , h.y  ,h.z-5 ,h.x +13 , h.y  ,h.z + 10 ,block.FENCE)
        mc.setBlocks(h.x +13, h.y , h.z -5 ,h.x +10, h.y ,h.z -5, block.FENCE)
        mc.setBlock(h.x +13, h.y , h.z -5,block.WOOD_PLANKS)
        mc.setBlock(h.x +9, h.y , h.z -5,block.WOOD_PLANKS)
        mc.setBlocks(h.x +9, h.y , h.z +10 ,h.x +13, h.y ,h.z +10, block.FENCE)
        mc.setBlock(h.x +13, h.y , h.z +10,block.WOOD_PLANKS)
        mc.setBlock(h.x +9, h.y , h.z +10,block.WOOD_PLANKS)
        mc.setBlock(h.x +13 , h.y  ,h.z ,block.FENCE_GATE.id,3)
        
        # making door connecting house to swimming pool
        mc.setBlocks(h.x + 8  , h.y , h.z  , h.x + 8 , h.y +2, h.z -2 , block.AIR)
        mc.setBlocks(h.x + 8  , h.y , h.z -2 , h.x + 8 , h.y +2, h.z +7 , block.GLASS)
        mc.setBlock(h.x  +8 , h.y +1, h.z -2 ,block.DOOR_WOOD.id,8)
        mc.setBlock(h.x  +8 , h.y , h.z -2 ,block.DOOR_WOOD.id,0)
        
        #filling the pool with water 
        mc.setBlocks(h.x +14 , h.y -1,h.z -4 ,h.x +19 , h.y-4 ,h.z+5,block.WATER_STATIONARY)
        
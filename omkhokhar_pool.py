from mcpi import minecraft
from mcpi import block
import time
import math
import random

mc = minecraft.Minecraft.create()

class omkhokharpool:
    def __init__(self):
        return

    def createpool(self, x, y, z):

        self.random_length = random.randint(0, 3)
        self.random_width = random.randint(0, 3)
        self.random_height = random.randint(0, 3)

        self.pool1(x + self.random_length, y, z)

    def pool1(self, x, y, z):

        if self.random_length <=1:

            #creating pool structure
            mc.setBlocks(x + 21, y - 3 - self.random_height, z - 2, x + 30 + self.random_length, y, z + 6, block.DIAMOND_BLOCK.id)
            #creating air in pool
            mc.setBlocks(x + 22, y - 2 - self.random_height, z - 1, x + 29 + self.random_length, y, z + 5, block.AIR.id)
            #filling pool with water
            mc.setBlocks(x + 22, y - 2 - self.random_height, z - 1, x + 29 + self.random_length, y, z + 5, block.WATER_STATIONARY.id)
            #creating border to pool
            mc.setBlocks(x + 21, y , z - 2, x + 30 + self.random_length, y, z + 6, block.DIAMOND_ORE.id)
            #removing top of the pool
            mc.setBlocks(x + 22, y , z - 1, x + 29 + self.random_length, y, z + 5, block.AIR.id)
            #adding fence to pool
            mc.setBlocks(x + 24, y , z + 6, x + 26, y, z + 6, block.FENCE.id)
            #adding fence gate to pool
            mc.setBlocks(x + 25, y , z + 6, x + 25, y, z + 6, block.FENCE_GATE.id)
            #adding glass at bottom
            mc.setBlocks(x + 22, y - 3 - self.random_height, z -1, x + 29 + self.random_length, y -3 - self.random_height, z + 5, block.GLASS.id)

        if self.random_length >=2:

            #creating pool structure
            mc.setBlocks(x + 21, y - 3 - self.random_height, z - 2, x + 28 + self.random_length, y, z + 5, block.GOLD_BLOCK.id)
            #creating air in pool
            mc.setBlocks(x + 22, y - 2 - self.random_height, z - 1, x + 27 + self.random_length, y, z + 4, block.AIR.id)
            #filling pool with water
            mc.setBlocks(x + 22, y - 2 - self.random_height, z - 1, x + 27 + self.random_length, y, z + 4, block.WATER_STATIONARY.id)
            #creating border to pool
            mc.setBlocks(x + 21, y , z - 2, x + 28 + self.random_length, y, z + 5, block.GOLD_ORE.id)
            #removing top of the pool
            mc.setBlocks(x + 22, y , z - 1, x + 27 + self.random_length, y, z + 4, block.AIR.id)
            #adding fence to pool
            mc.setBlocks(x + 24, y , z + 5, x + 26, y, z + 5, block.FENCE.id)
            #adding fence gate to pool
            mc.setBlocks(x + 25, y , z + 5, x + 25, y, z + 5, block.FENCE_GATE.id)
            #adding glass at bottom
            mc.setBlocks(x + 22, y - 3 - self.random_height, z -1, x + 27 + self.random_length, y -3 - self.random_height, z + 4,  block.DIAMOND_BLOCK.id)            
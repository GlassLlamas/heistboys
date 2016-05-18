import os

import pygame

from buffalo import utils

textures = dict()

def loadSprites(spritePath):
    directions = {"up":[], "down":[], "left":[], "right":[]}
    for direction in directions:
        path = os.path.join(spritePath, direction)
        for filename in [f for f in os.listdir(path) if f.endswith(".png")]:
            fullpath = os.path.join(path, filename)
            # If the image isn't already in the cache
            if fullpath not in textures:
                # Load it and put it in the cache so it doesn't need to be loaded again
                textures[fullpath] = pygame.image.load(fullpath)
            directions[direction].append(textures[fullpath])
    return directions

def loadItemSprites(spritePath):
    itemSprites = {False:[], True:[]}
    for relpath in ["", "inUse"]:
        path = os.path.join(spritePath, relpath)
        for filename in [f for f in os.listdir(path) if f.endswith(".png")]:
            fullpath = os.path.join(path, filename)
            # If the image isn't already in the cache
            if fullpath not in textures:
                # Load it and put it in the cache so it doesn't need to be loaded again
                textures[fullpath] = pygame.image.load(fullpath)
            itemSprites[bool(relpath)].append(textures[fullpath])
    return itemSprites

def getSprite(spritePath):
    if spritePath in textures:
        return textures[spritePath]
    textures[spritePath] = pygame.image.load(spritePath)
    return textures[spritePath]

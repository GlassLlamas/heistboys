import os

import pygame

from buffalo import utils

textures = dict()

def loadAnimateSprites(spritePath):
    directions = {"up":[], "down":[], "left":[], "right":[]}
    for direction in directions:
        path = os.path.join(spritePath, direction)
        for filename in [f for f in os.listdir(path) if f.endswith(".png")]:
            directions[direction].append(getSprite(os.path.join(path, filename)))
    return directions

def loadUsableItemSprites(spritePath):
    itemSprites = {False:[], True:[]}
    for relpath in ["", "inUse"]:
        path = os.path.join(spritePath, relpath)
        for filename in [f for f in os.listdir(path) if f.endswith(".png")]:
            itemSprites[bool(relpath)].append(getSprite(os.path.join(path, filename)))
    return itemSprites

def loadUnusableItemSprites(spritePath):
    itemSprites = []
    for filename in [f for f in os.listdir(spritePath) if f.endswith(".png")]:
        itemSprites.append(getSprite(os.path.join(spritePath, filename)))
    return itemSprites

def getSprite(spritePath):
    if spritePath in textures:
        return textures[spritePath]
    textures[spritePath] = pygame.image.load(spritePath)
    return textures[spritePath]

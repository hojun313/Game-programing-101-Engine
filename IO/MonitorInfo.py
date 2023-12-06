# 화면 정보를 담고 있는 클래스
import pygame

class MonitorInfo:
    def __init__(self):
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.center = (self.width/2, self.height/2)
        self.top = (self.width/2, 0)
        self.bottom = (self.width/2, self.height)
        self.left = (0, self.height/2)
        self.right = (self.width, self.height/2)
        self.topLeft = (0, 0)
        self.topRight = (self.width, 0)
        self.bottomLeft = (0, self.height)
        self.bottomRight = (self.width, self.height)
        self.centerTop = (self.width/2, 0)
        self.centerBottom = (self.width/2, self.height)
        self.centerLeft = (0, self.height/2)
        self.centerRight = (self.width, self.height/2)

    def getCenter(self):
        return self.center

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getTopLeft(self):
        return self.topLeft

    def getTopRight(self):
        return self.topRight

    def getBottomLeft(self):
        return self.bottomLeft

    def getBottomRight(self):
        return self.bottomRight

    def getCenterTop(self):
        return self.centerTop

    def getCenterBottom(self):
        return self.centerBottom

    def getCenterLeft(self):
        return self.centerLeft

    def getCenterRight(self):
        return self.centerRight

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
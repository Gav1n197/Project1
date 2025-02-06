## Project1 2/6/25 3DGameEngineConcepts
## Comments on column 81, 
## All file names and folder names are capitalized (Assets/Planets/Textures/WhitePlanet.png)

import math, sys, random
from direct.showbase.ShowBase import ShowBase 

class MyApp(ShowBase):
    def __init__(self): ## Constructor
        ShowBase.__init__(self)
        self.accept('escape', self.quit)  ## Esc to escape
        self.setupScene()


    def setupScene(self): ## snailCase for entire project
        self.universe = self.loader.loadModel("Assets/Universe/Universe.x")
        self.tex = self.loader.loadTexture("Assets/Universe/Universe.jpg")
        self.universe.reparentTo(self.render)                                   # Makes the universe object a child of the camera (self.render)
        self.universe.setScale(15000)
        self.universe.setTexture(self.tex, 1)

        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/Mercury.jpg",      160,   5000, 1890, 320)
        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/Moon.jpg",         400,   5200, 2270, 120)
        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/WhitePlanet.jpg", -2700,  6200, 1270, 150)
        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/Neptune.jpg",     -2500,  6000, 970, 100)
        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/Venus.jpg",        3000, -6000, 230, 350)
        self.placePlanet("Assets/Planets/protoPlanet.x", "Assets/Planets/Textures/GreyPlanet.jpg",        -3000, -6000, 730, 250)

        self.player = self.loader.loadModel("Assets/Spaceships/Dumbledore/Dumbledore.x")
        self.player.reparentTo(self.render)
        self.player.setHpr(0, 93, 0) ## Set rotation

        self.station = self.loader.loadModel("Assets/SpaceStation/SpaceStation1B/spaceStation.x")
        self.station.reparentTo(self.render)
        self.station.setPos(40, 50, 23)
        self.station.setHpr(0, 93, 0) 

    def placePlanet(self, planet, texture, x, y, z, scale):
        self.planet = self.loader.loadModel(planet)
        self.texture = self.loader.loadTexture(texture)
        self.planet.reparentTo(self.render)
        self.planet.setPos(x, y, z)
        self.planet.setScale(scale)
        self.planet.setTexture(self.texture, 1)

    def quit(self):
        sys.exit()


app = MyApp()
app.run()
## Project2 2/13/25 3DGameEngineConcepts
## Comments on column 81, 
## All file names and folder names are capitalized (Assets/Planets/Textures/WhitePlanet.png)

import math, sys, random
from direct.showbase.ShowBase import ShowBase 
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses

class MyApp(ShowBase):
    def __init__(self): ## Constructor
        ShowBase.__init__(self)
        self.accept('escape', self.quit)  ## Esc to escape
        self.setupScene()
        
        fullCycle = 60
        for i in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)  ##Concantenation of nicknames for each drone made

            self.DrawCloudDefense(self.planet1, nickName)
            self.drawBaseballSeams(self.SpaceStation1, nickName, i, fullCycle, 2)


    def setupScene(self): ## snailCase for entire project
        self.universe = spaceJamClasses.Universe(self.loader, "Assets/Universe/Universe.x", self.render, "Universe", "Assets/Universe/Universe.jpg", (0,0,0), 10000)

        self.planet1 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet1", "Assets/Planets/Textures/Mercury.jpg",       ( 160,   5000, 1890), 320) 
        self.planet2 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet2", "Assets/Planets/Textures/Moon.jpg",          ( 400,   5400, 2270), 120) 
        self.planet3 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet3", "Assets/Planets/Textures/WhitePlanet.jpg",   (-2700,  6200, 1270), 150) 
        self.planet4 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet4", "Assets/Planets/Textures/Neptune.jpg",       (-2500,  6000, 970),  100) 
        self.planet5 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet5", "Assets/Planets/Textures/Venus.jpg",         ( 3000, -6000, 230),  350) 
        self.planet6 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet6", "Assets/Planets/Textures/GreyPlanet.jpg",    (-3000, -6000, 730),  250) 


        self.player = self.loader.loadModel("Assets/Spaceships/Dumbledore/Dumbledore.x")
        self.player.reparentTo(self.render)
        self.player.setHpr(0, 93, 0) ## Set rotation
        
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "Assets/SpaceStation/SpaceStation1B/spaceStation.x", self.render, "spaceStation1", "Assets/Planets/Textures/Mercury.jpg",       (40, 50, 23), 1) 
        #self.SpaceStation1 = self.loader.loadModel("Assets/SpaceStation/SpaceStation1B/spaceStation.x")
        #self.SpaceStation1.reparentTo(self.render)
        #self.SpaceStation1.setPos(40, 50, 23)
        #self.SpaceStation1.setHpr(0, 93, 0) 

    def drawBaseballSeams(self, centralObject, droneName, step,numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 5)
    
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 10)
    
    def quit(self):
        sys.exit()


app = MyApp()
app.run()
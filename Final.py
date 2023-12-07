# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:03:43 2023

@author: antho
"""


import pygame, simpleGE, random

class GAME(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("background.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Old Western Shoot-Out")
        
        self.sndShoot = simpleGE.Sound("shoot.mp3")
        pygame.mixer.music.load("backgroundSND.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        
        self.hand = []
        for i in range(2):
            Hands = HANDS(self)
            Hands.setPosition((150 + (i * 350), 150))
            self.hand.append(Hands)
            
        self.btnShoot = BtnShoot()
        self.lblScore = LblScore()
        self.userScore = 0
        
        self.sprites = [self.hand, self.btnShoot, self.lblScore]
    
    def update(self):
        if self.btnShoot.clicked:
            self.sndShoot.play()
            for Hands in self.hand:
                result = Hands.shoot()
                if result == "win":
                    self.userScore += 1
                    self.lblScore.text = f"Score: {self.userScore}" 
       
class HANDS(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("rock.png")
        self.setSize(120, 120)
        
        self.images = [None,
                       pygame.image.load("rock.png"),
                       pygame.image.load("paper.jpg"),
                       pygame.image.load("scissor.png"),
                       ]
        
        for i in range(1, 4):
            self.images[i] = pygame.transform.scale(self.images[i], (120, 120))
    
    def shoot(self):
        self.value = random.randint(1, 3)
        self.imageMaster = self.images[self.value]
        computer_value = random.randint(1, 3)
        
        outcomes = {
            (1, 1): "tie", (2, 2): "tie", (3, 3): "tie",
            (1, 3): "win", (2, 1): "win", (3, 2): "win"
        }
        
        if self.value == computer_value:
            return "tie"
        elif (self.value, computer_value) in outcomes and outcomes[(self.value, computer_value)] == "win":
            return "win" 
        else:
            return "lose"

class BtnShoot(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((320, 240))
        self.text = "Shoot"

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (100, 50)
        self.text = "Score: 0"

def main():
    game = GAME()
    game.start()

if __name__ == "__main__":
    main()

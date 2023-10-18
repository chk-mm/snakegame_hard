from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self,fruit):
        super().__init__()
        if fruit:
            self.shape(fruit[random.randint(0,len(fruit)-1)])
            # self.shape(fruit)
        else:
            self.color('blue')
            self.shape('circle')
        self.pu()
        self.fruitpic = fruit

    def food_pos(self):
        self.shape(self.fruitpic[random.randint(0, len(self.fruitpic) - 1)])
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def food_name_score(self):
        for s in self.fruitpic:
            print("x")

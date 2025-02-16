import random
import time
import turtle

from Shape import Shape
from Text import Text


class Game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor("white")
        self.win.title("Catch the Circles!")
        self.win.tracer(0)
        self.shapes = []
        self.score = 0
        self.duration = 30
        self.start_time = time.time()
        self.score_text = Text(-200, 250, f"Score: {self.duration}")
        self.timer_text = Text(200, 250, f"time: {self.duration}")
    def create_shape(self):
        x = random.randint(-250, 250)
        y  = 250
        shape = random.choice(["circle", "square", "triangle"])
        color = random.choice(["red", "blue", "green"])
        new_shape = Shape(x, y, shape, color)
        new_shape.show()
        self.shapes.append(new_shape)
    def move_shape(self):
        for shape in self.shapes:
            shape.move()
            if shape.shape.ycor() < -250:
                self.shapes.remove(shape)
                shape.hide()
    def on_shape_click(self, x, y):
        for shape in self.shapes:
            if shape.shape.distance(x, y) < 40 and shape.shape.shape() == "circle":
                self.shapes.remove(shape)
                shape.hide()
                self.score += 1
            elif shape.shape.distance(x, y) < 40 and shape.shape.shape() != "circle":
                self.shape.remove(shape)
                shape.hide()
                self.score -= 1
            self.score_text.write_text(f"Score: {self.score}")
    def update_timer(self):
        time_passed = int(time.time() - self.start_time)
        time_left = max(0, self.duration - time_passed)
        self.timer_text.write_text(f"Time: {time_left}")
        return time_left > 0
    def start(self):
        self.win.listen()
        self.win.onclick(self.on_shape_click)
        while self.update_timer():
            self.win.update()
            self.create_shape()
            self.move_shape()
            time.sleep(0.1)
        self.win.textinput("Game over!", f"Highest Score: (self.score)")

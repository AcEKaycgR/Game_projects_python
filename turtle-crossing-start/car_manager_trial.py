from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
starting_positions = [290, 310, 330]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.Car = []
        self.All_CAR = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            self.Car = []
            car_color = random.choice(COLORS)
            for position in starting_positions:
                new_car = Turtle()
                new_car.penup()
                new_car.shape("square")
                new_car.color(car_color)
                y = random.randint(-250, 250)
                new_car.goto(position, y)
                self.Car.append(new_car)
            self.All_CAR.append(self.Car)

    def move_cars(self):
        for cars in self.All_CAR:
            for car in range(len(self.Car) - 1, 0, -1):
                new_x = cars[car - 1].xcor()
                new_y = cars[car - 1].ycor()
                cars[car].goto(new_x, new_y)
            cars[0].backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

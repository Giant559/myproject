class Car(object):
    condition = 'New'
    def __init__(self,brand,color,speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def drive(self):
        self.condition = 'Used'

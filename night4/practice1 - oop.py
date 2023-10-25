class Human:
    def __init__(self, name, hair="", color_eye=""):
        print("start create human")
        self.name = name
        self.hair = hair
        self.color_eye = color_eye

    def walk(self):
        print(self.name, "Walking")

    def run(self):
        print(self.name, "Running")

    def details(self):
        print(self.name, "has a ", self.hair, "hair and", self.color_eye, "eyes")


fatima = Human("Fatima", hair="curly", color_eye="brown")
fatima.walk()
fatima.run()
fatima.details()

abolfazl = Human("Abolfazl", color_eye="Brown")
abolfazl.details()

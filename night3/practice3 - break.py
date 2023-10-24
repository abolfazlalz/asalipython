animals = ['lion', 'cheetah', 'tiger']

def feed_animal(animal_name):
  if animal_name in animals:
    print("I feed", animal_name)
    return
  print("not found")

feed_animal("lion")
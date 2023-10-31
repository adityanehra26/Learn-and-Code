import random
class Human:
    def __init__(self, name='Unknown', age=0, height=0.0, weight=0.0):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self._water_intake = 0
        self._food_intake_calories = 0
        self._required_food = 2000  # No of calories
        self._required_water = 4   # in liters

    def mouth(self, **kwargs):
        if 'water' in kwargs.keys():
            print('water taken')
            if self._water_intake + kwargs['water'] > self._required_water:
                print("Caution! Extreme water intake")
                return "vomit\n"
            return self.stomach(kwargs['water'], 0)

        if 'food' in kwargs.keys():
            print('food is taken')
            if self._food_intake_calories + kwargs['food'] > self._required_food:
                print("Caution! Extreme food intake")
                return "vomit\n"
            return self.stomach(0, kwargs['food'])

    def stomach(self, water=0, food=0):
        self._water_intake += water
        self._food_intake_calories += food

        if water:
            print("Water is inside stomach")
            water_percentage_for_elimination = water*random.randint(50,60)/100
            return self.bladder(water_percentage_for_elimination)

        food_percentage_for_elimination = food * random.randint(35, 40)/100
        return self.large_intestine(food_percentage_for_elimination)

    def bladder(self, urine):
        return f"Urine is generated : {urine} litter\n"

    def large_intestine(self, feces):
        return f"Feces is generated: {feces} Calories\n"



        



new_human_obj = Human('Aditya', 20, 180, 81)

print(new_human_obj.mouth(water=2))
print(new_human_obj.mouth(water=2))
print(new_human_obj.mouth(water=2))

print(new_human_obj.mouth(food=1500))



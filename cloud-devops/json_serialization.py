import json
import answer

with open('cars.json', 'r') as f:
    cars = json.load(f)

with open('fruits.json', 'r') as f:
    fruits = json.load(f)

if __name__ == '__main__':
    serialized_cars = answer.serialize(cars)
    print('Serialized cars:')
    for k, v in serialized_cars.items():
        print(k, '=', v)
    print('')
    serialized_fruits = answer.serialize(fruits)
    print('Serialized fruits:')
    for k, v in serialized_fruits.items():
        print(k, '=', v)

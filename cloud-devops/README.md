# Simple Everyday Problems
Overly simple everyday problems to check if you even can code.

## Problem 1: JSON Pretty Print
You received a bit of JSON data in [cars.json](cars.json) and [fruits.json](fruits.json) and you just want to format it nicely so that for each value in the document, the nested path for it would be clearly visible.

Example:
```
python json_serialization.py
Serialized cars:
toyota.wheels.0 = big
toyota.wheels.1 = small
toyota.models.0.corolla.color.light = grey
toyota.models.0.corolla.color.dark = blue

Serialized fruits:
banana.colors.0 = green
banana.colors.1 = yellow
banana.tastes.ripe = sweet
banana.tastes.raw = sour
```

Lucky for you, everything is set up for you!

All you need to do is to open `answer.py` fill in the contents for `def serialize(data):`. The function needs to return a  dictionary where both keys and values are simple strings.
Example:
```
return {
    "toyota.wheels.0": "big",
    "toyota.wheels.1": small
}
```
The same function must work for both cars and fruits.


Testing:
```
python3 json_serialization.py
```

Good luck!

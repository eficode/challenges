# JSON Transformation endpoints

This challenge is about nesting and flattening json data.

## Overview
The task is to expose 2 http(s) endpoints:
```
<url_of_your_choice>/nest
<url_of_your_choice>/flatten
```

## About the "flatten" endpoint

When a user sends any json data to `<url_of_your_choice>/flatten`, the response must be the flattened version of the data.

### Example
There are some JSON data in [cars.json](cars.json) and [fruits.json](fruits.json). If those contents are sent to the flatten endpoint, it should return a flattened version of the data so that for each value in the document, the nested path for it would be clearly visible.

Sending cars.json must produce this output:
```
{
  "toyota.wheels.0": "big",
  "toyota.wheels.1": "small",
  "toyota.models.0.corolla.color.light": "grey",
  "toyota.models.0.corolla.color.dark": "blue"
}
```

Sending fruits.json must produce this output:
```
{
  "banana.colors.0": "green",
  "banana.colors.1": "yellow",
  "banana.tastes.ripe": "sweet",
  "banana.tastes.raw": "sour"
}

```

### Getting started with the "flatten" endpoint

This folder contains a frame for implementing flattening logic locally in Python. If you prefer another language, please feel free to use any. 

If you wish to try implementing flattening logic in python you need to do is to open `answer.py` fill in the contents for `def serialize(data):`. The function needs to return a dictionary where both keys and values are simple strings.
Example:
```
return {
  "toyota.wheels.0": "big",
  "toyota.wheels.1": small
}
```
Obviously the same function must work for both cars and fruits (or any other json).

Testing:
```
python3 json_serialization.py
```

## About the "nest" endpoint

When a user sends any flattened json data to `<url_of_your_choice>/nest`, the response must be the nested ("normal") version of the data.

Nest is flatten in reverse. If a user submits any json to `flatten` endpoint, they get the flattened version of that json. If they then submit the flattened json to the `nest` endpoint, the response must be the original json. So flatten is nest in reverse and vice versa.

## Extra notes
- For simplicity it's ok to assume that none of the JSON keys contain dots. But feel free to escape dots if you want to.
- It doesn't matter which http request types you use. As long as it works.
- Could be cool to have 2 serverless functions exposed by an api gateway. But there's no single correct way. Could just as well be a container running somewhere.
- You can try to implement the logic as a one-liner. It's possible.
- Would be cool to also have a UI if anyone needs to flatten or nest their json.


Have fun!

from flask import Flask
d = [
    {
        "number":1,
        "name": "Mahesh",
        "age": 25,
        "city": "Bangalore",
        "country": "India"
    },
    {
        "number":2,
        "name": "Alex",
        "age": 26,
        "city": "London",
        "country": "UK"
    },
    {
        "number":3,
        "name": "David",
        "age": 27,
        "city": "San Francisco",
        "country": "USA"
    },
     {
        "number":4,
        "name": "Jonh",
        "age": 28,
        "city": "Toronto",
        "country": "Canada"
    },
     {
        "number":5,
        "name": "Cris",
        "age": 29,
        "city": "Paris",
        "country": "France"
    }
]
app = Flask(__name__)

@app.route('/')
def index():
    return d

app.run()
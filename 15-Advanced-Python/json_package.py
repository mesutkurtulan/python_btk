import json

# dictionary
personDictionary = {"name": "Jane", "language":["java", "python"]}
print(personDictionary["name"])   # Jane
print(personDictionary["language"]) # ["java", "python"]
print(personDictionary["language"][0]) # java

# json string to dictionary
personString = '{"name": "Jane", "language":["java", "python"]}'
result = json.loads(personString)
print(result)   # {'name': 'Jane', 'language': ['java', 'python']}
print(result["name"])   # Jane
print(result["language"]) # ["java", "python"]
print(result["language"][0]) # java

# json file to dictionary
with open("person.json") as f:
    data = json.load(f)
    print(data) # {'name': 'Jane', 'language': ['java', 'python']}
    print(type(data))   # <class 'dict'>

# Dictionary to json string
result = json.dumps(personDictionary)
print(result)   # {"name": "Jane", "language": ["java", "python"]}
print(type(result)) # <class 'str'>

result = json.dumps(personDictionary, indent=4)
print(result)
'''
{
    "name": "Jane",
    "language": [
        "java",
        "python"
    ]
}
'''
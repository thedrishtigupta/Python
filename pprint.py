import json
import pprint

# Example complex data
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'hiking', 'coding'],
    'address': {
        'street': '123 Maple St',
        'city': 'Wonderland',
        'zipcode': '12345'
    }
}

# Convert the data to a JSON string with indentation for readability
formatted_data = json.dumps(data, indent=4)

# Write the formatted data to a file
with open('data.json', 'w') as file:
    file.write(formatted_data)

print("Data has been written to data.json")

# Read the data back from the file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print("Data has been loaded from data.json")
print(loaded_data)
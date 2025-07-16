# dict_methods_examples.py

# Creating a dictionary
person = {
    "name": "Zahra",
    "age": 22,
    "city": "Rabat"
}

# 1. get()
print("1. get():", person.get("name"))  # Zahra

# 2. keys()
print("2. keys():", person.keys())  # dict_keys(['name', 'age', 'city'])

# 3. values()
print("3. values():", person.values())  # dict_values(['Zahra', 22, 'Rabat'])

# 4. items()
print("4. items():", person.items())  # dict_items([('name', 'Zahra'), ...])

# 5. pop()
print("5. pop():", person.pop("age"))  # 22
print("   After pop:", person)

# 6. update()
person.update({"country": "Morocco"})
print("6. update():", person)

# 7. clear()
person.clear()
print("7. clear():", person)  # {}

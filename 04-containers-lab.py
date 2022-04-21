# ## Exercises

# #### Exercise 1
# - Create a list named `students` containing some student names (strings).
# - Print out the second student's name.
# - Print out the last student's name.

students = ['Charlie', 'Roger', 'Fred']
print(students[1])
print(students[-1])

# #### Exercise 2
# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
# - Use a `for` loop to print out the string "_food goes here_ is a good food".
foods = ('Burgers', 'Sushi', 'Steak')
for food in foods:
	print(f"{food} is a good food")

# #### Exercise 3
# - Using a `for` loop, print just the last two food strings from `foods`.
for food in foods[-2:]:
	print(food)

# #### Exercise 4
# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"
home_town = {
	'city': 'Seattle',
	'state': 'Washington',
	'population': 1000000
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# #### Exercise 5
# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"
for key, value in home_town.items():
	print(f"{key} = {value}")

# #### Exercise 6
# - Create an empty list named `cohort`.
# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:

# 	```python
# 	{
# 	  'student': 'Tina',
# 	  'fav_food' 'Cheeseburger'
# 	}
# 	```
# - Iterate over `cohort` printing out each element.
cohort = []

for i, student in enumerate(students):
  cohort.append({
    'student': student,
    'fav_food': foods[i]
  })

for student in cohort:
  print(student)

# #### Exercise 7
# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.
awesome_students = [f"{name} is awesome!" for name in students]

for student in awesome_students:
  print(student)

# #### Exercise 8
# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.

for food in [food for food in foods if 'a' in food]:
  print(food)










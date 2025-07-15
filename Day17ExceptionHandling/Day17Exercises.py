# Exercises: Day 17

"""names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively."""

names = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Estonia", "Russia"]
nordic_countries, es, ru = names[:5], names[5], names[6]
print(nordic_countries)
print(es)
print(ru)

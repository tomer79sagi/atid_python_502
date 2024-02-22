data = [
    {"name": "Alice", "hobbies": ["reading", "traveling"], "colors": {"red", "blue"}},
    {"name": "Bob", "hobbies": ["cooking", "reading"], "colors": {"blue", "green"}},
    {"name": "Charlie", "hobbies": ["traveling", "cooking"], "colors": {"yellow"}}
]


def extract_unique_names(list_people):

    unique_names = set({})
    hobby_list = []

    for person in list_people:
        # (1) Unique names
        unique_names.add(person['name'])

        # (2) Hobbies (duplicates allowed)
        # hobby_list.append(person['hobbies'])  # Doesn't work, creates lists of lists
        hobby_list.extend(person['hobbies'])

    return {
        'unique_names': unique_names,
        'hobbies': hobby_list
    }

u_names = extract_unique_names(data)
print(u_names)
def my_profile(name, second_name, *grades, **contact_details):
    print("Name: " + name)
    print(grades)
    print(contact_details)


my_profile("Tomer Sagi", "George", 77, 88, 76, 96, phone="052888444", email="me@tomersagi.com")

from inmanta.plugins import plugin

@plugin
def hello():
    print("Hello World! - Plugin")

@plugin
def upper(value: "string") -> "string":
    return value.upper()


@plugin
def is_employee(person: "example_module::services::Employee") -> "bool":
    if person.name == 'Piotr Tutak':
        return True
    return False

"""
@plugin
def is_employer(person: "Person") -> "bool":
    if person.name == "Przemyslaw Wawrzynczak":
        return True
    return False
"""

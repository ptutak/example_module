from inmanta.plugins import plugin
from inmanta.resources import resource, Resource
import os

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

@plugin
def out(employee_list: "example_module::services::Employee[]") -> "std::none":
    print(employee_list[0].__dict__['__instance'])
    print(employee_list[0]._get_instance().get_attribute('name').get_value())



class TestResourceImpl:
    @staticmethod
    def get_name(exporter, obj):
        print("get_name method from resource called")
        return obj.name

    @staticmethod
    def get_status(exporter, obj):
        print("get_status method called")
        return "this is a return value from get_status method"

    @staticmethod
    def get_some_field(exporter, obj):
        print('get_some_field method called')
        return "this is a return value from get_some_field method"


@resource('example_module::services::TestResource', id_attribute='name', agent='agent_name_field')
class TestResource(Resource):
    fields = ('name', 'status', 'some_field')
    map = {
        "some_field": TestResourceImpl.get_some_field,
        "name": TestResourceImpl.get_name,
        "status": TestResourceImpl.get_status}

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

@resource('example_module::services::TestResource', id_attribute='name', agent='host.name')
class TestResource(Resource):
    fields = ('name', 'status')

    @staticmethod
    def get_name(exporter, obj):
        return obj.name

    @staticmethod
    def get_status(exporter, obj):
        return "{:o}".format(os.stat(obj.name)[0])[-3:]

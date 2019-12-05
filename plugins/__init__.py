from inmanta.plugins import plugin
from inmanta.agent.handler import provider, HandlerContext, CRUDHandler, InvalidOperation
from inmanta.resources import resource, Resource, PurgeableResource
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

    @staticmethod
    def get_field(exporter, obj):
        print('get_field method called')
        obj_names = []
        for x in obj.field:
            obj_names.append(x.name)
        return str(obj_names)

@resource('example_module::services::TestResource', id_attribute='name', agent='agent_name_field')
class TestResource(PurgeableResource):
    fields = ('name', 'status', 'some_field', 'field')
    map = {
        "some_field": TestResourceImpl.get_some_field,
        "name": TestResourceImpl.get_name,
        "status": TestResourceImpl.get_status,
        "field": TestResourceImpl.get_field}


@provider('example_module::services::TestResource', name='test_resource')
class TestResourceHandler(CRUDHandler):
    def read_resource(self, context: HandlerContext, resource: TestResource) -> None:
        context.info(str(resource))
        print(resource.purged)
        print("SJSJSJS")
        context.info("HELLO")
        if self._io.file_exists(resource.name):
            resource.content = self._io.read(resource.name)
        raise InvalidOperation("No such file")

    def create_resource(self, context: HandlerContext, resource: TestResource) -> None:
        if self._io.file_exists(resource.name):
            self.update_resource(context, resource)
            context.set_created()
            return
        self._io.put(resource.name, resource.content)
        context.set_created()

    def update_resource(self, context: HandlerContext, resource: TestResource) -> None:
        if self._io.file_exists(resource.name):
            self._io.put(resource.name, resource.content)
            context.set_updated()
        raise InvalidOperation("No such file")

    def delete_resource(self, context: HandlerContext, resource: TestResource) -> None:
        if self._io.file_exists(resource.name):
            self._io.remove(resource.name)
        context.set_purged()

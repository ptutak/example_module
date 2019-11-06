from inmanta.plugins import plugin

@plugin
def hello():
    print("Hello World! - Plugin")

@plugin
def upper(value: "string") -> "string":
    return value.upper()

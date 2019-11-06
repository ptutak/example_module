def test_upper(project):
    text = "hello"
    assert project.get_plugin_function("upper")(text) == "HELLO"

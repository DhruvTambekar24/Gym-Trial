from app.tools.class_tool import list_classes

def test_list_classes():
    classes = list_classes()
    assert isinstance(classes, list)

import pytest

from tethys import example


def test_function_with_types_in_docstring():
    assert example.function_with_types_in_docstring(1, 'two') is True


def test_function_with_pep484_type_annotations():
    assert example.function_with_pep484_type_annotations(1, 'two') is True


def test_module_level_function_pass():
    assert example.module_level_function(1, 2) is True


def test_module_level_function_fail():
    with pytest.raises(ValueError):
        example.module_level_function(1, 1)


def test_example_generator():
    assert list(example.example_generator(4)) == [0, 1, 2, 3]


def test_example_error():
    with pytest.raises(example.ExampleError):
        raise example.ExampleError('Internal Server Error', 500)


def test_example_class():
    c = example.ExampleClass('test', 200, ['hello', 'world'])
    c.readwrite_property = 'foo'
    assert c.readonly_property == 'readonly_property'
    assert c.readwrite_property == 'foo'
    assert c.example_method(1, 2) is True
    assert c.__special__() is None
    assert c.__special_without_docstring__() is None
    assert c._private() is None
    assert c._private_without_docstring() is None

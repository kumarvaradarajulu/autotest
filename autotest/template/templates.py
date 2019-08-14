import ast
import unittest
import codegen
import mock

new_test_class_template = """
import unittest
import {module_path}
class Test{filename}(unittest.TestCase):
    \"\"\" Test  cases for {filename} \"\"\"
    def setUp(self):
        pass
"""

coverage_config = """
[report]
show_missing = True
"""

new_class = """
class Test{classname}(unittest.TestCase):
    \"\"\" Test  cases for {classname} \"\"\"
    def setUp(self):
        pass
"""


new_function = """
class Test{functionname_camel}(unittest.TestCase):
    \"\"\" Test  cases for {functionname} \"\"\"
    def setUp(self):
        pass
    
    def test_{functionname}(self):
        pass
"""


new_method = """
def test_{methodname}(self):
    pass
"""


template_types = {
    "new_test_class": new_test_class_template,
    "coverage_config": coverage_config,
    "new_class": new_class,
    "new_method": new_method,
    "new_function": new_function,
}


class TemplateCreator(object):
    def __init__(self, template_type, module_path, filename, **kwargs):
        """

        Args:
            template_type:
            write_to_file:
            module_path:
            filename:
        """
        self.template_type = template_type
        self.module_path = module_path
        self.filename = filename
        self.template = template_types[template_type]
        kwargs.update({
            "template_type": template_type,
            "module_path": module_path,
            "filename": filename
        })
        self.kwargs = kwargs

    def create_template(self, write_to_file=False,):
        tree = ast.parse(self.template.format(**self.kwargs))
        if write_to_file:
            with open('test_{}.py'.format(self.filename), 'w') as f:
                f.write(codegen.to_source(tree))
        return tree

    def create_coverage_config(self):
        with open('.coveragerc', 'w') as f:
            f.write(template_types['coverage_config'])


def create_template(template_type, **kwargs):
    return ast.parse(template_types[template_type].format(**kwargs))

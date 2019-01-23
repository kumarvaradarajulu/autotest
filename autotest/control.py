import sys
from coverage import Coverage
from template.templates import TemplateCreator


class Controller(object):
    """ Controller that controls the execution of the script """
    def __init__(self, options):
        """ """
        self.module_package_path = options.module_package_name

    def process(self):
        """ """
        # TODO: Check if user gave module or package name for the testing.
        # TODO: If user gave a module name need to search for all tests where this module if being tested and
        #  nosetests coverage needs to be run for all such tests to get accurate coverage data
        """ Implementation here """

        # TODO: For now we deal only with new files. Create a new test case file so it can be run to get the missing lines for our module
        module_package_name = self.module_package_path
        if ("/" in module_package_name or "\\" in module_package_name) and module_package_name.endswith(".py"):
            module_package_name = module_package_name.split(".py")[0]
        module_path = module_package_name.replace("/", ".")
        filename = module_path.split(".")[-1]
        templ_creator = TemplateCreator(template_type="new_test_class", module_path=module_path, filename=filename)
        templ_creator.create_coverage_config()
        templ_creator.create_template(write_to_file=True)
        test_file = 'test_{}.py'.format(filename)
        coverage = Coverage()
        missing_lines = coverage.get_missing_lines(filename, self.module_package_path)

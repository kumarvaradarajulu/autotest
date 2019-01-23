from autotest import astwrapper


class Generator(object):
    """ Process the missing lines and tries to add psuedo code for test scenarios """
    def __init__(self, module_path):
        self.ast_wrapper = astwrapper.AstModuleWrapper(module_path)

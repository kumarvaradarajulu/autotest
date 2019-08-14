import os
import subprocess
import re


class Coverage(object):
    """

    """
    def __init__(self):
        """ Get coverage data """
        # TODO: For now only implementing file analysis
        pass

    def get_coverage(self, filename):
        test_file_path = os.path.join(os.path.expanduser('~'), 'test1.log')
        # TODO: nosetests within virtualenv is not recognized, need to fix it
        subprocess.Popen('nosetests {filename} --with-coverage &>{test_file_path}'.format(filename=filename, test_file_path=test_file_path), shell=True, stdout=subprocess.PIPE)
        with open(test_file_path) as f:
            log_lines = f.readlines()
        return log_lines

    def get_missing_lines(self, filename, module_package_path, full_path):
        """

        Returns:

        """
        module_package_path = module_package_path + '.py' if '.py' not in module_package_path else ''
        coverage_data = self.get_coverage(filename)
        start = False
        missing_lines = {}
        for line in coverage_data:
            # Ignore reporting decoration lines
            if line.startswith('----------------'):
                continue
            if not start:
                if re.match(r'.*?Name.*?Stmts.*?Miss.*?Cover.*?Missing.*', line):
                    # This marks the start of coverage report
                    start = True
            if start:
                # Check if its the end
                if 'TOTAL' in line:
                    end = True
                    break
                cols = line.split('   ')
                if not cols[0] in (module_package_path, full_path):
                    # We are only interested in our module skip others
                    # TODO: We can expand to return missing files for all modules that was not asked for
                    continue
                missing_lines[module_package_path] = cols[-1].replace('\n', '')
        return missing_lines

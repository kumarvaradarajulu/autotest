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
        subprocess.Popen('nosetests {filename} --with-coverage &>~/test1.log'.format(filename=self.filename), shell=True, stdout=subprocess.PIPE)
        with open('test1.log') as f:
            log_lines = f.readlines()
        return log_lines

    def get_missing_lines(self, filename, module_package_path):
        """

        Returns:

        """
        coverage_data = self.get_coverage(filename)
        start = True
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
                cols = line[14].split('   ')
                if not cols[0] == module_package_path:
                    # We are only interested in our module skip others
                    # TODO: We can expand to return missing files for all modules that was not asked for
                    continue
                missing_lines[module_package_path] = cols[-1].replace('\n', '')
        return missing_lines

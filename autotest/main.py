import argparse
import logging
import sys

import six
#import autotest.__VERSION__
from control import Controller

logging.basicConfig(level=logging.ERROR)
log = logging.getLogger('')
logging.getLogger('sh').setLevel(logging.ERROR)

VERBOSITY_MAPPING = {
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}

parser = argparse.ArgumentParser(prog='AutoTest')

parser.add_argument('module_package_name',
                    help='Module name to be analyzed and written tests for')

parser.add_argument('--vcs',
                    dest='vcs',
                    default='git',
                    type=six.text_type,
                    help='VCS to be used')

parser.add_argument('-v', '--verbose',
                    action='count',
                    default=0,
                    help='Control verbosity level. Can be supplied multiple times to increase verbosity level',)

parser.add_argument('-V', '--version', action='version', version='%(prog)s v' + '1.0a',
                    help='Displays AutoTest version number',)


def main():
    args = parser.parse_args()
    log.setLevel(VERBOSITY_MAPPING.get(args.verbose, VERBOSITY_MAPPING[0]))
    log.debug("Verbosity Level={}".format(args.verbose))

    try:
        Controller(options=args).process()
    except (EnvironmentError, NotImplementedError, RuntimeError) as e:
        sys.stdout.write(six.text_type(e.message) + '\n')
        sys.exit(False)

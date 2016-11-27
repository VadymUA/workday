"""
Sample usage, command line:
  app_cli.py 1 2 3 4 5 6 12

Expected result looks like:
  1 * 2 * 6 = 12

You can extend few parameters to 'app.conf' file. There are default values:
  limit = 1024
  params = 7
"""

import os
import sys
from app_lib import Matrix, Keymap, Calculator

def main():
    config_body = {}
    config_name = 'app.conf'
    application_path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    config_file = os.path.join(application_path, config_name)

    try:
        execfile(config_file, config_body)
        params = config_body['params']
        limit = config_body['limit']
    except:
        raise IOError("Config file {} is absent".format(config_name))

    if len(sys.argv) > 1:
        if len(sys.argv[1:]) != params:
            raise ValueError(
                "Number of arguments is not as expected ({0} instead of {1})".format(len(sys.argv[1:]), params)
            )
        target = int(sys.argv[params])
        numbers = map(int, sys.argv[1:params])
        for _i in numbers + [target]:
            if _i > limit:
                raise ValueError("All input numbers should be under {}".format(limit))
    else:
        return "Usage: {0} {1}".format(sys.argv[0], ' '.join([str(x) for x in range(1, params+1)]))

    calculator = Calculator(numbers, target, Matrix(numbers, target, Keymap(numbers), limit))
    return calculator.get_result()

if __name__ == '__main__':
    run = main()
    print run

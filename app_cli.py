#! /usr/bin/python2.7
#

'''
Maintainer: VadymT <help2any1@gmail.com>

Sample usage, command line:
  app_cli.py 1 2 3 4 5 6 12

Expected result looks like:
  1 * 2 * 6 = 12

You can extend few parameters in 'app.conf' file. There are default values:
  limit = 1024
  params = 7
'''

import sys
from app_lib import Matrix, Keymap, Calculator

def main():
    config = {}
    cfile = "app.conf"
    try:
        execfile(cfile, config)
    except:
        raise IOError("Config file '%s' is absent" % cfile)
    else:
        execfile("app.conf", config)
        params = config['params']
        limit = config['limit']

    if len(sys.argv) > 1:
        if len(sys.argv[1:]) != params:
            raise ValueError(
                "Number of arguments is not as expected (%s instead of %s)" % (len(sys.argv[1:]), params)
            )
        target = int(sys.argv[params])
        numbers = map(int, sys.argv[1:params])
        for _i in numbers + [target]:
            if _i > limit:
                raise ValueError("All input numbers should be under %s" % limit)
    else:
        return "Usage: %s %s" % (sys.argv[0], ' '.join([str(x) for x in range(1, params+1)]))

    calculator = Calculator(numbers, target, Matrix(numbers, target, Keymap(numbers), limit))
    return calculator.get_result()

if __name__ == '__main__':
    print main()

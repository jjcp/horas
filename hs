#!/usr/bin/env python3

import sys
from horas import Horas


def main():
    if len(sys.argv) > 1:
        hs = Horas()
        comando = sys.argv[1]

        if comando == 'inicio':
            hs.inicio(' '.join(sys.argv[2:]))
        elif comando == 'fin':
            hs.fin()
        elif comando == 'reporte':
            hs.reporte()
        else:
            sys.stdout.write('comando erróneo: %s\n' % comando)
    else:
        sys.stdout.write('hs inicio <nombre>\n'
                         'hs fin\n'
                         'hs reporte\n')


if __name__ == '__main__':
    main()

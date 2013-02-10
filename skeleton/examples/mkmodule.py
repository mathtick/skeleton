#!/usr/bin/env python3
"""
Basic script to create an empty python package containing one module
"""
from skeleton import Skeleton, Var

import os
myname = os.path.realpath(__file__)
mypath = os.path.dirname(myname)
myname = os.path.basename(myname)

class BasicModule(Skeleton):
    """
    Create an empty module with its etup script and a README file.
    """
    src = os.path.join(mypath, 'basic-module')
    variables = [
        Var('module_name'),
        Var('author'),
        Var('author_email'),
        ]


def main():
    """Basic command line bootstrap for the BasicModule Skeleton"""
    BasicModule.cmd()

if __name__ == '__main__':
    main()

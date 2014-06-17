#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    with open('settings_env.txt') as f:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f.read().strip())

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import inspect
import json
import os
import platform
import sys

for name, value in inspect.getmembers(platform):
    if name[0] != '_' and callable(value):
        try:
            value = value()
        except (IndexError, TypeError):
            continue
        if str(value).strip("( ,')"):
            print('{:>21}() = {}'.format(name, value))

print(sys.platform, sys.version)
print(json.dump(os.environs, indent=4))

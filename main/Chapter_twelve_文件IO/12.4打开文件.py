from pathlib import *


if __name__ == '__main__':
    file = open(Path('./testDir/a_test.py'))
    print(file.encoding)
    print(file.mode)
    print(file.closed)
    file.close()
    print(file.closed)
    print(file.name)


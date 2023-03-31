import sys
import time

from nyanlang.nyan import NyanEngine

def run():
    print("Hello World")
    NyanEngine.add_keyword("힛", breakpoint_handler)
    match sys.argv:
        case [_, _, f]:
            ne = NyanEngine(f, debug=True)
            ne.run()

def breakpoint_handler():
    dest = time.time() + 5
    while time.time() < dest:
        pass
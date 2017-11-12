# -*- encoding: utf-8 -*-

import sys
import json

def read_in():
    line = sys.stdin.readline()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(line)

if __name__ == "__main__":
    lines = read_in()
    pgn = lines['PGNtoAnalyze']
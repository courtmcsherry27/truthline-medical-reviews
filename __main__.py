#!/usr/bin/env python3
import os, sys
sys.path.insert(0,os.path.dirname(__file__))
from setup import main
sys.exit(main() or 0)

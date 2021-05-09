#!/usr/bin/env python3

# imports
import os
import re
import time
import random
import logging
import urllib.parse
import urllib.request
import http.cookiejar
import concurrent.futures

from pathlib import Path
from datetime import datetime
from argparse import FileType
from argparse import SUPPRESS
from argparse import ArgumentError
from argparse import ArgumentParser

NAME = "wpcrack brute forcing tool"
BANNER= "WPCRACK" % (NAME)

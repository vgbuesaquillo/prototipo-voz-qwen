import logging
import sys

def setup_logging(debug: bool = False):
    level = logging.DEBUG if debug else logging.INFO
    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    logging.basicConfig(level=level, format=fmt, handlers=[logging.StreamHandler(sys.stdout)])

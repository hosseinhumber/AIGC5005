"""Part 2: logging instead of printing.

Run:  python logging_demo.py
"""
import logging

# One logger per module, named after the module, created at the top of the file.
logger = logging.getLogger(__name__)


def process(items: list[int]) -> int:
    logger.debug("Processing %d items", len(items))     # %s style: built only if the level is on
    total = 0
    for item in items:
        if item < 0:
            logger.warning("Skipping negative value %d", item)
            continue
        total += item
    logger.info("Total is %d", total)
    return total


# Configure logging once, at the program's entry point, never inside a library module.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
)

process([3, -1, 4])

try:
    1 / 0
except ZeroDivisionError:
    # logger.exception logs at ERROR level and includes the traceback.
    logger.exception("The calculation failed")

logger.critical("This level is for failures the program cannot recover from")

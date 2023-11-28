"""Override some production settings for tests."""
import os

from .settings import *  # noqa: F403  # we really want to import everything

DATABASES["default"]["NAME"] = os.environ.get(  # noqa: F405  # overriding settings on purpose
    "BCZA_TEST_DB", "db.tests"
)

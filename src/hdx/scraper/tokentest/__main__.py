"""Entry point to start HAPI HNO pipeline"""

import logging
from os.path import expanduser, join

from ._version import __version__
from hdx.data.user import User
from hdx.facades.simple import facade
from hdx.utilities.easy_logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

lookup = "hdx-scraper-tokentest"
updated_by_script = "HDX Scraper: Token Test"


def main() -> None:
    """Test token

    Returns:
        None
    """
    logger.info(f"##### {lookup} version {__version__} ####")
    User.check_current_user_write_access("hdx")
    logger.info("HDX Scraper token test completed!")


if __name__ == "__main__":
    facade(
        main,
        user_agent_config_yaml=join(expanduser("~"), ".useragents.yaml"),
        user_agent_lookup=lookup,
    )

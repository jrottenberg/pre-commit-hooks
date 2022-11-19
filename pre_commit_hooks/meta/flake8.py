# update flake8 repo


import re


def adjust_flake8_url(pre_commit_config: str) -> str:
    flake8_regexp = re.compile('gitlab.com\\/pycqa\\/flake8', re.IGNORECASE)
    return re.sub(flake8_regexp, "github.com/pycqa/flake8", pre_commit_config)


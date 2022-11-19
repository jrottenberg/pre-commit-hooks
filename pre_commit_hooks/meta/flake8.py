# update flake8 repo


import re


def adjust_flake8_url(pre_commit_config: str) -> int:
    flake8_regexp = re.compile("gitlab.com/pycqa/flake8", re.IGNORECASE)
    return re.sub(flake8_regexp, pre_commit_config)


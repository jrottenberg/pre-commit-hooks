# update flake8 repo


import re
import ruamel


def adjust_flake8_url(pre_commit_config: ruamel.yaml.comments.CommentedMap) -> ruamel.yaml.comments.CommentedMap:
    flake8_regexp = re.compile('gitlab.com\\/pycqa\\/flake8', re.IGNORECASE)

    i = 0
    for item in pre_commit_config['repos']:
        replacement = re.sub(flake8_regexp, "github.com/pycqa/flake8",item['repo'])
        pre_commit_config['repos'][i]['repo'] = replacement
        i += 1
    return pre_commit_config


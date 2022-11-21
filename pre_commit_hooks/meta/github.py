# update github repo


import re
import ruamel


def replace_github_protocol(pre_commit_config: ruamel.yaml.comments.CommentedMap) -> ruamel.yaml.comments.CommentedMap:
    github_regexp = re.compile('git:\\/\\/github.com', re.IGNORECASE)
    i = 0
    for item in pre_commit_config['repos']:
        replacement = re.sub(github_regexp, "https://github.com", item['repo'])
        print(replacement)
        pre_commit_config['repos'][i].repo = replacement
        i += 1
    return pre_commit_config


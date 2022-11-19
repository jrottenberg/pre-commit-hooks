# update flake8 repo 


import re 
import ruamel.yaml

from pre_commit_hooks.utils import cmd_output, get_all_tags, highest_version

yaml = ruamel.yaml.YAML()

yaml.indent(mapping=2, sequence=4, offset=2)


def adjust_flake8_url(pre_commit_config_path: str) -> int:

    with open(pre_commit_config_path) as pre_commit_config:
        original_pre_commit_config = yaml.load(
            pre_commit_config,
        )

    flake8_regexp  = re.compile("gitlab.com/PyCQA/flake8", re.IGNORECASE)
    
    updated_pre_commit_config  = flake8_regexp.sub("github.com/pycqa/flake8", original_pre_commit_config)
    
    if updated_pre_commit_config == original_pre_commit_config:
        return 0
    else:
        with open(pre_commit_config_path, "w") as pre_commit_config:
            yaml.dump(updated_pre_commit_config, pre_commit_config) 
        return 1

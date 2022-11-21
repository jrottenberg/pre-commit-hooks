import argparse
import sys
from pathlib import Path
import io 

import ruamel.yaml

from pre_commit_hooks.meta.pycqa import adjust_pycqa_url
from pre_commit_hooks.meta.github import replace_github_protocol


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="""Where to find the config ?""")
    parser.add_argument(
        "--pre-commit-config",
        dest="PRE_COMMIT_CONFIG",
        default=".pre-commit-config.yaml",
        help="Where is the .pre-commit-config config located",
    )

    args, _ = parser.parse_known_args()

    pre_commit_config_path = Path(args.PRE_COMMIT_CONFIG)

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)

    
    if not pre_commit_config_path.exists():
        return 1

    with open(pre_commit_config_path) as pre_commit_config_file:
        pre_commit_config = yaml.load(
            pre_commit_config_file,
        )

    original_pre_commit_config = pre_commit_config
    adjust_pycqa_url(pre_commit_config)
    replace_github_protocol(pre_commit_config)
   
    
    original = io.BytesIO()
    yaml.dump(original_pre_commit_config, original)
    replaced = io.BytesIO()
    yaml.dump(pre_commit_config, replaced)


    if original.getvalue() != replaced.getvalue():
        with open(pre_commit_config_path, "w") as pre_commit_config_file:
            yaml.dump(pre_commit_config, pre_commit_config_file) 
        


if __name__ == "__main__":
    sys.exit(main())

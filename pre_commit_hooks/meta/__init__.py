import argparse
import sys
from pathlib import Path

# from pre_commit_hooks.meta.github import replace_github_protocol
import ruamel.yaml

from pre_commit_hooks.meta.flake8 import adjust_flake8_url


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=""" """)
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

    retval = 0

    if not pre_commit_config_path.exists():
        return 1

    with open(pre_commit_config_path) as pre_commit_config:
        original_pre_commit_config = yaml.load(
            pre_commit_config,
        )

    flake8_pre_commit_config = adjust_flake8_url(original_pre_commit_config)

    if flake8_pre_commit_config != original_pre_commit_config:
        retval += 1
        original_pre_commit_config = flake8_pre_commit_config

    # replace_github_protocol(pre_commit_config)

    if retval > 0:
        with open(pre_commit_config_path, "w") as pre_commit_config:
            yaml.dump(original_pre_commit_config, pre_commit_config) 

    return retval

if __name__ == "__main__":
    sys.exit(main())

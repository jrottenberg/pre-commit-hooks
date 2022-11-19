import argparse
import sys
from pathlib import Path

from pre_commit_hooks.meta.flake8 import adjust_flake8_url
# from pre_commit_hooks.meta.github import replace_github_protocol


def main(argv=None):
    parser = argparse.ArgumentParser(description=""" """)
    parser.add_argument(
        "--pre-commit-config",
        dest="PRE_COMMIT_CONFIG",
        default=".pre-commit-config.yaml",
        help="Where is the .pre-commit-config config located",
    )

    args, _ = parser.parse_known_args()

    pre_commit_config = Path(args.PRE_COMMIT_CONFIG)
    if pre_commit_config.exists():
        adjust_flake8_url(pre_commit_config)
        # replace_github_protocol(pre_commit_config)


if __name__ == "__main__":
    sys.exit(main())

import argparse
import sys
from pathlib import Path

from pre_commit_hooks.pinned_update.gitlab_ci import update_gitlab_ci


def main(argv=None):
    parser = argparse.ArgumentParser(description=""" """)
    parser.add_argument(
        "--gitlab-ci",
        dest="GITLAB_CI_FILE",
        default=".gitlab-ci.yml",
        help="Where is the gitlab-ci config located",
    )

    args, unknown = parser.parse_known_args()

    gitlab_ci = Path(args.GITLAB_CI_FILE)
    if gitlab_ci.exists():
        update_gitlab_ci(gitlab_ci)


if __name__ == "__main__":
    sys.exit(main())

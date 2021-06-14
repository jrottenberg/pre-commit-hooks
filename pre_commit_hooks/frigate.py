import argparse
import os
import sys
from pathlib import Path

from frigate.gen import gen


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="""Run frigate nd replace the entire
                       README.md file each chart folder."""
    )
    parser.add_argument(
        "--output",
        dest="output",
        default="README.md",
        help="Where to store the result file",
    )
    parser.add_argument(
        "--no-credits",
        dest="nocredits",
        required=False,
        default=True,
        help="Disable the Frigate credits",
    )

    parser.add_argument(
        "--no-deps",
        dest="nodeps",
        required=False,
        default=True,
        help="Do not render dependency values",
    )

    parser.add_argument(
        "--format",
        dest="format",
        default="markdown",
        help="Disable the Frigate credits",
    )

    args, unknown = parser.parse_known_args()
    dirs = []
    path = os.getcwd()
    name = "Chart.yaml"

    retval = 0
    charts = []

    # Find all the charts
    for root, dirs, files in os.walk(path):
        if name in files:
            charts.append(os.path.join(root, name))

    # For each chart
    for chart in charts:
        chart_location = os.path.dirname(chart)
        frigate_output = gen(
            chart_location, args.format, credits=args.nocredits, deps=args.nodeps
        )
        artifact = Path(chart_location, args.output)
        Path(artifact).touch()
        with open(artifact, "r") as before:
            current_output = before.read()
        if current_output != frigate_output:
            retval += 1
            with open(artifact, "w") as generated:
                generated.write(frigate_output)
    return retval


if __name__ == "__main__":
    sys.exit(main())

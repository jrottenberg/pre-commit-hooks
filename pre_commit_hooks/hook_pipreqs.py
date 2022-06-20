import argparse
import os
import sys
import logging
from pathlib import Path
# from distutils.core import run_setup
from setuptools.sandbox import run_setup
from pipreqs import pipreqs
from pep517 import meta


def normalize(src):
    src = list(map(lambda x: x.lower().replace("_", "-"), src))
    return set(src)

def main():  # pragma: no cover
    parser = argparse.ArgumentParser(
        description="""Compare packages discovered with pipreqs in code and setup.py"""
    )    
    parser.add_argument(
        "--debug",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="How verbose should we be ?",
    )    
    args = parser.parse_args()    
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')
    logging.getLogger("pep5217").setLevel(logging.WARNING)


    target_path="/Users/Julien.Rottenberg/git/mpl/ms-core/msprod"
    code_requires = pipreqs.get_all_imports(target_path)
    code_package_requires = pipreqs.get_pkg_names(code_requires)
    try:
        code_package_requires.remove("setuptools")
    except ValueError:
        pass

    code_package_requires = normalize(code_package_requires)
    logging.debug(f"Found packages used in code : {list(code_package_requires)}")


    result = meta.load(target_path)
    setup_package_requires = setup_requires = list(filter(lambda x: 'extra ==' not in x, result.requires))
    setup_package_requires = normalize( setup_package_requires)


    logging.debug(f"Found packages in setup.py : {list(setup_package_requires)}")

    non_used_packages = setup_package_requires.difference(code_package_requires)
    missing_packages = code_package_requires.difference(setup_package_requires)
    exit_error = 0
    if non_used_packages != set():
        logging.error(f"You have packages in setup.py that are not used in code: {non_used_packages}")
        exit_error = 1

    if missing_packages != set():
        logging.error(f"You have python code using packages not defined in setup.py {missing_packages}")
        exit_error = 1


if __name__ == '__main__':
    main()  # pragma: no cover
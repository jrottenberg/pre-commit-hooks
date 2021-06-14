from setuptools import find_packages, setup

setup(
    name="pre-commit-terraform",
    description="Pre-commit hooks for frigate_replace",
    url="https://github.com",
    version_format="{tag}+{gitsha}",
    author="Contributors",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(exclude=("tests*", "testing*")),
    install_requires=[
        "frigate",
    ],
    entry_points={
        "console_scripts": [
            "frigate_replace = pre_commit_hooks.frigate:main",
        ],
    },
)

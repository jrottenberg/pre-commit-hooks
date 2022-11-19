from setuptools import find_packages, setup

setup(
    name="pre-commit-hooks",
    description="Pre-commit hooks",
    url="https://github.com/jrottenberg/pre-commit-hooks",
    version_format="{tag}",
    author="Julien Rottenberg",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(exclude=("tests*", "testing*")),
    install_requires=["ruamel.yaml", "packaging"],
    entry_points={
        "console_scripts": [
            "pinned_update = pre_commit_hooks.pinned_update:main",
            "meta = pre_commit_hooks.meta:main",
        ],
    },
)

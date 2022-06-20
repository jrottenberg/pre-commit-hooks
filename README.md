# Pre-commit-hooks

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Installation


Step into the repository you want to have the pre-commit hooks installed and run:


```
cat <<EOF > .pre-commit-config.yaml
repos:
- repo: https://github.com/jrottenberg/pre-commit-hooks
  rev: v1.0.0 #  pre-commit update  - to keep the version up to date
  hooks:
    - id: frigate
EOF
```

## Hooks


### Pifreqs


Leverage [pifreqs](https://github.com/bndr/pipreqs) to validate the required packages in code versus in setup.py
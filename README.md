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


### Frigate


Run [frigate](https://github.com/rapidsai/frigate) against the detected chart(s) in the repository and create/update
a README.md file in the same folder.

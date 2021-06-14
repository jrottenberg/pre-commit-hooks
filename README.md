# Pre-commit-hooks


## Installation


Step into the repository you want to have the pre-commit hooks installed and run:

cat <<EOF > .pre-commit-config.yaml
repos:
- repo: https://github.com/jrottenberg/pre-commit-hooks
  rev: main #  pre-commit update  - to keep the version up to date
  hooks:
    - id: frigate
EOF


## hooks


### Frigate



Run [frigate](https://github.com/rapidsai/frigate) against the detected chart in the repository and create/update
a README.md file in the same folder.

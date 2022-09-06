# Pre-commit-hooks


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


### Pinned Update


WIP: Update any pinned version discovered in the project.

#### Current

 - Gitlab-ci


#### Next

 - Dockerfile

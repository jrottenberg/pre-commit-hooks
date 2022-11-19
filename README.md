# Pre-commit-hooks


## Installation


Step into the repository you want to have the pre-commit hooks installed and run:


```
cat <<EOF > .pre-commit-config.yaml
repos:
- repo: https://github.com/jrottenberg/pre-commit-hooks
  rev: v1.0.0 #  pre-commit update  - to keep the version up to date
  hooks:
    - id: pinned_update
EOF
```

## Hooks


### Pinned Update


WIP: Update any pinned version discovered in the project.

#### Current

 - Gitlab-ci


#### Next

 - Dockerfile




### Meta

Adjust `.pre-commit-config.yaml` for various little bugs that pre-commit won't fix :

 - [pre-commit fails to install flake8 hook](https://github.com/pre-commit/pre-commit/issues/2596) - repo moved from gitlab to github
 - [Autoupdate to correct references of "git://github.com/"](https://github.com/pre-commit/pre-commit/issues/2212) - github stopped support for unauthenticated git protocol

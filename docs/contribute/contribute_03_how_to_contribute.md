# How to contribute

Each repository should have at least the following branches:

 - main: the latest stable release
 - dev: the development branch used to do the integration tests of new commits
  
Other branches are optional and on the behalf of the [repository maintainers](../01_projects_overview.md)

If you want to contribute code please follow the follwing process

- create or pick an issue in the repository you want to contribute to
- assign yourslef to this issue
- [fork the repsitory](__create_a_fork.md) dev branch into your account
- make sure to follow the special code development guidelines if those exist
- make your changes
- create a pull request against the dev branch
- add at least one maintainer as reviewer

Once the PR against the dev-branch is accepted integration tests will be done and if successful the the dev branch is merged into main branch. 
The detailed process is on behalf of the repo maintainers

## General recommendation

To avoid incorrect commits (e.g. not lint-clean code) it is recommended to use tools like [pre-commit](https://pre-commit.com)
This tool has several plug-ins for checking the code compliance. See special guidelines below for details.
pre-commit is always running when running git-commit. The commit will only be accepted, if pre-commit returns without error. This is useful to reduce the number of invalid commits. 
This is most useful if code has to be lint-clean.

## Special guidelines

- [Ansible Development guidelines](__ansible_dev_guidelines.md)
- [Installing pre-commit](__install_pre_commit.md)

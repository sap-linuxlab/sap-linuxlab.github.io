# Participate in a Project

All members of the Open Source Community are welcome to contribute to the SAP LinuxLab Open-Source Initiative, by using each individual Project's GitHub Repository to create GitHub Issues or GitHub Pull Requests.

Development roadmaps for each project are available upon request. Core developers of each project use GitHub Issues to track bugs and feature requests.

To request maintainer status, use [GitHub Discussions](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions). For all code contributions, use GitHub Issues and Pull Requests on the respective project's repository.

## Contribution workflow with GitHub

The SAP LinuxLab Open-Source Initiative uses [fork-based git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).

The majority of existing Projects use a simplified code contribution process to feel familiar to SAP practitioners:

- Each GitHub Repository will have a `main` branch (effectively "Production") and use Git Tags to define individual Git Releases.
- Each GitHub Repository will have a `dev` branch where code development contributions are merged into and tested (effectively "Integration Test").
- Each developer will fork the repository into a personal GitHub Repository, and create their own branch e.g. `new-feat001` (effectively "Sandbox"); which are merged into the aforementioned `dev` branch using a GitHub Pull Request.

At a high-level, the steps in sequence to add code contributions is therefore:

- [Fork the GitHub Repository](./create_a_fork.md) for which you want to make a contribution
- Create a separate branch for the work
- Create a GitHub Pull Request back to the original GitHub Repository
- Adjust the work based on comments received
- Await the merge of the GitHub Pull Request by another committer

## Related guides

- [Developer Guidelines](./developer_guidelines.md)
- [Install pre-commit](./install_pre_commit.md)
- [Ansible Dev Guidelines](./ansible_dev_guidelines.md)
- [Governance](../initiative_governance.md) — maintainers and naming conventions

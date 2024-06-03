# Initiative Contributions

Contributions from the community are important to the long-term benefit of the SAP LinuxLab Open-Source Initiative.

Such contributions can be code development, code review and testing / feedback (bugs, better-ifs, feature requests). This can include submission of an entire Project / Code Repository into the ownership of SAP LinuxLab Open-Source Initiative.

## Contributors to the community

All members of the Open Source Community are welcome to contribute to the SAP LinuxLab Open-Source Initiative, by using each individual Project's GitHub Repository to create GitHub Issues or GitHub Pull Requests.

Regular contributors to a Project are awarded maintainer status, and play a more active role in the long-term development of the Project. To be awarded maintainer status, self-nomination via an existing maintainer is permitted - although existing maintainers proactively embrace contributors and this is likely to happen automatically. All maintainer requests are approved by the SAP LinuxLab Open-Source Initiative's Governance Board.

New Project / Code Repository submissions are firstly reviewed by an existing Project Maintainer, and then submitted to the SAP LinuxLab Open-Source Initiative's Governance Board for approval; the approval is largely based upon the validation the new project does not duplicate the intent of another.

To request new project contributions and maintainer status, please use the [GitHub Discussion of the SAP LinuxLab Open-Source Initiative's website](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions). For all other contributions, please use the GitHub Issues on the respective Project's GitHub Repository.

## Contribution workflow with GitHub

The SAP LinuxLab Open-Source Initiative uses [fork-based git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).

The majority of existing Projects use a simplified code contribution process to feel familiar to SAP practitioners:

- Each GitHub Repository will have a `main` branch (effectively "Production") and use Git Tags to define individual Git Releases.
- Each GitHub Repository will have a `dev` branch where code development contributions are merged into and tested (effectively "Integration Test").
- Each developer will fork the repository into a personal GitHub Repository, and create their own branch e.g. `new-feat001` (effectively "Sandbox"); which are merged into the aforementioned `dev` branch using a GitHub Pull Request.

At a high-level, the steps in sequence to add code contributions is therefore:

- [Fork the GitHub Repository](./initiative_contribute/__create_a_fork.md) for which you want to make a contribution
- Create a separate branch for the work
- Create a GitHub Pull Request back to the original GitHub Repository
- Adjust the work based on comments received
- Await the merge of the GitHub Pull Request by another committer

## General guidance for contributions

When making a contribution to a Project within the SAP LinuxLab Open-Source Initiative, please try to utilize the following set of developer guidelines.

Please note, these developer guidelines may require more practice with using Git tooling (such as squashing commits):

Do:

- Keep it simple
- Follow coding style guides where they exist
- Write tests or show test evidence when applicable
- Review existing content in order to avoid overwriting existing content
- Create documentation, especially for new features and functionality
- Discuss with other committers whenever you are unsure of something
- Engage with the community and with contributors
- Squash commits whenever possible
- Use `pre-commit` to avoid pushing non-standardized code
- Avoid incorrect commits, by using Linter tools to check code syntax or CodeSpell for spelling mistakes; for example [Ansible Development guidelines](./initiative_contribute/__ansible_dev_guidelines.md).

Don’t:

- Commit directly or open pull request to the `main` branch
- Merge pull requests you have authored yourself, wait for a code review by another member
- Break existing functionality
- Ignore requests for assistance

## Governance Board

The SAP LinuxLab Open-Source Initiative is managed by a Governance Board that consists of at least one person of each foundation company. This board helps to keep vendor neutrality, approve new contributions and define roadmap, structure and other rules (e.g. naming conventions).

The Governance Board meets on a monthly cadence.

[See the current list of participating companies](./initiative_participating_companies.md), the list does not include those companies who actively use and provide feedback but do not actively provide code contributions.

## Maintainers

For each Project's GitHub Repository under the SAP LinuxLab Open-Source Initiative, one or two responsible maintainers are elected. The maintainers take responsibility for the roadmap of the repository they maintain.

On larger Projects (e.g. `sap_install` Ansible Collection), maintainers are defined by sub-component of the Project (keeping with the example, Ansible Roles each have a maintainer within the Ansible Collection).

Each maintainer is responsible for watching, commenting and prioritizing GitHub Issues and GitHub Pull Requests in a timely manner.

## Project Naming Conventions

To aid new-users easily finding content, Project GitHub Repositories follow naming convention prefixes. Often the prefix is the technology used, unless an existing nomenclature exists for the given technology (e.g. Ansible uses prefix `community.` for community upstream Ansible Collections).

| Category | Content type | Prefix |
|:---|:---|:---|
| Automation (Infrastructure-as-Code) | Terraform Templates (and Modules) | `terraform.`*description* |
| | Kubernetes (Source-to-Image) | `k8s.`*description* |
| Automation (Configuration-as-Code) | Ansible Collections (and Roles or Modules) | `community.`*collection_name* |
|  | Salt | `salt.`*description* |
| Shell scripts | Tools and Utilities | `tool.`*description* |
| Documentation | Architectures | `architecture.`*sap_product_name* <sub>*(1..n Solution Architectures)*</sub> |
| Special Topics | High Availability | `high-availability.`*description* |
| Misc. | Demos and Examples | `demo.`*description* |

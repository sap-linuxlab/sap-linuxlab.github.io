# Submit a New Repository

We are glad you are thinking about contributing a new project to SAP LinuxLab. Whether you are an SAP customer, service partner, or technology partner — if your automation helps the SAP on Linux community, we want to hear from you.

!!! tip "You are welcome here"
    New ideas strengthen the initiative. Taking a few minutes to prepare your repository using the checklist below helps us review your submission quickly and get you connected with the right maintainers.

To start a submission, open a thread in [GitHub Discussions](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions). New repositories are reviewed by an existing maintainer and then approved by the [Governance Board](../initiative_contributions.md#governance-board).

## Is this the right path?

| Your goal | Where to go |
|:---|:---|
| Fix a bug, add a feature, or open a pull request in an **existing** repository | Use GitHub Issues and Pull Requests on that project, or follow the [Fork a Repository](./__create_a_fork.md) guide |
| Submit a **whole new repository** to join SAP LinuxLab | Read this page, prepare your README, then open a [GitHub Discussion](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions) |

## What we look for

The following criteria help us publish consistent, trustworthy automation for the community. Use them as a self-review before you submit.

### Code quality and ownership

- [ ] **Human-reviewed code** — AI-assisted development is welcome, but all code must be reviewed by a human before submission.
- [ ] **Human understanding and responsibility** — Submitters must fully understand what the code does and be willing to take responsibility for it as maintainers.
- [ ] **Human-authored code** — Code should be authored and owned by humans; AI may assist, but must not be submitted unchecked.

### Documentation and language

- [ ] **English README and comments** — README and code comments must be in English so the whole community can collaborate.
- [ ] **README disclaimer** — Every README must include a **Disclaimer** section covering:
    - Supported platforms
    - Testing coverage
    - Constraints and limitations
    - A clear statement that users should **use the software at their own responsibility**
- [ ] **Consistent README structure** — Follow the [README template](#readme-templates-by-repository-type) for your repository type.

### Platform and license

- [ ] **Designed for RHEL and/or SLES** — Solutions should target Red Hat Enterprise Linux for SAP Solutions and/or SUSE Linux Enterprise Server for SAP applications. State which operating systems you support in your README.
- [ ] **License compliance** — The repository must match SAP LinuxLab license requirements, typically the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## README templates by repository type

Choose the template that best matches your project. Copy the structure into your repository's `README.md` before submitting.

| Repository prefix | Template | Example |
|:---|:---|:---|
| `community.*` (Ansible Collection) | [Ansible Collection README template](../readme_templates/readme_ansible_collection.md) | [community.sap_install](https://github.com/sap-linuxlab/community.sap_install) |
| Ansible Playbooks (e.g. `ansible.playbooks_for_sap`) | [Ansible Playbooks README template](../readme_templates/readme_ansible_playbooks.md) | [ansible.playbooks_for_sap](https://github.com/sap-linuxlab/ansible.playbooks_for_sap) |
| `terraform.*`, `tool.*`, `demo.*`, and others | Start from the closest template above and note any gaps in your Discussion post | — |

For repository naming conventions, see [Project Naming Conventions](../initiative_contributions.md#project-naming-conventions).

## Before you submit — quick checklist

- [ ] Code has been human-reviewed (including any AI-assisted parts)
- [ ] Maintainers understand the code and accept responsibility for it
- [ ] README and comments are in English
- [ ] README follows the correct template and includes a Disclaimer
- [ ] Supported platforms (RHEL and/or SLES) are documented
- [ ] Testing coverage and limitations are documented
- [ ] Apache 2.0 (or approved) license is in place
- [ ] Repository name follows SAP LinuxLab naming conventions

## What happens next

1. Open a [GitHub Discussion](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions) with your proposed repository name, type, and a link to your repository.
2. An existing maintainer reviews your submission for quality and checks that it does not duplicate another project.
3. The Governance Board approves the submission.
4. The repository is created or transferred under the [sap-linuxlab](https://github.com/sap-linuxlab) organization.

## Related guides

- [Initiative Contributions](../initiative_contributions.md) — governance, maintainers, and naming conventions
- [Ansible Development Guidelines](./__ansible_dev_guidelines.md) — coding style for `community.*` Ansible collections
- [Install pre-commit](./__install_pre_commit.md) — recommended tooling for consistent commits
- [Fork a Repository](./__create_a_fork.md) — for contributing to existing projects

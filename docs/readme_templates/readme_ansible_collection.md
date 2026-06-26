# Ansible Collection README Template

!!! note "How to use this template"
    Copy the structure below into your repository's `README.md` before submitting a new project to SAP LinuxLab. Replace all placeholder text marked with `<!-- ... -->` comments.

    **Based on:** [community.sap_install](https://github.com/sap-linuxlab/community.sap_install) and [community.sap_launchpad](https://github.com/sap-linuxlab/community.sap_launchpad)

---

```markdown
# community.<name> Ansible Collection

![Ansible Lint](https://github.com/sap-linuxlab/community.<name>/actions/workflows/ansible-lint.yml/badge.svg?branch=main)

## Description

<!-- Briefly describe what this collection does and which SAP scenarios it supports. -->

## Requirements

### Control Nodes

| Type | Version |
| :--- | :--- |
| Operating system | <!-- e.g. Any OS with required Python and Ansible versions --> |
| Python | <!-- e.g. 3.11 or higher --> |
| Ansible | <!-- e.g. 12 or higher --> |
| Ansible-core | <!-- e.g. 2.18 or higher --> |

### Managed Nodes

| Type | Version |
| :--- | :--- |
| Operating system | <!-- Red Hat Enterprise Linux for SAP Solutions 8.x, 9.x, 10.x and/or SUSE Linux Enterprise Server for SAP applications 15 SPx, 16.x --> |
| Python | <!-- e.g. 3.9 or higher --> |

> **Managed Node Registration**  
> Operating system needs to have access to required package repositories either directly or via subscription registration.

## Installation Instructions

### Installation

Install this collection with Ansible Galaxy:

\`\`\`console
ansible-galaxy collection install community.<name>
\`\`\`

Optionally include the collection in a `requirements.yml` file:

\`\`\`yaml
collections:
  - name: community.<name>
\`\`\`

### Upgrade

\`\`\`console
ansible-galaxy collection install community.<name> --upgrade
\`\`\`

## Contents

### Ansible Roles

| Name | Summary |
| :--- | :--- |
| [<role_name>](<!-- link to role -->) | <!-- One-line description --> |

### Ansible Modules

| Name | Summary |
| :--- | :--- |
| [<module_name>](<!-- link to module docs -->) | <!-- One-line description --> |

## Testing

<!-- Describe what you tested: operating systems, SAP products, and scenarios. -->

| Type | Version |
| :--- | :--- |
| Operating system | <!-- RHEL for SAP / SLES for SAP versions tested --> |
| SAP products | <!-- e.g. SAP S/4HANA, SAP HANA --> |
| Scenarios | <!-- e.g. sandbox, distributed, HA --> |

> **Testing Disclaimer**  
> <!-- State what was and was not tested. It is not possible to test every OS and SAP product combination with every release. -->

## Disclaimer

<!-- Required for SAP LinuxLab repositories. -->

This Ansible Collection provides automation for SAP-related tasks. It is intended to accelerate common activities and can be extended to meet specific requirements.

**Supported platforms:** <!-- List RHEL for SAP and/or SLES for SAP versions -->

**Testing coverage:** <!-- Summarise what combinations were tested -->

**Constraints and limitations:** <!-- Known limits, experimental features, dependencies -->

**Use at your own responsibility.** Always refer to official SAP documentation and validate automation in your own environment before production use.

## Contributing

For information on how to contribute, please see our [contribution guidelines](https://sap-linuxlab.github.io/contribute/).

## Contributors

We welcome contributions to this collection. For a list of all contributors and information on how you can get involved, please see our [CONTRIBUTORS document](./CONTRIBUTORS.md).

## Support

You can report any issues using [GitHub Issues](https://github.com/sap-linuxlab/community.<name>/issues).

## Release Notes and Roadmap

You can find the release notes of this collection in the [Changelog file](./CHANGELOG.rst).

## License

[Apache 2.0](./LICENSE)
```

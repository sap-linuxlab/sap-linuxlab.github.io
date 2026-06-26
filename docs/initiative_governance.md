# Governance

## Governance Board

The SAP LinuxLab Open-Source Initiative is managed by a Governance Board that consists of at least one person of each foundation company. This board helps to keep vendor neutrality, approve new contributions and define roadmap, structure and other rules (e.g. naming conventions).

The Governance Board meets on a monthly cadence.

[See the current list of participating companies](./initiative_participating_companies.md). The list does not include those companies who actively use and provide feedback but do not actively provide code contributions.

For how to contribute to the initiative, see the [Contribute](./contribute/index.md) section.

## Maintainers

For each Project's GitHub Repository under the SAP LinuxLab Open-Source Initiative, one or two responsible maintainers are elected. The maintainers take responsibility for the roadmap of the repository they maintain.

On larger Projects (e.g. `sap_install` Ansible Collection), maintainers are defined by sub-component of the Project (keeping with the example, Ansible Roles each have a maintainer within the Ansible Collection).

Each maintainer is responsible for watching, commenting and prioritizing GitHub Issues and GitHub Pull Requests in a timely manner.

Regular contributors to a Project are awarded maintainer status, and play a more active role in the long-term development of the Project. To be awarded maintainer status, self-nomination via an existing maintainer is permitted — although existing maintainers proactively embrace contributors and this is likely to happen automatically. All maintainer requests are approved by the Governance Board.

Each repository lists its maintainers in `CONTRIBUTORS.md` on GitHub. Browse the [sap-linuxlab organization](https://github.com/sap-linuxlab) to find individual projects and their maintainers.

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

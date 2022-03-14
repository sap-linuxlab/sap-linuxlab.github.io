# Project Naming Conventions

The content in this github organization should be easy to find. that's why repositories should have meaningful names, so that it is easy to find content.

The content repositories contain will be prefixed according the following schema, so that it is easy to understand what a repository contains

| Category | Content type | Prefix |
|:---|:---|:---|
| Automation (Infrastructure-as-Code) | Terraform Templates (and Modules) | `terraform.`*description* |
| | Kubernetes (Source-to-Image) | `k8s.`*description* |
| Automation (Configuration-as-Code) | Ansible Collections (and Roles or Modules) | `community.`*collection_name* |
|  | Salt | `salt.`*description* |
| Shell scripts | Tools and Utilities | `tool.`*description* |
| Documentation | Architectures | `architecture.`*sap_product_name* <sub>*(assumes Solution Architectures)*</sub> |
| Misc. | Demos and Examples | `demo.`*description* |

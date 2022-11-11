# Development Guidelines

<!---  ## Terraform Templates and Modules for SAP --->

## Ansible Collections and Roles for SAP

### Blocks and Tasks

All blocks and tasks must be named and must have a unique name in each role.

### Variable Naming

Role variables must be named as follows (example role name: sample_role)

- Role external variables start with the role name, as in:
```
sample_role_required_packages
```

- Role internal variables start with two underscores, followed by the role name, as in:
```
__sample_role_required_packages
```

- Role variables which store the result of a set_fact has the string "_fact" after the role name part, as in:
```
__sample_role_fact_required_packages
```

- Role variables which store the result of a function other than set_fact has the string "_register" after the role name part, as in:
```
__sample_role_register_installed_packages
```

### Ansible-lint Cleaning

Only ansible-lint clean collections can be imported into Ansible Galaxy.

- Always install and use the latest version of ansible-lint. As of 02-Dec-2021, it's ansible-lint-5.3.0. Install with:
```
# pip3 install ansible-lint --user
```

- Put the following two files in the home directory of each role:
  - [.ansible-lint](https://github.com/berndfinger/sap-preconfigure/blob/bz2003630/.ansible-lint)
  - [.yamllint.yml](https://github.com/berndfinger/sap-preconfigure/blob/bz2003630/.yamllint.yml)

The files are configured to enforce most default ansible-lint rules but skip others based on certain development requirements and experiences.

- Put the following file into directory .github/workflow of each role:
  - [.github/workflows/ansible-lint.yml](https://github.com/berndfinger/sap-preconfigure/blob/bz2003630/.github/workflows/ansible-lint.yml)

This will trigger an ansible-lint v. 5.3.0 run in a freshly created virtual system on GitHub after each git push or pull request.

- For skipping certain ansible-lint checks for certain tasks only, follow the chapter "False Positives: Skipping Rules" in [https://ansible-lint.readthedocs.io/en/latest/rules.html](https://ansible-lint.readthedocs.io/en/latest/rules.html):

Add `# noqa` after the task name, followed by a space and the rule name from [Default Rules](https://ansible-lint.readthedocs.io/en/latest/default_rules.html), e.g. `package-latest`. Also add a line starting with `# Reason for noqa:`, followed by a space and a short explanation on why ansible-lint should not report a failure for the rule in this case.
Example: [This line and the following one](https://github.com/berndfinger/sap-hana-preconfigure/blob/5be04d3a1b3f64b1966075896d9f7428fbf70a0b/tasks/RedHat/installation.yml#L83) in file tasks/RedHat/installation.yml of role sap-hana-preconfigure.

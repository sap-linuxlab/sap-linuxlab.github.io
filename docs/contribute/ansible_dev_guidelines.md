# Development Guidelines

<!---  ## Terraform Templates and Modules for SAP --->

## Ansible Collections and Roles for SAP

### Blocks and Tasks

All blocks and tasks must be named and must have a unique name in each role.

### Variable Naming

Role variables must be named as follows (example role name: sample_role)

- Role external variables start with the role name, as in:
```yaml
sample_role_required_packages: ''
```

- Role internal variables start with two underscores, followed by the role name, as in:
```yaml
__sample_role_required_packages: ''
```

- Role variables which store the result of a set_fact has the string "_fact" after the role name part, as in:
```yaml
__sample_role_fact_required_packages: ''
```

- Role variables which store the result of a function other than set_fact has the string "_register" after the role name part, as in:
```yaml
__sample_role_register_installed_packages: ''
```

### Ansible-lint Cleaning

Only ansible-lint clean Ansible Collections can be imported into Ansible Galaxy.

Then the linting files `.ansible-lint` and `.yamllint.yml` are automatically maintained and installed by any `git clone` or `git pull` request. 
The correct linting version is maintained by the `.pre-commit-config.yml` file.

If you do not want to use pre-commit follow this guideline:

- Always install and use the latest version of ansible-lint. You can find the latest release version [here](https://github.com/ansible-community/ansible-lint/releases/).
Install with:
```shell
pip3 install ansible-lint --user
```

- Put the following two files in the home directory of each role, such as:
  - [.ansible-lint](https://github.com/sap-linuxlab/community.sap_install/tree/main/roles/sap_general_preconfigure/.ansible-lint)
  - [.yamllint.yml](https://github.com/sap-linuxlab/community.sap_install/tree/main/roles/sap_general_preconfigure/.yamllint.yml)

The files are configured to enforce most default ansible-lint rules but skip others based on certain development requirements and experiences.

- Put the following file into directory .github/workflow of each role, such as:
  - [.github/workflows/ansible-lint.yml](https://github.com/sap-linuxlab/community.sap_install/tree/main/roles/sap_general_preconfigure/.github/workflows/)

This will trigger an ansible-lint run in a freshly created virtual system on GitHub after each git push or pull request.

- For skipping certain ansible-lint checks for certain tasks only, follow the chapter "False Positives: Skipping Rules" in [https://ansible-lint.readthedocs.io/en/latest/rules.html](https://ansible-lint.readthedocs.io/en/latest/rules.html):

Add `# noqa` after the task name, followed by a space and the rule name from [Default Rules](https://ansible-lint.readthedocs.io/en/latest/default_rules.html), e.g. `package-latest`. Also add a line starting with `# Reason for noqa:`, followed by a space and a short explanation on why ansible-lint should not report a failure for the rule in this case.

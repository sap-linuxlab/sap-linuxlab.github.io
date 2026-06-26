# Developer Guidelines

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
- Use [pre-commit](./install_pre_commit.md) to avoid pushing non-standardized code
- Avoid incorrect commits, by using Linter tools to check code syntax or CodeSpell for spelling mistakes; for example [Ansible Development guidelines](./ansible_dev_guidelines.md).

Don't:

- Commit directly or open pull request to the `main` branch
- Merge pull requests you have authored yourself, wait for a code review by another member
- Break existing functionality
- Ignore requests for assistance

## Related guides

- [Participate in a Project](./participate.md)
- [Fork a Repository](./create_a_fork.md)

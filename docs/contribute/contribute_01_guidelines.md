# Contribution Guidelines

Contributions from the community play an important role in the assets associated with the SAP LinuxLab GitHub repositories.

## Contributions and Committers
All members of the Open Source Community are welcome to contribute to the SAP GitHub organization repositories. Contributions to the repositories can be achieved through a variety of methods including source code contributions, reviews and issue creation.

Individuals who are interested in directly affecting repository content may request the privilege in becoming a maintainer in one or more repository for which they have made contributions in the past.
Committers play an important role within our community and act as an extension of the core teams to help facilitate key initiatives that benefit the entire community as a whole. These individuals may [request mainteiner status](../form_request_apply_as_maintainer.md) or be nominated by another member of the community for being maintainer. All requests will be reviewed by the board members along with the maintainers who are associated to a repository.

If you have a complete new idea you want to have implemented, please contact the board
 and ask yourself if you are willing to maintain this piece of code and if you want to apply for a seat in the board. If you are not able to code, go to the [discussion space](https://github.com/sap-linuxlab/sap-linuxlab.github.io/discussions) and leave your input there.
 If you have pre-existing code you want to move to the SAP LinuxLab GitHub organization please fill out [this form](../form_request_submit_new_content.md)

## Understanding Our Workflow
While there are multiple development styles, the SAP LinuxLab GitHUb community typically follows a [fork-based git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) that is common in many Open Source projects. At a high level, this style consists of the following actions:

- Fork the repository for which you want to make a contribution
- Create a separate branch for the work
- Create a pull request back to the originating repository being sure to follow any specific guidelines outlined in the repository
- Adjust the work based on comments received
- Await the merge by another committer

The following guides are available to learn more about this process and start contributing:

1. [Local Setup](contribution/localsetup)
2. [Contributing Code (Opening a Pull Request)](contribution/createPR)
3. [Testing a Pull Request](contribution/testPR)
4. [Opening a Pull Request Against A Pull Request](contribution/openPR)

## General Guidance

When making a contribution to the repositories of the SAP LinuxLab organization, try to utilize the following set of guidelines outlined in this section. Committers should adhere to these practices as they attempt to address many (but not all) of the primary concerns associated with open source repositories and project management:

Do:

- Squash commits whenever possible
- Engage with the community and with contributors
- Write tests when applicable
- Discuss with other committers whenever you are unsure of something
- Create documentation, especially for new features and functionality
- Review existing content in order to avoid overwriting existing content
- Follow coding style guides where they exist
- Keep it simple

Don’t:

- Commit directly to the master branch
- Merge pull requests you have authored
- Break existing functionality
- Ignore requests for assistance
- Go against established repository norms

## The Board

The SAP LinuxLab project is managed by a governor board that consists of at least one person of each foundation member.

Companies that add projects (repositories) may apply for a seat in the governor board. This board decides on roadmaps, structure and other generic rules such as naming conventions etc. of this project.

The board meets on a monthly cadence internally and with the maintainers to review progress.

[Press here to view the current participating companies](../05_participating_companies.md)

## Maintainer

For each github repository in this project one or two responsible maintainers are elected.

The maintainers take responsibility for the roadmap of the repository they maintain (i.e. ansible collection)

On larger repositories it may be useful to delegate responsibility for certain tasks to sub-maintainers, e.g. for single roles in an ansible collection

Each maintainer is responsible for watching, commenting and prioritizing issues, review and accepting or denying pull requests in a timely manner

[press here to view maintainers or apply as maintainer](../01_projects_overview.md)

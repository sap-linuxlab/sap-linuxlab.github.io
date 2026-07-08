![Build Status](https://github.com/sap-linuxlab/sap-linuxlab.github.io/actions/workflows/gh-pages.yml/badge.svg)


# [SAP LinuxLab initiative site](https://sap-linuxlab.github.io)


## This repository

*This static site uses the modified minimal theme from [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)*

This is the source code repository of the SAP LinuxLab initiative website. To propose changes, clone this repository and open a pull request against the `main` branch.

## Deployment

The site is built with [MkDocs](https://www.mkdocs.org/) and published by the [gh-pages](.github/workflows/gh-pages.yml) GitHub Action to GitHub Pages.

| Branch | URL | Purpose |
|--------|-----|---------|
| `main` | https://sap-linuxlab.github.io/ | Production site |
| `dev` | https://sap-linuxlab.github.io/preview/ | Preview for testing changes before merging to `main` |

On every push to `main` or `dev`, the workflow builds both versions and deploys them together: production from `main` and preview from `dev`. Pull requests against `main` run a build check only; they are not deployed.

To test website changes before they go live, work on the `dev` branch and push your commits there. When you are ready, merge `dev` into `main`.

All content that should appear in the left navigation bar must also be added to `mkdocs.yml`.

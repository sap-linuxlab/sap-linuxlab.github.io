[![Build Status](https://travis-ci.org/pages-themes/minimal.svg?branch=gh-pages)](https://travis-ci.org/pages-themes/minimal) [![Gem Version](https://badge.fury.io/rb/jekyll-theme-minimal.svg)](https://badge.fury.io/rb/jekyll-theme-minimal)

*This page uses the modified minimal theme from [armsp](https://github.com/armsp/minimally)*


# SAP Linuxlab Community Project

To visit the page click [here](https://sap-linuxlab.github.io) 

This is the source code repository page of the SAP Linuxlab Community project. If you want to make changes or add content, please clone this repository and create a pull request against the gh-pages branch

To add content create a file namend *`number-anytext.md`* in the root directory of the gh-pages branch. The content of this file should look like

```
---
layout: default
title: *sidebar title*
rank: *number*
---

# Headline

your text in markdown

```

Your content will then be added to the sidebar with the title *sidebar title* and position *rank number*

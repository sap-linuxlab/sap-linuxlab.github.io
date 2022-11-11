# Installing pre-commit

[pre-commit](https://pre-commit.com) is a python program which can be installed with pip

## Minimum requirements

- pyhton 3.7 and higher

## Installation on RHEL8 (defaults to pyhton 3.6)

1. Install Python 3.9   

    ```
    $ sudo dnf install python39-3.9.7
    ```

2. Create a venv and activate it

    ```
    $ /usr/bin/python3.9 -m venv ~/.venv/pre-commit 
    ```
    <BR>
    ```
    $ . ~/.venv/pre-commit/bin/activate
    ```

3. Install pre-commit
    
    ```
    $ pip install --upgrade pip
    ```
    <BR>
    ```
    $ pip install pre-commit
    ```

4. Set an alias or link to `~/.venv/pre-commit/bin/pre-commit` to use it

On other Linux distributions with newer python versions, you can either create a virtual environment or install with `pip install --user pre-commit`

## Using pre-commit

### Configuration files

The config file for pre-commit are created in the root directory of github and is called `.pre-config.yml`. 
In case of ansible collections other config files may apply such as `.ansible-lint` and `.yamllint`. 
The required config files should be created and maintained by the repo maintainers.
Hence they are automatcially downloaded with `git clone` and `git pull` commands

### Activate pre-commit
A repository maintainer activates pre-commit by running `pre-commit install` within a directory of the cloned repository

### Deactivate pre-commit
run `pre-commit uninstall` 

### Useful commands

When you first install pre-commit on a repository and you have created your confg file, you should run:

```
pre-commit run --all-files [--show-diff-on-failure]
```

The optional parameter `--show-diff-on-failure` prints the problematic code at the end of the run.
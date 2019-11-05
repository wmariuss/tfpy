# tfenv (terraformpy)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Check and apply changes (only if changes exists) in all subdir(s) in the current path. This can be used for CI/CD.

This was created to have a workaround for `Gitea`, `Jenkins` and use `Terraform as a Team`. If you want something better I highly recommend to use [Atlantis](https://www.runatlantis.io/) instead.

## Requirements

* `Python >= 3.6`
* `tfenv`

## Install

For production systems we use binary file. Ask or build the binary.

### Build executable

* `pipenv install --dev`
* `pipenv run tox -e package`

## Usage

* `tfpy --help` for active parameters and options

## Tests

Soon.

## Contribute

Contributions are always welcome.

* Fork the repo
* Create a pull request against master
* Be sure tests pass (if exists)

Check [Git Flow](https://guides.github.com/introduction/flow/) for details.

## Authors

* [Marius Stanca](mailto:me@marius.xyz)
# tfpy (terraformpy)

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/wmariuss/tfpy)](https://github.com/wmariuss/tfpy/releases)
[![Tag](https://img.shields.io/github/v/tag/wmariuss/tfpy)](https://github.com/wmariuss/tfpy/tags)
[![License](https://img.shields.io/github/license/wmariuss/tfpy)](https://github.com/wmariuss/tfpy/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Check and apply changes (only if changes exists) in all dir(s) in the current path. This can be used for CI/CD.

This was created to have a workaround for `Gitea`, `Jenkins` and use `Terraform as a Team` model. If you want something better I highly recommend to use [Atlantis](https://www.runatlantis.io/) instead.

## Requirements

* `Python >= 3.6`
* `tfenv`

## Install

For easy deployment this is built as executable. You can download it from [release](https://github.com/wmariuss/tfpy/releases) section.

### Build executable

* `pipenv install --dev`
* `pipenv run tox -e package`

## Usage

* `tfpy --help` for active parameters and options

For Jenkinsfile example, check [here](docs/Jenkinsfile).

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

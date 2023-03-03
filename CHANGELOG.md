<!-- omit in toc -->
# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.5.0] - 2023-03-03

Changed

- App now runs with python 3.10
- Dockerfile now uses python:3.10-alpine rather than python:3.8
- Dockerfile now installs dependencies from requirements.txt rather than pipfile
- Updated CHANGELOG.md to use '-' instead of '*' for bullets

## [2.4.0] - 2022-04-28

Added

* Dockerised the app
* Command line arguments for start/end values and divisors

Changed

* Updated README.md with new examples for arguments & docker
* Changed version links in this file to point to tags

Fixed

* Version typo in this file

## [2.3.0] - 2022-01-13

Changed

* config.py format - now a single dict containing all config items
* Now using ```config['item']``` syntax to bring in variables

## [2.2.0] - 2022-01-13

Added

* Backticks to code blocks in this file

Fixed

* Fixed "dangerous default parameter" warning in ```play_fizzbuzz()```. Default is now "None" and is set inside the function

## [2.1.0] - 2022-01-13

Added

* ```__main__.py``` file so the package can be run directly

Changed

* Updated all test references to use the new 'play_fizzbuzz()' function
* Updated README.md with new 'play_fizzbuzz()' function name

Fixed

* config import in fizzbuyzz.py file

## [2.0.0] - 2021-06-15

Changed

* Removed ```playFizzBuzz()``` function

---

## [1.1.0] - 2021-06-15

Added

* New ```play_fizzbuzz()``` function

Changed

* Deprecated ```playFizzBuzz()``` function [will be removed from v2.0.0]

---

## [1.0.1] - 2021-06-14

Added

* pytest tests for FizzBuzz
* Sanity checking in FizzBuzz module

---

## [1.0.0] - 2021-06-11

Added

* FizzBuzz game working

---

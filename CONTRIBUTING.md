# Contributing
Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible.

Note that code must remain valid and Vermin be able to run via Python v3+ but still include
detection of v2.x functionality.

## Dependencies
Install development and analysis dependencies via `make setup`. It will setup a `virtualenv` in
`.venv` and install necessary dependencies.

Dependencies can also be directly installed via:
```shell
% python3 -m pip install --upgrade pip virtualenv
% virtualenv -p python3 .venv
% source .venv/bin/activate                          # or whatever suits the platform.
% pip install -r misc/.analysis-requirements.txt
```

**Note:** Until the release of Vermin 1.6, it is recommended to use Python 3.10 or lower when
running analysis checks. This is because Pylint requires an update but doing so makes it
incompatible with certain versions of Python 2.x. In Vermin 1.6, support for Python 2.7 will be
removed and dependencies will be updated such that Python 3.11 can be used for analysis checks.

Unittests can be run without installing any dependencies: `make test`

## Detection Rules
Rules for detecting minimum versions are defined in "vermin/rules.py".

## Backports
Some features are sometimes backported into packages, in repositories such as
[PyPi](https://pypi.org), that are widely used but aren't in the standard language.

Backports are defined in "vermin/backports.py" with associated rules in "vermin/rules.py".

Adding versioned backports is only applicable when the minimum versions of the most current,
published version change. Unversioned backports must be the newest among versioned and unversioned,
and must be sorted after the versioned counterparts in the tuples of `BACKPORTS`. The version part
can be any string.

## Pull Requests
Make sure to keep the code vanilla Python and run `make test check-all` first to improve turnaround
time.

It is required to add new unittests to cover related changes if appropriate.

Unittests are defined in test suites located in the "tests/" folder.

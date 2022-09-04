# Contributing
Contributions are very welcome, especially adding and updating detection rules of modules,
functions, classes etc. to cover as many Python versions as possible.

Note that code must remain valid and working on Python v2.7+ and v3+.

## Dependencies
Install development and analysis dependencies via `make setup`. It will setup a `virtualenv` in
`.venv` and install necessary depencencies.

Dependencies can also be directly installed via:
```shell
% python3 -m pip install --upgrade pip virtualenv
% virtualenv -p python3 .venv
% source .venv/bin/activate                          # or whatever suits the platform.
% pip install -r misc/.analysis-requirements.txt
```

Unittests can be run without installing any dependencies: `make test`

## Pull Requests
Make sure to keep the code vanilla Python and run `make test check-all` first to improve turnaround
time.

It is required to add new unittests to cover related changes if appropriate.

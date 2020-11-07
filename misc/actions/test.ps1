$PYTHON_VERSION = python -c "import sys;v=sys.version_info;print('{}.{}'.format(v[0],v[1]))"

if ( $PYTHON_VERSION -eq "2.7" -or $PYTHON_VERSION -eq "3.4" -or $PYTHON_VERSION -eq "3.5" ) {
  make test
  exit 0
}

# Set policy that allows the execution of scripts and tests.
Set-ExecutionPolicy Unrestricted -Force

# Setup virtual env.
make setup-venv
. .venv\Scripts\activate.ps1

# Install deps.
pip install -r misc\.coverage-requirements.txt

# Run tests and record coverage.
coverage run --source=vermin,tests runtests.py
if (!$?) {
  $Host.SetShouldExit(1) # This is necessary in order to fail the GitHub job.
  exit 1
}

# Report coverage.
$env:COVERALLS_REPO_TOKEN = "twBSHlgE5AMFEQNmUK04LDcN7SVth3lDV"
coveralls

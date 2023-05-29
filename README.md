# Template

Empty template repository to kickstart coding.

## Initialisation

Before starting to code, please change the following files:
 - Rename `src/my_package` to the correct package name (snake-case)
 - Add package description in `src/your_package/__init__.py`
 - Update package name and description in `setup.py`

Afterwards, run `./init.sh` to install the environment. Note:
 - If `zsh` is being difficult, run `chmod +x ./init.sh` first
 - Your system's default Python version is used (advise to have this set to `3.10`)
 - The virtual environment is called `.env`


## Usage

Use the `invoke` commands to:
 - Lint your repository under `src/your_package` using `invoke lint`
 - Test your packages via unit-tests in `tests/unit/` using `invoke test`
 - Start a Jupyter notebook environment using `invoke lab`

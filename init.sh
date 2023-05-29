#!/usr/bin/env bash
set -e

# Please do not edit this file!

function log {
    local PURPLE='\033[0;35m'
    local NOCOLOR='\033[m'
    local BOLD='\033[1m'
    local NOBOLD='\033[0m'
    echo -e -n "${PURPLE}${BOLD}$1${NOBOLD}${NOCOLOR}" >&2
}

function create_venv {
    log "Creating virtual environment... \\n"
    python -m venv .env
    log " --> Done! \\n\\n"
}

function install_dependencies {
    log "Installing dependencies... \\n"
    # shellcheck disable=SC1091
    source .env/bin/activate
    pip install --upgrade pip
    pip install -e ".[dev]"
    log " --> Done! \\n\\n"
}

# Initialise the environment
create_venv
install_dependencies
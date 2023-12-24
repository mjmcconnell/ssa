#!/bin/bash
# --------------------------------------------------------
# This file defines the script for starting the server.
# --------------------------------------------------------

set -euo pipefail
IFS=$'\n\t'

start_server () {
    echo "Starting server"

    python ./src/run.py run-app
}

start_server

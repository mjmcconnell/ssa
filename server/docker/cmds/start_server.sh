#!/bin/bash
# --------------------------------------------------------
# This file defines the script for starting the server.
# --------------------------------------------------------

set -euo pipefail
IFS=$'\n\t'

start_server () {
    echo "Starting server"

    python -m core.main
}

start_server

#!/bin/bash
# --------------------------------------------------------
# This file defines scripts, to be run as one off jobs.
#
# Typically this is for setting up database schemas, and loading initial data
# --------------------------------------------------------

set -euo pipefail
IFS=$'\n\t'

# alembic_upgrade applied the alembic migrations defined in /migrations/alembic
alembic_upgrade () {
    echo "Running migrations"

    cd /opt/app-root/migrations
    alembic upgrade head
    cd /opt/app-root
}

# sync_elasticsearch
run_seeding () {
    echo "Seeding database"
    python /opt/app-root/cli/run_seed.py
}

run_jobs () {
    alembic_upgrade
    run_seeding
}

run_jobs

#!/usr/bin/env bash
#
# deploy-docs.sh — trigger a docs deploy on the server.
#
# Deploys are now built on the server. This just runs /opt/wirge/deploy.sh over
# SSH, which pulls the latest commit and rebuilds the live site. Push your
# changes to the repo first so the server has something to pull.
#
# Usage:
#   deploy/deploy-docs.sh
#
set -euo pipefail

exec ssh epimethean.dev /opt/wirge/deploy.sh

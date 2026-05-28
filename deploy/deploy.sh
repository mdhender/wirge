#!/usr/bin/env bash
#
# deploy.sh — update the docs checkout and rebuild the live site, on the server.
#
# Installed at /opt/wirge/deploy.sh. Pulls the latest commit into the wirge
# checkout and rebuilds Hugo's public/ directory, which the web server serves
# directly (see deploy/nginx.conf or deploy/Caddyfile).
#
# The rebuild happens in place on the live public/ directory, so a browser
# loading a page mid-build may briefly hit a missing or half-written asset.
# This is accepted as low risk (low probability, low impact).
#
# One-time server setup is documented in deploy/README.md.
#
# Usage (on the server):
#   /opt/wirge/deploy.sh
#
set -euo pipefail

# deploy-docs.sh invokes this over SSH, and a non-interactive SSH shell has a
# minimal PATH that omits /usr/local/bin, the Go toolchain, and /snap/bin. Add
# the common locations so git/hugo/go resolve however they were installed.
export PATH="/usr/local/bin:/usr/local/go/bin:/snap/bin:$PATH"

# Where the wirge repo is checked out on this server. The web server's docs root
# points at "$REPO_DIR/public".
REPO_DIR="/opt/wirge/wirge"

cd "$REPO_DIR"

echo ">> Updating checkout in $REPO_DIR"
git pull --ff-only

echo ">> Rebuilding public/"
hugo --gc --minify

echo ">> Done"

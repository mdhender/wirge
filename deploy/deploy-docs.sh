#!/usr/bin/env bash
#
# deploy-docs.sh — rebuild the Hugo site and deploy it to epimethean.dev.
#
# Rebuilds the static site into public/ and rsyncs its contents to the web
# server's docs root. See deploy/nginx.conf for how the server maps /docs/ to
# /var/www/epimethean/docs/.
#
# Usage:
#   deploy/deploy-docs.sh              # build, then sync to the server
#   deploy/deploy-docs.sh --dry-run    # build, then show what would sync (no changes)
#
set -euo pipefail

REMOTE="epimethean.dev:/var/www/epimethean/docs/"

# Run from the repo root regardless of where the script is invoked.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# rsync options: archive, compress, verbose. --checksum compares file contents
# rather than size+mtime, so Hugo rewriting every file each build (which bumps
# mtimes) does not force needless transfers. --delete-after removes files on the
# server that no longer exist locally, but only after the new files land (avoids
# a window where a referenced asset is briefly missing). --dry-run pairs with
# plain --delete so the preview lists deletions up front.
RSYNC_OPTS=(-avz --checksum --delete-after)
if [[ "${1:-}" == "--dry-run" ]]; then
  RSYNC_OPTS=(-avz --checksum --delete --dry-run)
  echo ">> DRY RUN — no changes will be made to the server"
fi

echo ">> Building site into public/"
hugo --gc --minify

echo ">> Syncing public/ -> $REMOTE"
rsync "${RSYNC_OPTS[@]}" public/ "$REMOTE"

echo ">> Done"

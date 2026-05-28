# Deploying the docs

The Epimethean Challenge docs are a static Hugo build. They are built **on the
server** from a git checkout, and the web server serves that build directly.

## Deploying

1. Push your changes to `main` — the server pulls from there.
2. Trigger the build, either:
   - from your laptop: `deploy/deploy-docs.sh` (runs the server script over SSH), or
   - on the server: `/opt/wirge/deploy.sh`.

`/opt/wirge/deploy.sh` `cd`s into the checkout, runs `git pull`, and rebuilds
`public/` with Hugo. The rebuild happens in place on the live directory, so a
browser loading a page mid-build may briefly hit a missing asset — accepted as
low risk (low probability, low impact).

## One-time server setup

Assumes `git` and `hugo` (Extended) are installed.

1. Clone the repo into place:

       sudo git clone https://github.com/mdhender/wirge.git /opt/wirge/wirge

2. Install the deploy script:

       sudo cp /opt/wirge/wirge/deploy/deploy.sh /opt/wirge/deploy.sh
       sudo chmod +x /opt/wirge/deploy.sh

3. Point the web server's docs root at the build output. The `nginx.conf` and
   `Caddyfile` templates keep their existing roots, so symlink that root at the
   checkout's `public/` directory:

       # nginx (see deploy/nginx.conf)
       sudo ln -s /opt/wirge/wirge/public /var/www/epimethean/docs

       # Caddy (see deploy/Caddyfile)
       sudo ln -s /opt/wirge/wirge/public /srv/epimethean/docs

4. Run the first deploy to produce `public/`:

       /opt/wirge/deploy.sh

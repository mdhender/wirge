# Deploying the docs

The Epimethean Challenge docs are a static Hugo build. They are built **on the
server** from a git checkout, and the web server serves that build directly.

## Everyday workflow

1. Commit and **push to `main`**. The server publishes the commit it pulls, not
   your working tree — so unpushed work won't go live, and a deploy that isn't
   preceded by a push republishes stale content.
2. Trigger the build, either:
   - from your laptop: `deploy/deploy-docs.sh` (SSHes in and runs the server
     script), or
   - on the server: `/opt/wirge/deploy.sh`.

`/opt/wirge/deploy.sh` `cd`s into the checkout, runs `git pull --ff-only`, and
rebuilds `public/` with `hugo --gc --minify`. The rebuild happens in place on the
live directory, so a browser loading a page mid-build may briefly hit a missing
asset — accepted as low risk (low probability, low impact).

## Server setup (one time)

The live server is `ec.pbbgaming.com`. Run these as the **deploy user** — the
non-root account that owns the checkout and that `ssh ec.pbbgaming.com` logs in as
(here, `wirge`) — using `sudo` only on the privileged steps. Don't deploy as
root: it taints `public/` and `.git` ownership and breaks the next deploy.

### 1. Toolchain — official binaries, not snaps

Install **Hugo Extended** and **Go** as official binaries (Hugo shells out to Go
to fetch the Hextra theme module). Do **not** use the snap packages: snaps are
strictly confined and can't read a project under `/opt` (the build dies with
`failed to apply mounts for project … /var/lib/snapd/void: permission denied`),
they auto-update on their own schedule, and `/snap/bin` isn't on a
non-interactive SSH PATH.

    # Hugo Extended (pin the version you want)
    cd /tmp
    curl -LO https://github.com/gohugoio/hugo/releases/download/v0.162.0/hugo_extended_0.162.0_linux-amd64.tar.gz
    tar xzf hugo_extended_0.162.0_linux-amd64.tar.gz hugo
    sudo install -m 0755 hugo /usr/local/bin/hugo

    # Go (latest stable)
    cd /tmp
    GOVER=$(curl -s 'https://go.dev/VERSION?m=text' | head -1)
    curl -LO "https://go.dev/dl/${GOVER}.linux-amd64.tar.gz"
    sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf "${GOVER}.linux-amd64.tar.gz"

`deploy.sh` prepends `/usr/local/bin:/usr/local/go/bin:/snap/bin` to `PATH`, so
the unattended SSH deploy finds these regardless of the login shell's PATH.

### 2. Clone the repo and install the script

    sudo mkdir -p /opt/wirge && sudo chown "$USER" /opt/wirge
    git clone https://github.com/mdhender/wirge.git /opt/wirge/wirge
    cp /opt/wirge/wirge/deploy/deploy.sh /opt/wirge/deploy.sh
    chmod +x /opt/wirge/deploy.sh

The checkout must stay owned by the deploy user. (If a build ever runs as root by
accident, fix it with `sudo chown -R wirge:wirge /opt/wirge/wirge`.) `deploy.sh`
is a *copy*, not a symlink — re-run the `cp` above whenever `deploy/deploy.sh`
changes in the repo.

### 3. Produce the first build

    /opt/wirge/deploy.sh

### 4. Point the web root at the build output

The `nginx.conf` / `Caddyfile` templates keep their existing roots, so symlink
that root at the checkout's `public/`. The old rsync deploy may have left a real
directory there — move it aside first.

    # nginx (deploy/nginx.conf): root /var/www/wirge, /docs/ -> /var/www/wirge/docs
    sudo mv /var/www/wirge/docs /var/www/wirge/docs.old   # if it exists as a dir
    sudo ln -s /opt/wirge/wirge/public /var/www/wirge/docs

    # Caddy (deploy/Caddyfile)
    sudo ln -s /opt/wirge/wirge/public /srv/wirge/docs

Make sure the web server's user can traverse into the checkout:

    chmod o+rx /opt/wirge /opt/wirge/wirge /opt/wirge/wirge/public

### 5. Verify

    curl -sI https://ec.pbbgaming.com/docs/ | head -1   # expect: HTTP/... 200

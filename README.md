# SE

Self-education project

## Requirements

### Run project locally

- Docker Engine ≥ 24.0
- Docker Compose ≥ 2.20
- Linux (x86_64/arm64)
- GNU Make ≥ 4.3

### Development (additional)

- Python ≥ 3.13
- Poetry ≥ 2.0
- just ≥ 1.0
- **Git Bash ≥ 2.40** (Windows only)

## Structure

```bash
compose/    # Docker compose files
docker/     # Dockerfiles
docs/       # Project documentation
src/        # Code source
  se/
    domain/         # Project domain layer
    entrypoints/    # Project entrypoint layer
      web/            # WEB Backend for frontend
        handlers/       # Request handlers (BFF component)
    infrastructure/ # Project infrastructure layer
      db/             # Database infrastructure
      http/           # HTTP clients
      api_clients/    # Services API clients
tests/      # Tests
  web/        # WEB BFF tests
    e2e/        # Playwright (browser, DOM) tests
    unit/       # Unit tests
tools/
  just/     # Just recipes
  make/     # Makefile commands
```

## Workflow

### Development mode

#### Add environments and secrets examples

See: `.envs.example`

```bash
make environments   # Add environments example
make secrets        # Add secrets example
```

#### Add networks

```bash
make net-create     # Create networks
```

#### Database administration

```bash
make admin-up       # Start service on http://127.0.0.1:$(ADMIN_HOST_PORT)
make admin-migrate  # Apply migrations
make admin-su       # Create superuser
```

For example DB administration URL: http://127.0.0.1:8100/admin/

#### Start services

```bash
make web-up         # Start web entrypoint on http://127.0.0.1:$(WEB_HOST_PORT)
```
For example WEB URL: http://127.0.0.1:8200/ru/glossary/

##### Localize

```bash
make web-compilemessages    # Compile .po files to .mo
make web-restart            # Restart web process
```

#### Add dependencies for development

```bash
make setup          # Install project with development dependencies
```

#### Run e2e tests

```bash
make web-e2e        # Run Playwright E2E against web (web must be running)
```

#### Project documentation

```bash
make docs-build     # Build documentation image
make docs-run       # Run documentation server on http://127.0.0.1:$(DOCS_HOST_PORT)
```

For example documentation URL: http://127.0.0.1:8300

## Show available commands

```bash
make help           # Show Makefile command help
just help           # Show all just recipes
```
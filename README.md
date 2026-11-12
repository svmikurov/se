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

## Workflow

### Development mode

#### Add environments and secrets examples

See: `.envs.example`

```bash
make environments   # Add environments example
make secrets        # Add secrets example
```

#### Database administration

```bash
make admin-up       # Start container for below
make admin-migrate  # Apply migrations
make admin-su       # Create superuser
```

Service URL: http://127.0.0.1:8100/admin/

#### Add dependencies for development

```bash
make setup          # Install project with development dependencies
```

#### Project documentation

```bash
docs-docker-build:  # Build documentation image
docs-docker-run:    # Run documentation server on http://localhost:$(DOCS_HOST_PORT)
```

`DOCS_HOST_PORT` is defined in `.envs/docs` file

## Show available commands

```bash
make help           # Show Makefile command help
just help           # Show all just recipes

just ld {file_name} # Load file_name.json data to database
```
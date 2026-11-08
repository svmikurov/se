# SE

Self-education project

## Requirements

### Run project locally

- Docker
- GNU Make

### Development (additional)

- Python 3.13+
- Poetry 2.x
- just

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

## Show available commands

```bash
make help
```
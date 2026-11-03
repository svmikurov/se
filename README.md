# SE

Project for self education

## Requirements

- Python 3.13+
- PostgreSQL 14+
- Poetry 2.x
- GNU Make, just

## Workflow

```bash
make environments   # Add environments example
make secrets        # Add secrets example
make admin-up       # Start container for bellow
make admin-migrate  # Apply migrations
make admin-su       # Create super user
```

Service url: http://127.0.0.1:8100/admin/

## Development

```bash
make setup          # Install project with development dependencies
```

## Show available commands

```bash
make help
```
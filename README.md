# Containerized Dagster dbt Snowflake Pipeline

This project demonstrates a data pipeline using Dagster, dbt, and Snowflake, all containerized with Docker.

## Project Structure

```
.
├── dbt_project/           # dbt project directory
│   ├── models/           # dbt models
│   ├── macros/          # dbt macros
│   └── dbt_project.yml  # dbt project configuration
├── dagster/             # Dagster project files
│   └── dagster_home/    # Dagster home directory
├── docker/              # Docker configuration files
│   ├── Dockerfile.dagster
│   └── Dockerfile.dbt
├── docker-compose.yml   # Docker Compose configuration
└── requirements.txt     # Python dependencies
```

## Prerequisites

- Docker and Docker Compose
- Snowflake account with appropriate permissions
- Git

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd containerized_dagster_dbt_snowflake_pipeline
   ```

2. Configure Snowflake credentials:
   - Create a `profiles.yml` file in the `dbt_project` directory with your Snowflake credentials
   - Ensure the credentials match the configuration in `docker-compose.yml`

3. Start the containers:
   ```bash
   docker-compose up -d
   ```

4. Access Dagster UI:
   - Open `http://localhost:3000` in your browser
   - The Dagster UI will be available with your pipeline

## Development

### Adding New dbt Models

1. Create new model files in `dbt_project/models/`
2. Update `dbt_project/dbt_project.yml` to include new models
3. Test locally using dbt commands:
   ```bash
   docker-compose exec dbt dbt run
   ```

### Modifying Dagster Jobs

1. Edit the Dagster job definitions in the `dagster` directory
2. Restart the Dagster container to apply changes:
   ```bash
   docker-compose restart dagster
   ```

## Troubleshooting

- Check container logs:
  ```bash
  docker-compose logs -f
  ```
- Verify Snowflake connection:
  ```bash
  docker-compose exec dbt dbt debug
  ```
- Check dbt model status:
  ```bash
  docker-compose exec dbt dbt ls
  ```


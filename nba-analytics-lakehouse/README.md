# NBA Analytics Lakehouse

Projeto de Engenharia de Dados focado em analytics da NBA utilizando arquitetura moderna de Data Lake e Data Warehouse.

## Tecnologias

- Python
- PostgreSQL
- Docker
- Airflow
- AWS S3
- Power BI
- GitHub Actions

## Arquitetura

```text
NBA API
   ↓
Bronze Layer
   ↓
Silver Layer
   ↓
Gold Layer
   ↓
PostgreSQL
   ↓
Power BI
```

## Estrutura do Projeto

```text
nba-analytics-lakehouse/

├── airflow
├── dashboards
├── data
├── docker
├── docs
├── notebooks
├── src
└── tests
```

## Roadmap

- [ ] Setup do ambiente
- [ ] Ingestão NBA API
- [ ] Camada Bronze
- [ ] Camada Silver
- [ ] Camada Gold
- [ ] PostgreSQL
- [ ] Airflow
- [ ] AWS S3
- [ ] Dashboard Power BI
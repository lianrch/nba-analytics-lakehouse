# NBA Analytics Lakehouse

Projeto de Engenharia de Dados focado em analytics da NBA.

## Stack

- Python
- PostgreSQL
- Docker
- SQLAlchemy
- NBA API
- Git/GitHub

## Arquitetura

NBA API
↓
Raw Layer (CSV)
↓
Bronze Layer (PostgreSQL)
↓
Silver Layer (em construção)
↓
Gold Layer (em construção)

## Status

- [x] Infraestrutura Docker
- [x] PostgreSQL
- [x] Conexão SQLAlchemy
- [x] Ingestão de Times NBA
- [ ] Ingestão de Jogos
- [ ] Ingestão de Jogadores
- [ ] Airflow
- [ ] AWS S3
- [ ] Dashboard
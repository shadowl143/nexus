# Nexus Platform

Plataforma modular que se compone de tres, caras distinatas, dentro del repo se pude encontrar una opcion
para usar _tkinter_, _¨PyQt_ y _fast api_, para poder darle continuidad y segumiento al proyecto para fines educativos.

## Porque importa?

Nexus unifica lógica de negocio, API y cliente de escritorio en una arquitectura limpia y desacoplada. Permite escalar desde desarrollo local hasta despliegue productivo manteniendo pruebas automatizadas, separación de responsabilidades y consistencia visual (light/dark mode).

## Arquitectura

                 ┌────────────────────┐
                 │    Nexus Desktop   │
                 │  (PyQt6 UI Layer)  │
                 └─────────┬──────────┘
                           │ HTTP / DTOs
                 ┌─────────▼──────────┐
                 │      Nexus API     │
                 │   (FastAPI Layer)  │
                 └─────────┬──────────┘
                           │ Services
                 ┌─────────▼──────────┐
                 │     Nexus Core     │
                 │ (Business Logic)   │
                 └─────────┬──────────┘
                           │
                 ┌─────────▼──────────┐
                 │    Persistence     │
                 │ (DB / Repositories)│
                 └────────────────────┘

## Quickstart

./scripts/setup.sh && python -m python -m nexus_desktop.PyQt.app

## Deploys públicos

Github: https://github.com/shadowl143/nexus
youtube: <<por definir>>

## Tecnologías

| Capa      | Tecnología          |
| --------- | ------------------- |
| Core      | Python 3.12         |
| API       | FastAPI             |
| Desktop   | PyQt6               |
| Desktop   | Tkinter             |
| Testing   | Pytest / Unittest   |
| DB        | PostgreSQL / SQLite |
| Packaging | Docker              |
| CI/CD     | GitHub Actions      |

## Capturas

### modo claro

![alt text](<docs/files/Captura de pantalla 2026-07-12 173541.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 173633.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 173712.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 174402.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 174442.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 174456.png>)

### modo oscuro

![alt text](<docs/files/Captura de pantalla 2026-07-12 174621.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 174649.png>)
![alt text](<docs/files/Captura de pantalla 2026-07-12 174724.png>)

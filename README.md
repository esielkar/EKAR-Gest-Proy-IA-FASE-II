# Proyecto Fase II: Arquitectura de Inferencia Local Contenerizada

Sistema de IA desplegado en infraestructura propia (Synology NAS DS1525+) utilizando Docker, Ollama y Open WebUI.

## Requisitos
- Docker y Docker Compose instalados en el Synology NAS.
- Almacenamiento persistente configurado.

## Ejecución
Para levantar la pila completa de servicios, ejecuta en la terminal de tu NAS o utiliza Container Manager para cada:
```bash
docker compose up -d --build
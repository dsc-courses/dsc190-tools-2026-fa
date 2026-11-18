---
title: Heart Disease API
sdk: docker
app_port: 8000
---

A FastAPI app that serves the heart disease decision tree from Demo 02.

The settings above are for Hugging Face Spaces. `app_port: 8000` tells the
Space which port the app listens on; without it, the Space expects port 7860
and never finds the app.

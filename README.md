# Result-Check Website

A Flask-based web application to look up student exam results.

## Features
- Web UI to search results by roll number
- REST API endpoint (`/api/result/<roll_number>`)
- Health check endpoint (`/health`)
- CI/CD pipeline with GitHub Actions
- Docker containerization

## Usage
```bash
pip install -r requirements.txt
python app.py
```
Visit `http://localhost:5000`

## API
```bash
curl http://localhost:5000/api/result/21CS001
curl http://localhost:5000/health
```


<!-- CI/CD Pipeline verified -->

<!-- Warm cache test run -->

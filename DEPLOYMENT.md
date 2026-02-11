# Deployment Guide - Traffic Volume Prediction Dashboard

## 📋 Table of Contents
1. [Local Deployment](#local-deployment)
2. [Streamlit Cloud](#streamlit-cloud)
3. [Docker Deployment](#docker-deployment)
4. [Server Deployment (AWS/Azure/Heroku)](#server-deployment)
5. [Production Checklist](#production-checklist)

---

## Local Deployment

### Quick Start (5 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate test data (optional)
python prepare_test_data.py

# 3. Run dashboard
streamlit run app.py
```

**Access:** `http://localhost:8501`

### Advanced Options

```bash
# Run on specific port
streamlit run app.py --server.port 8502

# Enable debug logging
streamlit run app.py --logger.level=debug

# Disable file watcher
streamlit run app.py --server.runOnSave=false

# Headless mode (no browser auto-open)
streamlit run app.py --server.headless=true
```

---

## Streamlit Cloud (Free & Easy)

### Setup (Recommended for Personal Projects)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Add traffic dashboard"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your GitHub repository
   - Set main file to `app.py`
   - Click "Deploy"

3. **Public URL:** `https://yourname-traffic-dashboard.streamlit.app`

### Configure Secrets

Create `.streamlit/secrets.toml`:
```toml
[database]
host = "your-db-host"
user = "your-db-user"
password = "your-password"

[models]
model_path = "/path/to/models"
```

### Environment Variables

```bash
# .streamlit/config.toml
[client]
showErrorDetails = false
maxMessageSize = 200

[logger]
level = "warning"

[server]
headless = true
port = 8501
runOnSave = false
```

---

## Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create .streamlit config
RUN mkdir -p ~/.streamlit && \
    echo "[server]" > ~/.streamlit/config.toml && \
    echo "port = 8501" >> ~/.streamlit/config.toml && \
    echo "headless = true" >> ~/.streamlit/config.toml

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
CMD ["streamlit", "run", "app.py"]
```

### Create .dockerignore

```
__pycache__
*.pyc
*.pyo
.git
.gitignore
.streamlit/secrets.toml
venv/
.env
.Python
```

### Build & Run

```bash
# Build image
docker build -t traffic-dashboard:latest .

# Run container
docker run -p 8501:8501 traffic-dashboard:latest

# Run with volume mount
docker run -p 8501:8501 -v $(pwd)/data:/app/data traffic-dashboard:latest

# Run with environment variables
docker run -p 8501:8501 -e LOG_LEVEL=debug traffic-dashboard:latest
```

### Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  dashboard:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_LOGGER_LEVEL=info
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
```

---

## Server Deployment

### AWS (Elastic Container Service - ECS)

1. **Create ECR Repository:**
   ```bash
   aws ecr create-repository --repository-name traffic-dashboard
   ```

2. **Build & Push Image:**
   ```bash
   docker build -t traffic-dashboard .
   docker tag traffic-dashboard:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/traffic-dashboard:latest
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/traffic-dashboard:latest
   ```

3. **Create ECS Service:**
   - Navigate to ECS Console
   - Create cluster
   - Create task definition pointing to your image
   - Create service with load balancer

### Heroku (Deprecated but Alternatives)

For Railway.app or Fly.io:
```bash
# Deploy with Railway
railway init
railway up

# Deploy with Fly.io
flyctl launch
flyctl deploy
```

### Azure (App Service)

1. **Create Resource Group:**
   ```bash
   az group create --name myResourceGroup --location eastus
   ```

2. **Deploy Container:**
   ```bash
   az container create \
     --resource-group myResourceGroup \
     --name traffic-dashboard \
     --image <image-name> \
     --ports 8501 \
     --environment-variables PORT=8501
   ```

### Google Cloud (Cloud Run)

```bash
# Deploy
gcloud run deploy traffic-dashboard \
  --source . \
  --platform managed \
  --allow-unauthenticated

# Set environment
gcloud run services update traffic-dashboard \
  --set-env-vars STREAMLIT_SERVER_HEADLESS=true
```

---

## Production Checklist

### Security
- [ ] Remove debug mode from production
- [ ] Use HTTPS/TLS certificates
- [ ] Implement authentication (if needed)
- [ ] Validate all user inputs
- [ ] Hide error details from users
- [ ] Use environment variables for secrets
- [ ] Regular security updates
- [ ] Monitor for suspicious activity

### Performance
- [ ] Enable caching (models, data)
- [ ] Use CDN for static files
- [ ] Implement request throttling
- [ ] Monitor memory usage
- [ ] Optimize database queries
- [ ] Use connection pooling
- [ ] Add load balancing

### Monitoring & Logging
- [ ] Set up application monitoring
- [ ] Configure error tracking
- [ ] Implement usage logging
- [ ] Monitor model performance
- [ ] Alert on errors/anomalies
- [ ] Track resource utilization
- [ ] Log user actions (compliance)

### Data Management
- [ ] Backup data regularly
- [ ] Implement data retention policies
- [ ] Secure data transmission
- [ ] Implement audit trails
- [ ] GDPR/privacy compliance
- [ ] Data validation on input
- [ ] Regular data quality checks

### Deployment
- [ ] Use CI/CD pipeline
- [ ] Automated testing
- [ ] Staging environment
- [ ] Rollback capability
- [ ] Blue-green deployment
- [ ] Version control
- [ ] Documentation

### Maintenance
- [ ] Update dependencies monthly
- [ ] Monitor model accuracy
- [ ] Plan model retraining
- [ ] Document all changes
- [ ] Team access controls
- [ ] Incident response plan
- [ ] Disaster recovery plan

---

## Configuration by Deployment Type

### Local Development
```toml
[client]
showErrorDetails = true

[logger]
level = "debug"
```

### Staging
```toml
[client]
showErrorDetails = true

[logger]
level = "info"
```

### Production
```toml
[client]
showErrorDetails = false

[logger]
level = "warning"

[server]
headless = true
port = 8501
enableCORS = false
```

---

## Troubleshooting Deployment

### Port Already in Use
```bash
# Find process using port 8501
lsof -ti:8501

# Kill process
kill -9 <PID>

# Or use different port
streamlit run app.py --server.port 8502
```

### Out of Memory
```bash
# Increase Docker memory
docker run -m 2g traffic-dashboard:latest

# Or optimize in code
# Reduce sample size in prepare_test_data.py
```

### Models Not Found
```bash
# Ensure models are copied in Dockerfile
COPY *.pkl ./

# Or mount as volume
docker run -v $(pwd):/app traffic-dashboard:latest
```

### CORS Issues
```toml
# .streamlit/config.toml
[server]
enableCORS = false
enableXsrfProtection = true
```

---

## Performance Optimization Tips

1. **Cache aggressively:**
   ```python
   @st.cache_resource
   def load_model(name):
       return joblib.load(f"{name}.pkl")
   ```

2. **Lazy load data:**
   ```python
   @st.cache_data
   def get_test_data():
       return pd.read_csv('test_data.csv')
   ```

3. **Reduce plot complexity:**
   ```python
   # Limit data points in visualization
   sample_data = large_data.sample(1000)
   ```

4. **Use efficient data types:**
   ```python
   df['col'] = df['col'].astype('int32')  # Instead of int64
   ```

---

## Monitoring Dashboard Health

### Add Health Check Endpoint

```python
# In app.py or separate healthcheck.py
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "models_loaded": True
    }
```

### Monitor Key Metrics

- API response time
- Model prediction time
- Cache hit rate
- Error rate
- User count
- Memory usage
- CPU usage

---

## Rollback & Recovery

### Deployment History
```bash
# Git history
git log --oneline

# Revert to previous version
git revert HEAD
git push origin main

# Docker tag versions
docker tag traffic-dashboard:latest traffic-dashboard:v1.0
docker tag traffic-dashboard:latest traffic-dashboard:v1.1
```

### Zero-Downtime Deployment
1. Deploy to staging first
2. Run tests
3. Switch traffic gradually
4. Monitor metrics
5. Keep previous version available

---

## Support & Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Docker Docs:** https://docs.docker.com
- **Cloud Platforms:** AWS, Azure, GCP documentation
- **Community:** Streamlit Discord, Stack Overflow

---

**Happy Deploying! 🚀**

#first
after clone this project 

# how to use django prometheus 
first install django-prometheus package 

```bash 
python pip install django-prometheus
```

## check metrics 
```bash
python manage.py runserver
# in your browser
localhost:8000/metrics
```
##  go to prometheus folder in terminal
```bash
./prometheus --config.file=prometheus.yml
```
## in browser you browser you can check
```bash
http://127.0.0.1:9090/
```

## you can add new job in prometheus.yml 
```yaml
global:
  scrape_interval: 15s 
  evaluation_interval: 15s 


alerting:
  alertmanagers:
    - static_configs:
        - targets:

rule_files:

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: django-myapi
    metrics_path: /metrics
    scrape_interval: 10s
    static_configs:
      - targets:
        - localhost:8000
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
```
##dowload latest prometheus 
[prometheus](https://prometheus.io/download/)

## grafana 
you cann add your prometheus datasource in grafana for dashboard monitoring 




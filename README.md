# first
do this after clone this project 

# how to use django prometheus in this project 
first install django-prometheus package 

```bash 
python pip install django-prometheus
```

# check metrics 
```bash
python manage.py runserver
# in your browser
localhost:8000/metrics
```
# dowload latest version prometheus 
[prometheus](https://prometheus.io/download/)

# go to prometheus folder in terminal
```bash
./prometheus --config.file=prometheus.yml
```
## in browser you can check
```bash
http://127.0.0.1:9090/
```

# for node_exporter
for latest version [node_exporter](https://prometheus.io/download/#node_exporter)

## start node_exporter
#### go to node_exporter folder
#### yes you can make systemd service for execution 
```bash
./node_exporter
```

# add new job in prometheus.yml 
```yaml
global:
  scrape_interval: 15s 
  evaluation_interval: 15s 

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


# grafana 
#### you can add your prometheus datasource in grafana for dashboard monitoring 
you can see how to install grafana from here [grafana](https://grafana.com/docs/grafana/latest/installation/)

## prometheus visualization in grafana 
for how to add datasource in [grafana](https://prometheus.io/docs/visualization/grafana/)

# django-prometheus 
for more information checkout this [django-prometheus](https://github.com/korfuri/django-prometheus)





# API sentimiento v1

# Modelos

## crear los modelos con train.py

```shell
python train.py
```


# Fast API

## levantar los servicios con docker

```shell
docker compose up
```



## Probamos con postman

POST:  http://0.0.0.0:8008/sentimiento/

BODY JSON:  {"data": "Amigo @metrodemedellin una pregunta, para ir a arreglar un inconveniente con mi cívica en qué estación es y puedo ir mañana domingo???"}


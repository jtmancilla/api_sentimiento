# API sentimiento v1


# Fast API

## Running with docker

```shell
docker compose up
```



## Running with python virtualenv

1. Create virtualenv

2. Install requirements

    ```shell
    pip install -r requirements.ct
    ```

3. Execute

    ```shell
    uvicorn main:app --reload
    ```



## Testing with postman

POST:  http://0.0.0.0:8008/sentimiento/

BODY JSON:  {"data": "Amigo @metrodemedellin una pregunta, para ir a arreglar un inconveniente con mi cívica en qué estación es y puedo ir mañana domingo???"}


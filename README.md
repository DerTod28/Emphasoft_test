# Emphasoft_test
*Тестовое задание на позицию junior backend developer (python)*

Инструция по запуску

## Build and run docker-compose.yml

```shell
docker-compose -f docker-compose.dev.yml build --no-cache
```

## Makefile

run docker-compose:

```shell
make dev-docker-run
```

run pre-commit:

```shell
make precommit
```

run env genetations:

```shell
make env-gen-postgres
make env-gen-django
```

## Swagger-Ui documentation

http://127.0.0.1:8000/api/schema/swagger-ui/

## Endpoints

/users/

        -> login/ - login to get tokens
        -> login/refresh/ - refresh token
        -> me/ - current user
        -> signup/ - register a new user

After login you get access and refresh tokens

/rooms/

/rooms/ {id} /

/reservations/

/reservations/ {id} /

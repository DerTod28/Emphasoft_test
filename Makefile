.PHONY: dev-docker-down
dev-docker-down:
	docker-compose -f docker-compose.dev.yml down

.PHONY: dev-docker-build
dev-docker-build:
	docker-compose -f docker-compose.dev.yml build

.PHONY: dev-docker-build-no-cache
dev-docker-build-no-cache:
	docker-compose -f docker-compose.dev.yml build --no-cache

.PHONY: dev-docker-up
dev-docker-up:
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: dev-docker-run
dev-docker-run:
	docker-compose -f docker-compose.dev.yml down && docker-compose -f docker-compose.dev.yml up

.PHONY: precommit
precommit:
	pre-commit run --all-files

.PHONY: env-gen-postgres
env-gen-postgres:
	cat .ci/postgres/deploy/dev/.env.settings > .ci/postgres/deploy/dev/.env

.PHONY: env-gen-django
env-gen-django:
	cat .ci/django/deploy/dev/.env.settings > .ci/django/deploy/dev/.env

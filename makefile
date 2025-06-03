NAME = telegrambot
DIR = /opt/telegrambot

.PHONY: build up down restart logs clean redeploy

build:
	docker compose -f $(DIR)/docker-compose.yml build

up:
	docker compose -f $(DIR)/docker-compose.yml up -d

down:
	docker compose -f $(DIR)/docker-compose.yml down

restart: down up

logs:
	docker logs -f $(NAME)

clean:
	-docker rm -f $(NAME)
	-docker rmi $(NAME) || true

redeploy: clean build up
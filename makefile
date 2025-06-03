run:
	python bot/main.py

docker-build:
	docker build -t telegram-chatbot .

docker-run:
	docker run --env-file .env telegram-chatbot
all:
	docker-compose up --build
clean:
	docker system prune
fclean:
	docker system prune -a
istall:
	docker-compose up

bash:
	docker-compose exec app "/bin/bash"
reset:
	docker-compose stop
	docker-compose rm -f
	docker-compose build
	docker-compose up
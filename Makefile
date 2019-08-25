sh:
	docker-compose run --rm --service-ports app bash

clean:
	docker-compose down

.PHONY: setup
.DEFAULT: help
setup:
	@docker-compose up -d
	@docker-compose exec catalogs_web ./manage.py  migrate
	@docker-compose exec marketplace_web ./manage.py  migrate
	@docker-compose exec orders_web ./manage.py  migrate
	@docker-compose exec catalogs_web ./manage.py  loaddata fixtures/catalogs.json
	@docker-compose exec orders_web ./manage.py  loaddata fixtures/orders.json
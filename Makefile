mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


add:
	python3 manage.py loaddata learn.json
	python3 manage.py loaddata country.json
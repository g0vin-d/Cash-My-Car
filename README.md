# Cash-My-Car

Intructions:
1: First Create Virtual Environment

	virtualenv envName 
	source envName/bin/activate // to activate 

2: Install requirements

	pip install -r requirement.txt

3: To run project

	python manage.py migrate  
	python manage.py runserver
	python manage.py createsuperuser //to create admin ( optional )

4: other commands to remember

	python manage.py shell
	python manage.py makemigrations
	python manage.py sqlmigrate ----- ------
	deactivate (to deactivate virtual env later)	


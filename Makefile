help:
	cat Makefile

setup:
	virtualenv ./env --python=`which python3`
	./env/bin/pip install -r requirements

serve:
	./env/bin/python caduceus/manage.py migrate
	./env/bin/python caduceus/manage.py runserver

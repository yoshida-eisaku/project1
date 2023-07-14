cd Django-Simple-CRUD-Sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py runserver
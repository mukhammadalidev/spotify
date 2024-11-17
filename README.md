# spotify
python3 -m venv .venv
source .venv/bin/activate
pip3  install -r requirements.txt
python3 manage.py makemigrations migrate
python3 manage.py createsuperuser 
python3 manage.py runserver

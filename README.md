# alexandria

added something

Run these commands to install.

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd alexandria
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

docker build .
docker-compose build
docker-compose up

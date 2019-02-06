# UrlShortner
#creating virtual env
mkdir project
cd project
virtualenv .
source bin/activate

#clone the directory
git clone https://github.com/ricky1812/UrlShortner.git

#change directory
cd mysite

#Install dependencies
pip install -r requirements.txt

#Do migrations
python manage.py makemigrations
python manage.py migrate

#Run server
python manage.py runserver

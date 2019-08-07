# pi-django

# `Developer guide.`
Switch to MVP branch `git checkout mvp`

Install environment & dependencies.

``$ virtualenv --python=python3 venv``

``$ source venv/bin/activate``

`$ pip install -r requirements.txt` --ignore this for now

pip install the following
```
  $ pip install Pillow
   
  $ pip install twilio

  $ pip install xhtml2pdf

  
  $ pip install --upgrade django-crispy-forms
  $ pip install djangorestframework
  $ pip install markdown       # Markdown support for the browsable API.
  $ pip install django-filter  # 
  ```

Run Server

`$ python manage.py runserver`

`$ python manage.py syncdb`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`


Then create your working branch off mvp e.g `git branch fix/design` or `feat/design`

Then `checkout your branch` like `git checkout name-of-ur-branch`

While working please commit your work 
````
git add .

git commit -m "What i was working on"

git push orign  name-of-ur-branch if its the first commit `git push -u orign  name-of-ur-branch`
````

# kalar.codes
 Portfolio Website build in Django 3.2


## HOW TO RUN 
 Like with all Python projects, it's best to create a 
 new Python virtural environment to make sure you don't
 have conflicts bewteen dependencies. Once you have 
 cloned the repository, use the following command in
 the parent directory:

 `python -m venv <environment name>`

 The environment name is optional, but recommended.

 _Note: you may need to use `python3` if `python` doesn't work_

 Next run the virtual environment with the following command:

 MacOS and Linux:
 `source env/bin/activate`

 Windows:
 `.\env\Scripts\activate`


 Now that you have the environment running, install Django
 with the following command:

 `python -m pip install Django==3.2`

 Afer pip installs Django, change directories to the 
 repository and create a file called `local_variables.py`
 Inside that file, create the following lines:

 ```python
 SECRET_KEY = "1234567890password1"
 DEBUG = True
 ```

 Now you can run the server with the following command:
 
 `python manage.py runserver`

 And that's it. Now you can go to your localhost
 port 8000 and enjoy the website.

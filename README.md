# CoffeeShop app

cd starter/backend

virtualenv env
source env/Scripts/activate

pip install -r requirements.txt

be inside src/ for backend
FLASK_APP=api.py FLASK_ENV=development python -m flask run

AttributeError: module 'time' has no attribute 'clock' In SQLAlchemy python 3.8.2

    I had this issue with SQLAlchemy 1.2.10. Upgrading to the current version (1.3.18 as of now) fixed the problem

    pip install sqlalchemy --upgrade

if getting can't find flask, run flask like python -m flask run


- in frontend
    npm install
- had to look up answer to probelm when running npm start
- had to make sure package.json looked like gabe's original:
https://github.com/udacity/FSND/blob/master/projects/03_coffee_shop_full_stack/starter_code/frontend/package.json
- then npm install again
- then npm start worked



https://lb-fullstack.us.auth0.com/authorize?audience=drink&response_type=token&client_id=xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X&redirect_uri=http://127.0.0.1:8080/login-results


{
  "iss": "https://lb-fullstack.us.auth0.com/",
  "sub": "auth0|5fbd2b151bda000075e1928f",
  "aud": "drink",
  "iat": 1606233108,
  "exp": 1606240308,
  "azp": "xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X",
  "scope": "",
  "permissions": [
    "get:drinks-detail"
  ]
}


for testing tokens go to
https://lb-fullstack.us.auth0.com/authorize?audience=drink&response_type=token&client_id=xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X&redirect_uri=http://127.0.0.1:8080/login-results
in cognito browser

will need to do this whenever the tokens for manager and barista expire


--UPDATE!!!
permissions header seems to be working







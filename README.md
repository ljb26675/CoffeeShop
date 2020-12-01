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


Using auth0 debugger to get new tokens!! Will have to change callback url to other one when I need to







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

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJwU2dqQzFxRlNlZW9mUk9PS05SRyJ9.eyJpc3MiOiJodHRwczovL2xiLWZ1bGxzdGFjay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiZDJiMTUxYmRhMDAwMDc1ZTE5MjhmIiwiYXVkIjoiZHJpbmsiLCJpYXQiOjE2MDYyMzMxMDgsImV4cCI6MTYwNjI0MDMwOCwiYXpwIjoieFdtc2RDZGZyWHNZTWQycXdNdENwdXlxbHd1M0NMMFgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlsIl19.lFILNVJ38t75qO2pLw-CG8OqmP_9FRhrargOsQ1zqtvijenxPDcsDiw8cjjYn8zJzZw7BEO4roBbUwLpPO4my1BKodwbFbCKHMqOPXESCQ0CbkbWfSPvggqATEv882EQr9nB61klrp2Mriz9AvRs3bbnosKF2SRPuYrjtxXcmC6N6uccHw2VL8Q9X1s1reenkA4dsuEVMTiPiDclovc6juoaypB0RAcSaT3AIKlUxJ_RqKpXMm7zw-t9DagT1rdDZJ4oNmAHdAe8rhwrJHiJlsL7tcz7GSTKvAJwt0qnMMshO1lqbio7lxL-9j6L3000pL0KHg6upAk0Z9hBLYBGZA

{
  "iss": "https://lb-fullstack.us.auth0.com/",
  "sub": "auth0|5fbd2b29c29bd8006eafb99a",
  "aud": "drink",
  "iat": 1606234404,
  "exp": 1606241604,
  "azp": "xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X",
  "scope": "",
  "permissions": [
    "delete:drinks",
    "get:drinks-detail",
    "patch:drinks",
    "post:drinks"
  ]
}

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJwU2dqQzFxRlNlZW9mUk9PS05SRyJ9.eyJpc3MiOiJodHRwczovL2xiLWZ1bGxzdGFjay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZiZDJiMjljMjliZDgwMDZlYWZiOTlhIiwiYXVkIjoiZHJpbmsiLCJpYXQiOjE2MDYyMzQ0MDQsImV4cCI6MTYwNjI0MTYwNCwiYXpwIjoieFdtc2RDZGZyWHNZTWQycXdNdENwdXlxbHd1M0NMMFgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.Lfql45RI_V1h8LquNQ3HT7KDoJjzvLc6l6CBCTkBIk95RlLaVHTo63327LfDeKarpyC3RUWI5PFjbARE03xCL3Ez8bWEZXHdOBMpyvySbczqVUAjlPL7UArokPtrnl2olWZ2812fD5Xji2qftZCq_5ANFSYS1X-bSvKBiWM8Ek1KsWPMMdfO87N2odOorbKiH8aPbTSh9h6412WgdNEQ1JNy4BTiWd-vgzi_6GpvAw53orf721OWGwslaX093SPZA3-xn47MNY7g-Lcl3lfNhxHjb195jg7KiLS3geLwFOzbqM8eXMe55jhTAydDWAvfLqFbW5EeR-6wkk6wwWXYKQ



curl --request POST \
  --url 'https://lb-fullstack.us.auth0.com/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=password&username=barista@email.com&password=Test1234!&audience=drink&client_id=xWmsdCdfrXsYMd2qwMtCpuyqlwu3CL0X&client_secret=bJ0gpQ_7-uTJonchW1jfw7ek12NbVy21z4pVRCd3viNjFR-fE3_w3AiHrXCrjXKB"
 }'


WORKING ON?
 - currently working on making sure the api calls actually work, like for adding a drink
 
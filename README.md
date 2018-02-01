# Django OAuth2 Application

Test project that allows you to create OAuth2 applications and getting tokens by client app `Consumer`.

To test api you have to create new application. Go to [/consumer](http://localhost:8000/consumer/) and login. Then click on `Applications` and create new app with grand type: _Resource owner password-based_ and client type: _confidential_
Assuming your `client_id=qbmpPpuEnAvWoI8s55L9McafHwjHD8Wsjfm2oShu` and `client_secret=W39qCKpsUtXN7CchGxr9G2lgD8rLveo3gwd4eulClTuTnZKKidzx7DjUdWKIH8ndXyYFxZSKfqY6MUpzsZWGhuzscXKMpVardpsojMEoGfgjTy7jXUSgEfDwfwmLJCbo`

## Test API

At this point you are ready to request an access token:
```bash
curl -X POST -d "grant_type=password&username=test_user1&password=password_test_user1" -u"qbmpPpuEnAvWoI8s55L9McafHwjHD8Wsjfm2oShu:W39qCKpsUtXN7CchGxr9G2lgD8rLveo3gwd4eulClTuTnZKKidzx7DjUdWKIH8ndXyYFxZSKfqY6MUpzsZWGhuzscXKMpVardpsojMEoGfgjTy7jXUSgEfDwfwmLJCbo" http://localhost:8000/auth/token/
# response
{"access_token": "hu4P2IMQkrRObEx7QGXlXQ694jluTn", "expires_in": 360000, "token_type": "Bearer", "scope": "read write", "refresh_token": "HKTm13zavTQ64W44HSHsJliIcsV0kL"}
```

Now you can request user data:
```bash
curl -H "Authorization: Bearer hu4P2IMQkrRObEx7QGXlXQ694jluTn" http://localhost:8000/api/users/
# response
[{"id":2,"username":"test_user1","email":"test_user1@mail.com","first_name":"first","last_name":"user"}]
```

Api is per user protected, so this request is not allowed:
```bash
curl -H "Authorization: Bearer hu4P2IMQkrRObEx7QGXlXQ694jluTn" http://localhost:8000/api/users/1/
# response
{"detail":"Not found."}
```

Also you can make PUT request:
```bash
curl -H "Authorization: Bearer hu4P2IMQkrRObEx7QGXlXQ694jluTn" -X PUT -d"email=new_email_test_user1@mail.com" http://localhost:8000/api/users/2/
# response
{"id":2,"username":"test_user1","email":"new_email_test_user1@mail.com","first_name":"first","last_name":"user"}
```
## Test OAuth2

To test OAuth2 provider you can open app hosted at [heroku](https://test-django-oauth2-app.herokuapp.com).  
Click on _Applications_ and add new app with  
- _client type_: `confidential`,  
- _grant type_: `Authorizaiton code`,  
- _Redirect uris_: `https://test-django-oauth2-app.herokuapp.com/consumer/exchange/`  
then click save.  

Go to the main page and attempt to retrieve token. Hint: _Authorization url_ must be `https://test-django-oauth2-app.herokuapp.com/auth/authorize/` and the token url is: `https://test-django-oauth2-app.herokuapp.com/auth/token/`

## Documentation

Simple documentation available at [docs](https://test-django-oauth2-app.herokuapp.com/docs)

# BigBagAI


Register API

URL: ```http://127.0.0.1:8000/users/register/```

REQUEST BODY:

```
{
    "email": "syedkashifnaqvi142@gmail.com",
    "password": "testing",
    "first_name": "syed",
    "second_name": "kashif"
}

```

RESPONSE:

```
{
    "data": {
        "email": "syedkashifnaqvi14@gmail.com",
        "second_name": "kashif",
        "first_name": "syed"
    }
}
```

LOGIN API:

URL: ```http://127.0.0.1:8000/users/login/```


REQUEST BODY:
```
{
    "email": "syedkashifnaqvi14@gmail.com",
    "password": "testing"
}
```


RESPONSE:

```
{
    "email": "syedkashifnaqvi14@gmail.com",
    "tokens": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjQ3NDQ2NCwiaWF0IjoxNjk1MjY0ODY0LCJqdGkiOiJjMjQ0OTM2NjZjOWU0ZjhjYTk0ZmIyOWEyNjBjMmIxYyIsInVzZXJfaWQiOjF9.ft4n4zp93EiSOdIyUFHTruBla6KbA_pF5m4H36b6tpQ",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzUxMjY0LCJpYXQiOjE2OTUyNjQ4NjQsImp0aSI6IjliMjgyY2YwZDlhZjQ2NzdiNDIwNzIxZDhhNjdiYjk3IiwidXNlcl9pZCI6MX0.M4JOIMXCnZ7AN5F7wp4poR_v5O2HfUOTBpmPzAyIDo8"
    }
}
```




Note: Please replace localhost url ```http://127.0.0.1:8000``` with actual remote url
# Tests API for Stellar Burgers

[Website is here](https://stellarburgers.education-services.ru/)

[Docs is here](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-Stelar_Burger_10.25.pdf?etag=3584917d935c90b69cb3ffaff58d4f34)

## What tests are done

1. Create a user:
    * create a unique user:

    **REQUEST**

    ```bash
    curl POST -H 'Content-Type:application/json' -d '{"email":"cruiz12@example.net","password":"Qfdrfrrrffv123","name":"Sharon Chen53"}' https://stellarburgers.education-services.ru/api/auth/register
    ```

    **RESPONSE**

    ```json
    {
        "success": true,
        "user": 
            {
            "email":"cruiz@example.net",
            "name":"Sharon Chen52"
            },
        "accessToken":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY5ZTEyZGQxOTg0MjcwMDAxYmU4NTAzMyIsImlhdCI6MTc3NjM2NTAwOSwiZXhwIjoxNzc2MzY2MjA5fQ.dFM9n85h6t3RhtSEigN4MK33kieat-SNRsMg-SP5CiE",
        "refreshToken":"dc2f0e7ad6ba8baadf5e29016d709547f6a31d5f5127afb00129889321a7564550e3c39041567c32"
    }
    ```

    * create a user with existent data:

    **REQUEST**

    ```bash
    curl POST -H 'Content-Type:application/json' -d '{"email":"cruiz12@example.net","password":"Qfdrfrrrffv123","name":"Sharon Chen53"}' https://stellarburgers.education-services.ru/api/auth/register
    ```

    **RESPONSE**

    ```json
        {
            "success":false,
            "message":"User already exists"
        }
    ```

    * create a user without a required field.
  
        email required:

    **REQUEST**

    ```bash
    curl POST -H 'Content-Type:application/json' -d '{"password":"Qfdrfrrrffv123","name":"Sharon Chen53"}' https://stellarburgers.education-services.ru/api/auth/register
    ```

    **RESPONSE**

    ```json
    {"success":false,"message":"Email, password and name are required fields"}
    ```

2. Login:
    login with existent user data;

    **REQUEST**

    ```bash
    curl POST -i -H 'Content-Type:application/json' -d '{"email":"cruiz12@example.net","password":"Qfdrfrrrffv123"}' https://stellarburgers.education-services.ru/api/auth/login
    ```

    **RESPONSE**

    ```json
    HTTP/1.1 200 OK
    Server: nginx/1.24.0 (Ubuntu)
    Date: Sat, 18 Apr 2026 14:27:21 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 371
    Connection: keep-alive
    X-Powered-By: Express
    Access-Control-Allow-Origin: *
    ETag: W/"173-n6/Ps1FpoLkw1H+EbTuHkFGlqVw"

    {"success":true,"accessToken":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6I
    kpXVCJ9.eyJpZCI6IjY5ZTEzMmQ0OTg0MjcwMDAxYmU4NTE2OSIsImlhdCI6MTc3NjU
    yMjQ0MSwiZXhwIjoxNzc2NTIzNjQxfQ.OdOs2y8vvb32DVPg6olTQbAOpyibStOe73k
    QONLvTxM","refreshToken":"7f5a54764edf0372c6b6d16894fa6789460ee0da6
    4ab9fa5d64109c64739a762d6a7308db2cabe6f","user":{"email":"cruiz12@e
    xample.net","name":"Sharon Chen53"}}
    ```

    login with wrong data:
    **REQUEST**

    ```bash
    curl POST -i -H 'Content-Type:application/json' -d '{"email":"cr1111111111iz12@example.net","password":"Qfdrfrrrffv123"}' https://stellarburgers.education-services.ru/api/auth/login
    ```

    **RESPONSE**

    ```json
    HTTP/1.1 401 Unauthorized
    Server: nginx/1.24.0 (Ubuntu)
    Date: Sat, 18 Apr 2026 14:39:13 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 61
    Connection: keep-alive
    X-Powered-By: Express
    Access-Control-Allow-Origin: *
    ETag: W/"3d-ad9nrqlzQBuoZ0AId1U3rIgKU84"

    {"success":false,"message":"email or password are incorrect"}
    ```

3. Change user data:
    change user data by an auth user;
    change user data by the guest;

```bash
Для обеих ситуаций нужно проверить, что любое поле можно изменить. Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
```

4. Create an order:
    create an order by an auth user;
    create an order by the guest;

```bash
с ингредиентами,
без ингредиентов,
с неверным хешем ингредиентов.
```

5. Get a list of orders of a user:
    get a list of orders of a user by an auth user;
    get a list of orders of a user by the guest.

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

2. Login:
    login with existent user data;
    login with wrong data;

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

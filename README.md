Sample project to show up a problem with Django querysets being printed after exceptions
========================================================================================

To see the problem happening, I created a Django project with a simple view
that has an exception after initiating the serializer instance.

You can see the problem by executing:

```
docker-compose build app
docker-compose up db app
```

This would start Django development server and a local PostgreSQL database set
to print any query executed.

On another terminal, you can execute the problematic view through:

```
docker-compose exec app ./test.py
```

You will see the queryset to the whole user's table being executed (because the
serializer string representation is performed by Django automatically).

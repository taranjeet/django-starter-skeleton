# {{project_name}}

To generate `SECRET_KEY` use this command

```
$ python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))'
```

# git hub 수업 참고

### Contributing
- scenario #1
```bash
# setiing SSH
$ git clone <URL>
$ git branch <ver>/<NAME>
$ git checkout <ver>/<NAME>
$ git push
# make PR
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```
- scenario #2
```bash
$ git branch -r
$ git checkout -t origin/<ver>/<NAME>
# doing ...
# dogng ...
$ git add <FILE_NAME>
$ git commit -m "<MESSAGE>"
$ git push

# merge main -> deploy
# releases & tag
```

### Use
- https://agecal.wodan10.shop/


### Dev
```bash
$ pyenv global
3.10.12
$ python -V
python 3.10.12
# $ python -m venv venv
$ source venv/bin/activate
$ uvicorn api.index:app --reload
```


### Ref
- https://docs.python.org/ko/3.10/library/datetime.html

# machine-learning-project
Creating conda environment
```
conda create -p <environment_name> python==3.7 -y
```

Activating environment
``` 
conda activate <environment_name>/
```

To install all the libraries present in requirements.txt file
``` 
pip install -r requirements.txt
```

To check git status
```
git status
```

To check logs
```
git log
```

To add files in git
```
git add .
```

To commit changes in git
```
git commit -m"message"
```

To send version/changes in git
```
git push origin main
```

To check remote url
```
git remote -v
```

To set up CI/CD pipeline in heroku we need these information
1. Heroku API Key
2. Application name( in heroku)
3. Email id

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .
```
> Note: name of the docker shuld be in lowercase

To list docker images
```
docker images 
```


Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```


To check running images in docker
```
docker ps
```

To stop docker container 
```
docker stop <container_id>
```

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
in this app:app means first app is module name(app.py) and second app is name of the Flask object(app=Flask) 

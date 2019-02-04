# RMOTR Docker Images

Build the images:

```bash
$ make build
````

Run Jupyter labs in docker:

```bash
docker run -p 5000:8888 -p 5001:8080 -e JUPYTER_TOKEN=1234 -e SHELL=/bin/bash -v $(pwd):/app/user_data -it data-science-python-3.6 jupyter lab --allow-root
```

Examples:
* https://hub.docker.com/r/waleedka/modern-deep-learning/~/dockerfile/
* https://gist.github.com/orenitamar/f29fb15db3b0d13178c1c4dd611adce2

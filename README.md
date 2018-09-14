<p align="center"><img width="400" src="https://user-images.githubusercontent.com/872296/27511815-0e1cb62e-5904-11e7-8fe0-e1116e7a6ced.png"></p>

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

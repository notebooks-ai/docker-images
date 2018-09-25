PHONY: status start stop

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PACKAGE=linked_list

build:
	@echo $(TAG)Building Images$(END)
	@echo $(TAG)Building Py 3.6$(END)
	sudo docker build -t base-python:3.6 images/python/base-python/py-3.6

	@echo $(TAG)Building Py 2.7$(END)
	sudo docker build -t base-python:2.7 images/python/base-python/py-2.7

	@echo $(TAG)Building Data Science$(END)
	sudo docker build -t data-science:python images/python/data-science
	
	@echo $(TAG)Building Deep Learning$(END)
	sudo docker build -t deep-learning images/python/deep-learning

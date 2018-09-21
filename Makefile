PHONY: status start stop

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PACKAGE=linked_list

build:
	@echo $(TAG)Building Images$(END)
	sudo docker build -t base-python:3.6 images/python/base-python/py-3.6
	sudo docker build -t base-python:2.7 images/python/base-python/py-2.7

	docker build -t data-science:python data-science

	docker build -t deep-learning deep-learning

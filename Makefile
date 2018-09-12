PHONY: status start stop

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PACKAGE=linked_list

build:
	@echo $(TAG)Building Images$(END)
	docker build -t data-science-python-3.6 images/python/data-science/py-3.6

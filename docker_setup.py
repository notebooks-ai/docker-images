import docker
from os.path import join, dirname, realpath

BASE_PATH = dirname(realpath(__file__))

IMAGES_TO_BUILD = {
    # 'python-2.7-testing': 'images/python/testing/py-2.7',
    # 'python-3.5-testing': 'images/python/testing/py-3.5',
    # 'python-3.6-testing': 'images/python/testing/py-3.6',
    #
    # 'python-2.7-django-1.10': 'images/python/django/py-2.7/dj-1.10',
    # 'python-2.7-django-1.11': 'images/python/django/py-2.7/dj-1.11',
    #
    # 'python-3.5-django-1.10': 'images/python/django/py-3.5/dj-1.10',
    # 'python-3.5-django-1.11': 'images/python/django/py-3.5/dj-1.11',
    #
    # 'python-3.6-django-1.10': 'images/python/django/py-3.6/dj-1.10',
    # 'python-3.6-django-1.11': 'images/python/django/py-3.6/dj-1.11',

    'data-science-python-3.6': 'images/python/data-science/py-3.6',
}


def build_docker_images(images=IMAGES_TO_BUILD):
    client = docker.from_env()
    for tag, path in images.items():
        full_path = join(BASE_PATH, path)
        image = client.images.build(path=full_path, tag=tag, quiet=False)
        print("Built: %s" % image.tags[0].split(":")[0])


if __name__ == '__main__':
    build_docker_images()

# docker rm -f $(docker ps -aq) && docker rmi $(docker images --filter "dangling=true" -q --no-trunc) && docker rmi $(docker images -q)

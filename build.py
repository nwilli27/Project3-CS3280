from pybuilder.core import use_plugin
from pybuilder.core import init
from pybuilder.core import Author
from pybuilder.core import task, depends

from subprocess import call
from os import path

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "NolanWilliamsProject2"
default_task = "publish"
target_dir = path.join('main', 'python')

@init
def normalize_target_dir(project):
    project.set_property('dir_dist', target_dir)

@init
def copy_html_pages_to_distribution(project):
    project.set_property('copy_resources_target', target_dir)
    project.set_property('copy_resources_glob', ['*.html', '*.HTML', '*.htm', '*.HTM'])

@task
def run_http_server(project):
    call([
        'python',
        path.join(target_dir, 'service.py')
    ])


@init
def set_properties(project):
    pass

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    ]

install_links = [
    'git@github.com:marrow/web.dispatch.object.git#egg=web.object.dispatch'
    ]

setup(name='Pyramid_Object_Dispatch',
      version='0.1',
      description='Pyramid object based dispatching',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Darrol Jordan Duty',
      author_email='djdduty',
      url='djdduty.com',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      dependency_links=install_links
      )

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='naaya.selenium',
      version=version,
      description="Selenium functional test suite for Naaya",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Eaudeweb',
      author_email='office@eaudeweb.ro',
      url='http://naaya.eaudeweb.ro/',
      license='MPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['naaya'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'selenium',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [distutils.commands]
            naaya_selenium = naaya.selenium.runtests.main
      """,
      )

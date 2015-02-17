from setuptools import setup

import nginxplain

requirements = (
    'Flask==0.10.1',
)

setup(name='nginxplain',
      packages=('nginxplain',),
      include_package_data=True,
      zip_safe=False,
      author='Jacob Oscarson',
      author_email='jacob@plexical.com',
      install_requires=requirements,
      version=nginxplain.version)

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='kmlistfi',
      version='0.01.0',
      description='Get filepaths to all files Below a folder node',
      author='Keith Murray',
      author_email='kmurrayis@gmail.com',
      license='MIT',
      packages=['kmlistfi'],
      install_requires=[
	  
      ],
      zip_safe=False)

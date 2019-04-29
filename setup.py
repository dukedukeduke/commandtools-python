from setuptools import setup, find_packages



setup(name='commandtools',

      version='0.1',

      url='',

      license='MIT',

      author='duke.yang',

      author_email='duked.yang@gmail.com',

      description='comamnd tools',

      packages=find_packages(where='.', exclude=[], include=('*',)),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=[],

      test_suite='')
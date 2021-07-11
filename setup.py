from setuptools import setup

setup(name='input_num',
      version='0.1.0',
      description='Python package - input_num is like input but it only accepts numbers',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/HexagonCore/input_num',
      author='Hexagon Core Development',
      author_email='mp3martin.developer@gmail.com',
      license='MIT',
      packages=['input_num'],
      install_requires=[
          'markdown',
          'requests'
      ],
      zip_safe=False)

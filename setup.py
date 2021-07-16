from setuptools import setup
import re
import ast


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('input_num/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))



setup(name='input_num',
      version=version,
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

from setuptools import setup, find_packages

setup(
    name='cfdi',
    version='0.1.0',
    description='CFDI',
    url='https://github.com/isaacsancheza/cfdi',
    author='Isaac Sánchez',
    author_email='isaacsancheza@outlook.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['lxml'],
)

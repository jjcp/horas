from setuptools import setup, find_packages


setup(
    name='horas',
    version='0.0.1a3',
    description='Registro de horas',
    license='GPLv2',
    author='Juan Cabrera',
    author_email='jjcp.91@gmail.com',
    packages=find_packages(),
    scripts=['hs'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    url='https://bitbucket.org/jjcp/horas',
)

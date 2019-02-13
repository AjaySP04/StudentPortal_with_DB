from setuptools import find_packages, setup

setup(
    name='student_db',
    version='1.0.0',
    description='Student Portal CRUD app using SQLite Relational database.',
    url='https://github.com/AjaySP04/StudentPortal_with_DB',
    author='Ajay Singh Parmar',
    author_email='ajays.parmar04@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-wtf'
    ],
)

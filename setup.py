from distutils.core import setup

setup(
    name='django-auditlog',
    version='1.4.1',
    packages=['auditlog', 'auditlog.migrations'],
    package_dir={'': 'src'},
    url='https://github.com/jjkester/django-auditlog',
    license='MIT',
    author='Jan-Jelle Kester',
    description='Audit log app for Django',
    install_requires=[
        'Django>=1.8',
        'git+https://github.com/rocketrip/django-jsonfield.git>1.0.3'
    ],
    zip_safe=False
)

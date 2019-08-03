from setuptools import setup

install_requires = (
    'django>=2.1',
)

test_requries = (
    'pytest',
    'pytest-django',
    'pytest-cov',
    'pytest-pythonpath',
    'tox',
    'django-extensions',
)

setup(
    name='seshat',
    version='0.0.1',
    author='deadlylaid@gmail.com',
    url='https://github.com/deadlylaid/seshat',
    install_requires=install_requires,
    test_requries=test_requries,
    extras_require={
        'test': test_requries,
    }
)

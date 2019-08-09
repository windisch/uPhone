from setuptools import setup
import sys


if sys.implementation.name == 'micropython':
    import sdist_upip
    cmdclass={'sdist': sdist_upip.sdist},
    install_requires = [
        "micropython-logging"
    ]

else:

    cmdclass={}
    install_requires = []

setup(
    name="uphone",
    version="0.0.1",
    packages=["uphone"],

    # dependencies
    install_requires=install_requires,
    tests_require=[
        "pytest",
    ],

    # metadata for upload to PyPI
    author="Tobias Windisch",
    author_email="tobias.windisch@posteo.de",
    description="A baby phone running on MicroPython",
    license="GNU GPL3",
    cmdclass=cmdclass,
    keywords="baby phone micropyhton",
    url="https://github.com/windisch/uPhone",
)

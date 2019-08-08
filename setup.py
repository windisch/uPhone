from setuptools import setup

setup(
    name="uphone",
    version="0.0.1",
    packages=["uphone"],

    # dependencies
    install_requires=[
        "pytest",
    ],
    # metadata for upload to PyPI
    author="Tobias Windisch",
    author_email="tobias.windisch@posteo.de",
    description="A baby phone running on MicroPython",
    license="GNU GPL3",
    keywords="baby phone micropyhton",
    url="https://github.com/windisch/uPhone",
)

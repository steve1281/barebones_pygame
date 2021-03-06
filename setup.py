from setuptools import setup, find_packages

NAME = "game"
VERSION = "0.0.1"

REQUIRES = [
]

long_description = "Longer Markdown; sometimes we just read in the README.md file"

setup(
    name=NAME,
    extras_require=dict(test=['pytest']),
    version=VERSION,
    description="Description of the project",
    install_requires=REQUIRES,
    packages=find_packages('src'),
    package_dir={"": "src"},
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    use_scm_version = {
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp"
    },
    package_data={'': ['resources/*.*']},
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts":["the_game = game.__main__:main"]
    },
    long_description=long_description,
)

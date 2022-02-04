import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='plotlytron',
    version='0.0.1',
    author='Sebastian Mack',
    author_email='mack.seb@gmail.com',
    description='Personal Plotly Theme Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mackseb/themes',
    project_urls = {
        "Bug Tracker": "https://github.com/mackseb/themes/issues"
    },
    license='MIT',
    packages=['plotlytron'],
)
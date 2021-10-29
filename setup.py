# Måste ligga utanför "MyFunctions"
import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='MyOwnFunctions',
    version='0.0.2',
    author='Axel Wieslander Jansson',
    author_email='axl_wieslander@hotmail.com',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Axelwieslander/goodtohave',
    project_urls={
        "Bug Tracker": "https://github.com/aspcodenet/goodtohave/issues"
    },
    license='MIT',
    packages=['MyOwnFunctions'],
    install_requires=['requests']
)

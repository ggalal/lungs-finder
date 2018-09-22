from setuptools import setup, find_packages

setup(
    name="lungs_finder",
    version="1.0.0",
    description="Library that helps you to find lungs on chest X-ray (CXR) images for further processing",
    author="Galal Galal adapted from Maksym Kholiavchenko",
    author_email="ggalal@gumich.edu",
    url="https://github.com/ggalal/lungs-finder",
    license="Apache-2.0",
    packages=find_packages(),
    package_data={"lungs_finder": ["*.xml", "*.np"]}
)

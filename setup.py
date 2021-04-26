from setuptools import find_packages, setup

setup(
    name="my-package",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "my_package_with_extra @ git+ssh://git@github.com/yuvalmarciano/my-package-with-extra.git@1.0.0",
    ],
)

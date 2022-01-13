from setuptools import setup, find_packages


def load_requires_from_file(filepath):
    with open(filepath) as fp:
        return [pkg_name.strip() for pkg_name in fp.readlines()]


setup(
    name='mySample',  # パッケージ名
    version="0.0.1",
    description="MySmqplePackageCode",
    long_description="",
    author='watagori',
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
    packages=['view', 'model'],  # パッケージのサブフォルダー
    install_requires=['web3']
)

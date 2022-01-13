from setuptools import setup, find_packages

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
    packages=['view', 'model']  # パッケージのサブフォルダー
)

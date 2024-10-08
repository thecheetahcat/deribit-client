from setuptools import setup, find_packages


def parse_requirements():
    with open("requirements.txt", "r") as requirements:
        return requirements.read().splitlines()


setup(
    name='deribit_client',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements(),
    description='Deribit exchange client',
    author='Leo Martinez',
    author_email='leojmartinez@proton.me',
    url='https://github.com/thecheetahcat/deribit-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)

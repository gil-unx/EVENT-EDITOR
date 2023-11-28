from distutils.core import setup
from setuptools import find_packages

setup(
    name='PyTexturePacker',
    packages=find_packages(exclude=['docs', 'tests', 'test_image']),
    version='1.1.0',
    description='an package to create sprite sheets or sprite atlases',
    author='Quanyong Huang',
    author_email='quanyongh@foxmail.com',
    url='https://github.com/wo1fsea/PyTexturePacker',
    download_url='https://github.com/wo1fsea/PyTexturePacker/releases/tag/v1.1.0',
    keywords=['TexturePacker', 'cocos2d-x', 'sprite-sheet', 'texture-pack'],
    license='MIT',
    install_requires=['Pillow'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

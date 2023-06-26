from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent.resolve()
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='pychame',
    version='1.0.0.beta',
    description='A simple way to use the Chromebook integred camera within OpenCV',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Lucas Barros',
    author_email='lucas.barros1804@gmail.com',
    url="https://github.com/LucasOliveiraaa/Pychame",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={
        '': ["index.html","cert.pem","key.pem"]
    },
    install_requires=[
        'flask',
        'opencv-python',
        'numpy'
    ],
    python_requires=">=3.7, <4",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
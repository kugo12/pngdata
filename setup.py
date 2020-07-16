import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pngdata",
    version="1.0.0",
    author="kvgx12",
    description="Write data to PNG file format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kugo12/pngdata",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Pillow'
    ]
)
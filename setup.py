from setuptools import find_packages, setup

setup(
    name="eztts",
    version="0.3.0",
    description="A simple, easy-to-use interface for multiple text-to-speech engines",
    url="https://github.com/trevin-j/eztts",
    author="Trevin Jones",
    author_email="trevindjones@gmail.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "eztts = eztts.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="text-to-speech",
    long_description="A package that creates a uniform interface for dealing with multiple different TTS engines. It is modular and easy to extend.",
)
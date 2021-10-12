from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="text_split",
    version="0.1.0",
    description="split text by lineno",
    long_description=long_description,
    long_description_content_tpye="text/markdown",
    author="Qian",
    author_email="gokinjolno112358@gmail.com",
    license="MIT",
    packages=["text_split"],
    entry_points = {
        "console_scripts": ["split=text_split.split:main"]
    }
)
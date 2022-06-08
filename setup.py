from setuptools import setup, find_packages

setup(
    version="0.4",
    name="franz-blog",
    author="Franz Bandelin, copied from Mathias Brito",
    author_email="franz@whatever.com",
    description="This is the blog system created by Mathias and then crippled by Franz",
    long_description="I still hate Testpypy naming conventions!",
    url="https://github.com/Hans-Lambda/franz-python-deployment-blog",
    license="MIT",
    keywords="blog bms",
    requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": ['blog=blog.main:main']
    }
)

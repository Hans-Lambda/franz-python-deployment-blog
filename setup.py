from setuptools import setup, find_packages

setup(
    version="0.7",
    name="franz-blog",
    author="Franz Bandelin, copied from Mathias Brito",
    author_email="franz@whatever.com",
    description="This is the blog system created by Mathias and then crippled by Franz - changed description to see if token works - changed again to start with 'funny' ",
    long_description="I still hate Testpypy naming conventions! Why the fuck isn't it enough that I changed the version number? What do you want from me??",
    url="https://github.com/Hans-Lambda/franz-python-deployment-blog",
    license="MIT",
    keywords="blog bms",
    requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": ['funny=blog.main:main']
    }
)

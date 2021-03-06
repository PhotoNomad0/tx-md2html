from setuptools import setup

setup(
    name="tx-md2html",
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Unit test setup file.",
    license="MIT",
    keywords="",
    url="https://github.org/unfoldingWord-dev/tx-md2html",
    long_description='Unit test setup file',
    classifiers=[],
    install_requires=[
        'markdown',
        'requests',
        'tx-shared-tools'
    ],
    test_suite='tests'
)

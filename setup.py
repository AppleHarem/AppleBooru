from setuptools import setup, find_packages

setup(
    name='applebooru',
    version='1.0.0-beta.2',
    author='ChenMoe',
    description='A wrapper for Danbooru API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your_package_name',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.1',
    ],
)
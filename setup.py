from distutils.core import setup

setup(
    name = 'dict_filter',
    packages = ['dict_filter'],
    version = '0.1',
    license='MIT',
    description = 'A simple library for extracting multiple values from a large dictionary or JSON object',
    author = 'Dan Stuart',
    author_email = 'drestuart@gmail.com',
    url = 'https://github.com/drestuart/dict_filter',
    download_url = 'https://github.com/drestuart/dict_filter/archive/v_01.tar.gz',
    keywords = ['dict', 'dictionary', 'json'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
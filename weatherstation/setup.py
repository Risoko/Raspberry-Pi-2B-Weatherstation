from setuptools import setup, find_packages

setup(
    name='weatherstation',
    version='1',
    packages=find_packages(),
    include_package_data=True,
    author='TeKaPol',
    author_email='przemyslaww.rozyckii@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3.5.3'
    ],
)
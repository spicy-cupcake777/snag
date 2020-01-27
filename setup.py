import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
        name='snag',
        version='0.1',
        scripts=['snag.py'],
        author='Cassandra Gentry',
        author_email='cassiegentlekitty@gmail.com',
        description='An HTML utility package',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=setuptools.find_packages(),
        install_requires= [
            'requests',
            'bottle'
        ],
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GPL',
            'Operating System :: OS Independent'
        ]
)

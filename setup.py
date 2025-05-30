from setuptools import setup, find_packages

setup(
    name='omnigenai_toolkit',
    version='1.0.1',
    description='A Python package for Generative AI applications',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Gopalakrishnan Arjunan',
    author_email='gopalakrishnana02@gmail.com',
    url='https://github.com/gopalakrishnanarjun/omnigenai_toolkit.git',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

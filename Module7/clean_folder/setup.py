from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Checking and leaning your folder',
    url='http://kotfriend.com/clean_folder',
    author='kotfriend hub community',
    author_email='eugene.shulzhenko@gmail.com',
    license='GoIT',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']},
    packages=find_packages()
)
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


setup_args = dict(
    name='efsane-fixture',
    version='1.0.0',
    description='Create Own Sport Fixtures',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.xml"],
    },
    install_requires=[],
    author='Arif Mehniyar',
    author_email='arif.mehniyar@gmail.com',
    keywords=['sport', 'fixture', 'team-fixture', 'leage-fixture', 'basketball', 'football'],
    url='https://gitlab.com/pgdepot/mp_agent',
    download_url='https://pypi.org/project/mp_agent/'
)

if __name__ == '__main__':
    setup(**setup_args)

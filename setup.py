from setuptools import setup,find_packages

with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='src',
    version='0.0.1',
    author='abhilash panda',
    description='this is a simple ml pipeline file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abhilashpanda04/ml_pipeline.git',
    author_email='abhilashk.isme1517@gmail.com',
    # package_dir={"":"src"},
    # packages=find_packages(where='src'),
    packages=['src'],
    python_requires='>=3.6',
    license='GNU',
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
    ) 
from setuptools import setup, find_packages

setup(
    name='chatteract',  # The name of your package
    version='0.1',  # The current version of your package
    packages=find_packages(),  # List of all python packages to include. find_packages() automatically detects all packages and subpackages.
    author='Mattias Aspelund',  # Your name    
    description='A package to handle OpenAI responses and execute function calls.',  # A brief description of your package
    url='https://github.com/aspelund/chatter-act',  # Link to the github repo or website
    classifiers=[  # Classifiers help users find your project by categorizing it.
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'tiktoken',
        # add any additional packages that your software needs
    ],  # List of dependencies that Python will automatically install alongside your package
    python_requires='>=3.6',  # Minimum version of Python your package requires
)

import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='humai-certifica-ai',
    version='0.1.0',
    author='Hugo C Galvan',
    author_email='hcgalvan@gmail.com',
    description='Evaluador de posturas embebido en app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hcgalvan/humai-certifica-ai',
    project_urls = {
        "Bug Tracker": "https://github.com/hcgalvan/humai-certifica-ai/issues"
    },
    license='MIT',
    packages=['pnn_mvp'],
    install_requires=['requests'],
)
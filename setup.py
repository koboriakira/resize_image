from setuptools import setup, find_packages

setup(
    name="resize_image",
    version='1.0',
    description='画像を16:9にリサイズ',
    author='Kobori Akira',
    author_email='private.beats@gmail.com',
    url='https://github.com/koboriakira/resize_image',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      resize = resize_image.cli:execute
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)

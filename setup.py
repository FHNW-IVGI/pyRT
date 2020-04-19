"""
pyRT - The Python Raytracer

This is the Setup-Script...
"""

#calls for installation:
#    python3 setup.py install
#
#calls for distribution:
#    set HOME=C:\users\username    # or wherever your .pypirc is
#    python3 setup.py sdist
#    python3 setup.py sdist upload
#or by using twine:
#    python setup.py sdist bdist_wheel
#    python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# README.rst was created using: run pandoc --from=markdown --to=rst --output=README.rst README.md
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyrt',
    packages=['pyrt',
              'pyrt.camera',
              'pyrt.geometry',
              'pyrt.light',
              'pyrt.material',
              'pyrt.math',
              'pyrt.renderer',
              'pyrt.scene',
              'pyrt.utils'],
    package_dir={
        'pyrt.camera': 'pyrt/camera',
        'pyrt.geometry': 'pyrt/geometry',
        'pyrt.light': 'pyrt/light',
        'pyrt.material': 'pyrt/material',
        'pyrt.math': 'pyrt/math',
        'pyrt.renderer': 'pyrt/renderer',
        'pyrt.scene': 'pyrt/scene',
        'pyrt.utils': 'pyrt/utils'
    },
    package_data={'pyrt': ['camera/*.py']},
    include_package_data=True,
    version='0.5.3',
    description='pyRT - The Python Raytracer',
    long_description=long_description,
    url='https://github.com/martinchristen/pyRT',
    author='Martin Christen',
    author_email='martin.christen@gmail.com',
    license='MIT',
	long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8'
    ],
    keywords=['raytracing','3d-graphics'],
)
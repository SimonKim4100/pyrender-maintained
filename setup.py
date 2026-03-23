"""
Setup of pyrender Python codebase.

Author: Matthew Matl
"""
from setuptools import setup

# load __version__
exec(open('pyrender/version.py').read())

requirements = [
    'freetype-py',                # For font loading
    'imageio',                    # For Image I/O
    'networkx',                   # For the scene graph
    'numpy>=2.0',                 # Numpy
    'Pillow',                     # For Trimesh texture conversions
    'pyglet>=2.0',                # For the pyglet viewer
    'PyOpenGL>=3.1.0',            # For OpenGL
    'scipy',                      # Because of trimesh missing dep
    'trimesh',                    # For meshes
]

dev_requirements = [
    'flake8',            # Code formatting checker
    'pre-commit',        # Pre-commit hooks
    'pytest',            # Code testing
    'pytest-cov',        # Coverage testing
    'tox',               # Automatic virtualenv testing
]

docs_requirements = [
    'sphinx',            # General doc library
    'sphinx_rtd_theme',  # RTD theme for sphinx
    'sphinx-automodapi'  # For generating nice tables
]


setup(
    name = 'pyrender',
    version=__version__,
    description='Easy-to-use Python renderer for 3D visualization',
    long_description='A simple implementation of Physically-Based Rendering '
                       '(PBR) in Python. Compliant with the glTF 2.0 standard.',
    author='Matthew Matl',
    author_email='matthewcmatl@gmail.com',
    license='MIT License',
    url = 'https://github.com/mmatl/pyrender',
    python_requires='>=3.11',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
    ],
    keywords = 'rendering graphics opengl 3d visualization pbr gltf',
    packages = ['pyrender', 'pyrender.platforms'],
    install_requires = requirements,
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
    include_package_data=True
)

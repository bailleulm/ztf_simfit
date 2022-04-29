from setuptools import setup

# get the version here
pkg_vars = {}

with open("version.py") as fp:
    exec(fp.read(), pkg_vars)

setup(
    name='ztf_simfit',
    version=pkg_vars['__version__'],
    description='',
    url='http://github.com/pgris/ztf_simfit',
    author='M. Bailleul, Ph. Gris',
    author_email='manon.bailleul@etu.uca.fr,philippe.gris@clermont.in2p3.fr',
    license='BSD',
    packages=['ztf_simfit', 'ztf_simfit_input', 'ztf_data', 'ztf_simfit_plot'],
    package_data={'ztf_simfit_input': ['*.txt'], 'ztf_data': ['*.txt']},
    python_requires='>=3.5',
    zip_safe=False,
    install_requires=[
        'ztf_pipeutils>=0.1',
        'sncosmo>=1.3.1',
        'simsurvey >=0.1',
        'dustmaps',
        'iminuit'
    ],
)

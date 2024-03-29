from setuptools import find_packages
from numpy.distutils.core import setup

requirements = "requirements.txt"
setup(
    name = 'njoytk',
    version = '0.1',
    description = '',
    #long_description = long_description,
    # url='https://github.com/pypa/sampleproject',
    author = 'Luca Fiorito',
    author_email = 'lucafiorito.11@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        ],
#    keywords = 'uncertainty, nuclear data, covariance, sampling, sensitivity',
    packages = find_packages(),
#    install_requires = open(requirements).read().splitlines(),
    zip_safe = False,
#    setup_requires=["pytest-runner",],
    tests_require=["pytest",],
    include_package_data = True,
#    entry_points={
#    'console_scripts': [
#        'sandy=sandy.sampling.sampling:run',
#        'sandy_tests=sandy.sampling.tests:runtests',
#        'sandy_xs_plotter=sandy.sampling.plotter2:main',
#        'sandy_njoy=sandy.njoy.njoy:process_lib'
#        ],
#    },
)

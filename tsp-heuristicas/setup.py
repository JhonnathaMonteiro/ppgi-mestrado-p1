
from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: Portuguese',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: BSD',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Education',
]


setup(
    name='TSP',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    version='0.1',
    description='Pacote com a resolução das atividades do terceiro estagio',
    author='Jhonnatha de Andrade Monteiro',
    long_description=open('README.md').read(),
    author_email='jhonnatha.am@gmail.com',
    url='https://github.com/JhonnathaMonteiro/AtividadeFinalEstrutura',
    keywords=['algorithms', 'python3'],
    classifiers=classifiers,
    #   package_data={'<package_name>': ['<package_data>/*']}
)

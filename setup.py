from setuptools import setup


setup(
    name='thonny-onedark',
    version='0.1.0',
    description='One Dark theme for Thonny IDE',
    long_description=open('README.md').read(),
    url='https://github.com/ranelpadon/thonny-onedark',
    download_url='https://github.com/ranelpadon/thonny-onedark',
    author='Ranel Padon',
    author_email='ranel.padon@gmail.com',
    license='MIT',
    packages=['thonnycontrib.onedark'],
    include_package_data = True,
    install_requires=['thonny >= 3.0.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: Software Development :: Embedded Systems',
    ],
    keywords='IDE education programming Thonny dark theme one-dark "one dark"',
    platforms=['Windows', 'macOS', 'Linux'],
)
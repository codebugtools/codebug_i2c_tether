#!/bin/bash
python setup.py --command-packages=stdeb.command sdist_dsc

version=$(cat codebug_i2c_tether/version.py | sed 's/.*\([0-9]\.[0-9]\.[0-9]\).*/\1/')
cd deb_dist/codebug-i2c-tether-$version/

cp {../../dpkg-files,debian}/control
cp {../../dpkg-files,debian}/copyright
cp {../../dpkg-files,debian}/rules
cp {../../dpkg-files,debian}/python-codebug-i2c-tether.install
cp {../../dpkg-files,debian}/python3-codebug-i2c-tether.install

dpkg-buildpackage -us -uc

#!/usr/bin/env python3
import os
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.install import install


class NPMInstall(build_py):
    def run(self):
        target_dir = os.path.join(self.build_lib, 'django_vue_rollup')
        os.makedirs(os.path.join(target_dir, 'npm_prefix', 'node_modules'), exist_ok=True)
        npm_cmd = [
            'npm', 'install', '--prefix', os.path.join(target_dir, 'npm_prefix'),
            'vue@^2.6.10',
            'rollup@^1.17.0',
            'rollup-plugin-vue@^5.0.1',
            'vue-template-compiler@^2.6.10',
        ]
        subprocess.call(' '.join(npm_cmd), shell=True)
        super().run()


class NPMInstall2(install):
    def run(self):
        super().run()


setup(
    name='django-vue-rollup',
    version='0.1.2',
    description='A django-compressor filter to compile .vue files using rollup',
    author='Laura Klünder',
    author_email='laura@codingcatgirl.de',
    url='https://github.com/codingcatgirl/django-vue-rollup',
    packages=['django_vue_rollup'],
    license='Apache License 2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
    install_requires=[
        'django-compressor>=2.3',
    ],
    package_data={
        'django_vue_rollup': ['rollup.config.js'],
    },
    cmdclass={
        'build_py': NPMInstall,
        'install': NPMInstall2,
    },
)

from setuptools import setup

setup(
    name='Calculadora',
    version='0.0.1',
    license='MIT',
    packages=['calc'],
    zip_safe=False,
    entry_points={'console_scripts': ['calc = calc:args']}
)

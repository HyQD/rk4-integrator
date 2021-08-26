from setuptools import setup, find_packages

setup(
    name="rk4-integrator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy", "scipy",],
)

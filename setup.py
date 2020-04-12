from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


def license():
    with open("LICENSE") as f:
        return f.read()


setup(
    name="dek_d_font_injector",
    description="Inject font to your Dek-D's Writer.",
    long_description=readme(),
    version="1.0",
    url="https://github.com/pannxe/Dek-D-font-injector",
    author="pannxe",
    author_email="kzt.patrix@gmail.com",
    license=license(),
    scripts=["bin/ddfi"],
    packages=["dek_d_font_injector"],
    package_dir={"dek_d_font_injector": "src/"},
)

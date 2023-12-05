from setuptools import Extension, setup

setup(
    name="foreign",
    version="1.0.0",
    description="Raises a matrix to a power.",
    author="resethikova_nata",
    author_email="n.reshetnikova@g.nsu.ru",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["foreignmodule.c"],
        ),
    ]
)

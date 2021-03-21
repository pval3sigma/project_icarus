import setuptools

setuptools.setup(
    name="Tradematik2000",
    url="https://github.com/pval3sigma/tradematik2000.git",
    description="empty for now",
    setup_requires=["pytest-runner"],
    install_requires=[
        "numpy==1.18.2",
        "pandas==1.0.3",
        "pyarrow==0.17.0",
        "pyyaml==5.3.1",
        "scikit-learn==0.22.1",
    ],
    extras_require={
        "dev": [
            "pytest-ordering==0.6",
            "pytest==5.3.5",
        ],
        "test": ["pytest-ordering==0.6", "pytest==5.3.5"],
        "spark": ["pyspark==2.4.5", "psutil==5.8.0"],
    },
    classifiers=["Programming Language :: Python :: 3.6"],
)

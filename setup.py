import setuptools

setuptools.setup(
    name="streamlit-tensorboard",
    version="0.0.2",
    author="Snehan Kekre",
    author_email="snehan@streamlit.io",
    description="Streamlit component for TensorBoard",
    long_description="Streamlit component for TensorBoard",
    long_description_content_type="text/plain",
    url="https://github.com/snehankekre/streamlit-tensorboard",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit >= 0.63", "tensorboard >= 2.5.0"],
)
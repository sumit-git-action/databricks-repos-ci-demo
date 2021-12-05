from setuptools import find_packages, setup
from de_ml_cicd_git_action import __version__
#
setup(
    name="databricks_repos_ci_code",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks CICD Demo for DE and Promoting models to Production",
    author="sumit.prakash@databricks.com",
)
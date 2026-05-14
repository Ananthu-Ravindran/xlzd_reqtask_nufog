from setuptools import setup, find_packages
setup(
        name="fogtask",
        version = "0.3",
        packages=["fogtask", "detector_parameters"],
        package_dir = {"fogtask":"fogtask", "detector_parameters": "detector_parameters"},
        include_package_data=True,
        package_data={'detector_parameters': ['*.yaml']},
        author="Maike Doerenkamp,Robert James,Knut Morå",
        author_email="fysikk@dundasmora.no",
        description="Code for XLZD requirements task force",
        )

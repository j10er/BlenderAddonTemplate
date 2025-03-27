# Template Repository to create a new blank Blender Add-on/Extension
## Structure
- Folder "addonname" contains the addon itself, all other files in the top repository are only for development purposes
  - dev.py: Contains management functions for running the tests and building the application
  - run_tests.py: Will be executed from within Blender to run all tests with pytest
  - tests/: Contains the tests
  - development_requirements.txt: Contains all python packages that should be installed in the local python virtual environment
  - blender/: contains blender executables responsible for building and testing the add-on, automatically managed by dev.py
  - .github/: Contains github action configurations to automatically test the add-on on push
## Setup
- Rename all occurrences of "addonname" and "addonid" to the name and id of your add-on
  - Folder "addonname"
  - in addonname/blender_manifest.toml
  - in dev.py rename the variables
  - in the tests, use your addonid to access your add-on as a python module

# Blender Add-on Template

A modern template repository for creating Blender add-ons/extensions with automated testing and development tools.

## Project Structure

```
├── AddonName/                    # Main add-on directory
├── dev.py                        # Development management script
├── run_tests.py                  # Test runner for Blender
├── tests/                        # Test files
├── development_requirements.txt   # Python dependencies
├── blender/                      # Blender executables (auto-managed)
└── .github/                      # CI/CD workflows
```

The `AddonName` folder contains your actual add-on - all other files are development tools.

## Quick Setup

1. **Rename the `AddonName` and `addonid`  to your own name:**
   - Folder: `AddonName`
   - Update the variables in `AddonName/blender_manifest.toml`
   - Update the variables in `dev.py`
   - Update the `AddonName.zip` line in `.gitignore`
   - Update test imports to use your addon ID


2. **`dev.py` command line options**
   - ```bash python dev.py test``` runs all tests in the ./tests folder
   - ```bash python dev.py build``` build the add-on to a zip

## Features

- **Automated Testing** - Run tests within Blender using pytest
- **CI/CD Ready** - GitHub Actions for automatic testing
- **Build Management** - Automated Blender executable management
- **Development Tools** - Integrated development workflow

---
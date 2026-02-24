# Generators

This directory contains the Python scripts used to generate the visualizations.


## Developing

Each script should define a function called `make_viz` which does the following:

- Creates a set of visualizations
- Export them as PNGs into the output directory (`output_folder/` in the project root)

To test the function, just import it into `main.py` an call the function in `main`.

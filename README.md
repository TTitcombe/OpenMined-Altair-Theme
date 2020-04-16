# OpenMined Altair Theme
**Unofficial** [OpenMined] theme for [Altair],
following the [OpenMined] brand guide.

See [here][altair-custom-theme] for more information on defining custom themes for [Altair].

## How to use
1. Clone this repo to create a local copy of the theme.
2. Download the `PT Mono` and `Overpass` fonts
3. In your notebook / code import the `openmined` function from [openmined_theme.py](./openmined_theme.py)
    - This function returns the theme spec
4. Register the spec function as an [Altair] theme
    ```python
    alt.themes.register("openmined", openmined)
    ```
5. Enable the theme
    ```python
    alt.themes.enable("openmined")
    ```
6. Use [Altair] as normal

## Example usage
See the [notebooks](./examples) for example usage.
This repo provides a conda environment with all required packages.
With conda installed, run `conda env create -f environment.yml`
to create the conda environment,
called `om-altair-dev`.

## License
This repo is released with an Apache 2 license.
See the [license](./LICENSE) for more information.

[Altair]: https://github.com/altair-viz/altair
[OpenMined]: https://openmined.org

[altair-custom-theme]: https://altair-viz.github.io/user_guide/configuration.html#defining-a-custom-theme

from typing import Dict

# Quadrant colours
northwest_orange_dark = "#ED986C"
northwest_orange_light = "#F1BF7A"
northwest_orange_gradient = ["#ED986C", "#F1BF7A"]  # TODO interpolate between these colours

northeast_green_dark = "#5CB5A4"
northeast_green_light = "#9BCC9A"
northeast_green_gradient = []  # TODO

southeast_blue_dark = "#767EA1"
southeast_blue_light = "#62A4AE"
southeast_blue_gradient = []  # TODO

southwest_red_dark = "#C3707C"
southwest_red_light = "#EF996B"
southwest_red_gradient = []  # TODO

# Grayscale colours
light_gray = "#969696"
gray = "#808080"
dark_gray = "#323232"

# Fonts
headline_font = "PT Mono"
body_font = "Overpass"


def openmined() -> Dict:
    """
    OpenMined colour scheme for Altair

    To use, register and enable the theme:
        import altair
        altair.themes.register("openmined", openmined)
        altair.themes.enable("openmined")

    Returns
    -------
    dict
        Altair colour scheme spec
    """
    return {
        "config": {
            "background": light_gray,
            "title": {
                "anchor": "start",
                "color": dark_gray,
                "font": headline_font,
                "fontSize": 22,
                "fontWeight": "normal",
            },
            "legend": {
                "labelFont": body_font,
                "labelFontSize": 13,
                "symbolType": "circle",
                "titleFont": headline_font,
                "titleFontSize": 11,
            },
            "axis": {
                "domain": False,
                "grid": False,
                "labelColor": dark_gray,
                "labelPadding": 4,
                "tickColor": dark_gray,
                "tickSize": 5.67,
                "titleFontSize": 16,
                "titleFontWeight": "normal",
            },
            # Colours
            "range": {
                "category": [
                    northwest_orange_dark,
                    northeast_green_dark,
                    southeast_blue_dark,
                    southwest_red_dark,
                ],
                "diverging": [],  # TODO use northwest gradient
                "heatmap": [],  # TODO
            },
            # Marks
            "arc": {"fill": northwest_orange_dark},
            "area": {"fill": northwest_orange_dark},
            "point": {"filled": True, "shape": "circle"},
            "line": {"stroke": northwest_orange_dark, "strokeWidth": 2,},
            "bar": {"binSpacing": 2, "fill": northwest_orange_dark, "stroke": None,},
            # TODO rect
        }
    }

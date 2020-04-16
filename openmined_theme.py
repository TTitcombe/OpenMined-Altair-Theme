from typing import Dict

# Quadrant colours
northwest_orange_dark = "#ED986C"
northwest_orange_light = "#F1BF7A"
northwest_orange_gradient = [
    "#F1BF7A",
    "#ED986C",
]

northeast_green_dark = "#5CB5A4"
northeast_green_light = "#9BCC9A"
northeast_green_gradient = [
    "#5CB5A4",
    "#9BCC9A",
]

southeast_blue_dark = "#767EA1"
southeast_blue_light = "#62A4AE"
southeast_blue_gradient = [
    "#62A4AE",
    "#767EA1",
]

southwest_red_dark = "#C3707C"
southwest_red_light = "#EF996B"
southwest_red_gradient = [
    "#C3707C",
    "#EF996B",
]

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
            "background": "#FFFFFF",
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
                    northwest_orange_light,
                    northeast_green_light,
                    southeast_blue_light,
                    southwest_red_light,
                ],
                "heatmap": northwest_orange_gradient,
                "ordinal": northwest_orange_gradient,
            },
            # Marks
            "arc": {"fill": northwest_orange_dark},
            "area": {"fill": northwest_orange_dark},
            "point": {
                "fill": northwest_orange_dark,  # Use dark orange as default colour
                "filled": True,
                "shape": "M 0 -1 l 0.179 0.821 L 1 0 l -0.821 0.179 L 0 1 l -0.179 -0.821 L -1 0 l 0.821 -0.179 Z",
                "size": 250,
            },
            "line": {"stroke": northwest_orange_dark, "strokeWidth": 2,},
            "bar": {"binSpacing": 2, "fill": northwest_orange_dark, "stroke": None,},
            # TODO rect
        }
    }

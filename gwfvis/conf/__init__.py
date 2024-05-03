import base64
import json
from dataclasses import dataclass


@dataclass
class PluginNames:
    SQLITE_LOCAL_DATA_PROVIDER = "gwf-default.sqlite-local-data-provider"
    GWFVISDB_DATA_PROVIDER = "gwf-default.gwfvisdb-data-provider"
    TEST_DATA_FETCHER = "gwf-default.test-data-fetcher"
    TILE_LAYER = "gwf-default.tile-layer"
    GEOJSON_LAYER = "gwf-default.geojson-layer"
    CONTOUR_LAYER = "gwf-default.contour-layer"
    VECTOR_GRID_LAYER = "gwf-default.vector-grid-layer"
    LEGEND = "gwf-default.legend"
    DATA_CONTROL = "gwf-default.data-control"
    METADATA = "gwf-default.metadata"
    MARKDOWN = "gwf-default.markdown"
    LOCATION_PIN = "gwf-default.location-pins"
    LINE_CHART = "gwf-default.line-chart"


_DEFAULT_PLUGIN_PATH = "https://vga-team.github.io/gwf-vis_default-plugins"
_RECOMMENDED_PLUGIN_IMPORTS = {
    PluginNames.SQLITE_LOCAL_DATA_PROVIDER: f"{_DEFAULT_PLUGIN_PATH}/sqlite-local-data-provider.plugin.js",
    PluginNames.GWFVISDB_DATA_PROVIDER: f"{_DEFAULT_PLUGIN_PATH}/gwfvisdb-data-provider.plugin.js",
    PluginNames.TEST_DATA_FETCHER: f"{_DEFAULT_PLUGIN_PATH}/test-data-fetcher.plugin.js",
    PluginNames.TILE_LAYER: f"{_DEFAULT_PLUGIN_PATH}/tile-layer.plugin.js",
    PluginNames.GEOJSON_LAYER: f"{_DEFAULT_PLUGIN_PATH}/geojson-layer.plugin.js",
    PluginNames.CONTOUR_LAYER: f"{_DEFAULT_PLUGIN_PATH}/contour-layer.plugin.js",
    PluginNames.VECTOR_GRID_LAYER: f"{_DEFAULT_PLUGIN_PATH}/vector-grid-layer.plugin.js",
    PluginNames.LEGEND: f"{_DEFAULT_PLUGIN_PATH}/legend.plugin.js",
    PluginNames.DATA_CONTROL: f"{_DEFAULT_PLUGIN_PATH}/data-control.plugin.js",
    PluginNames.METADATA: f"{_DEFAULT_PLUGIN_PATH}/metadata.plugin.js",
    PluginNames.MARKDOWN: f"{_DEFAULT_PLUGIN_PATH}/markdown.plugin.js",
    PluginNames.LOCATION_PIN: f"{_DEFAULT_PLUGIN_PATH}/location-pins.plugin.js",
    PluginNames.LINE_CHART: f"{_DEFAULT_PLUGIN_PATH}/line-chart.plugin.js",
}
_DEFAULT_FAVICON_DATA_URL = "data:image/png;base64,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"


def create_config(no_basemap=False):
    return {
        "imports": _RECOMMENDED_PLUGIN_IMPORTS,
        "pageTitle": "GWF-VIS",
        "favicon": _DEFAULT_FAVICON_DATA_URL,
        "plugins": (
            [
                {
                    "import": "gwf-default.tile-layer",
                    "container": "",
                    "props": {
                        "displayName": "World_Imagery",
                        "active": True,
                        "urlTemplate": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                        "options": {
                            "attribution": "Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community"
                        },
                    },
                }
            ]
            if no_basemap == False
            else []
        ),
    }

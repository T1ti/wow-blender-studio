import bpy
import time

from ..utils.misc import load_game_data
from .wmo_scene import BlenderWMOScene
from ..pywowlib import CLIENT_VERSION, WoWVersions
from ..pywowlib.wmo_file import WMOFile
from ..ui import get_addon_prefs
from .ui.handlers import DepsgraphLock


def import_wmo_to_blender_scene(filepath, import_doodads, import_lights, import_fogs, group_objects):
    """ Read and import WoW WMO object to Blender scene"""

    start_time = time.time()

    print("\nImporting WMO")

    addon_prefs = get_addon_prefs()
    game_data = load_game_data()

    with DepsgraphLock():
        wmo = WMOFile(CLIENT_VERSION, filepath=filepath)
        wmo.read()
        wmo_scene = BlenderWMOScene(wmo=wmo, prefs=addon_prefs)

        # extract textures to cache folder
        game_data.extract_textures_as_png(addon_prefs.cache_dir_path, wmo.motx.get_all_strings())

        # load all WMO components
        wmo_scene.load_materials()
        wmo_scene.load_lights()
        wmo_scene.load_properties()
        wmo_scene.load_fogs()
        wmo_scene.load_groups()
        wmo_scene.load_portals()
        wmo_scene.load_doodads()

    # update visibility
    bpy.context.scene.wow_visibility = bpy.context.scene.wow_visibility

    print("\nDone importing WMO. \nTotal import time: ",
          time.strftime("%M minutes %S seconds.\a", time.gmtime(time.time() - start_time)))


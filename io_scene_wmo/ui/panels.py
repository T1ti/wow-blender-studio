import bpy
from .. import ui_icons


class WBS_PT_wow_scene(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"
    bl_label = "WoW Scene"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(context.scene.wow_scene, 'version')
        col.prop(context.scene.wow_scene, 'type')
        col.prop(context.scene.wow_scene, 'game_path')

    @classmethod
    def poll(cls, context):
        return context.scene is not None


class WowScenePropertyGroup(bpy.types.PropertyGroup):

    version:  bpy.props.EnumProperty(
        name='Client version',
        items=[('264', 'WotLK', "", ui_icons['WOTLK'], 0),
               ('274', 'Legion', "", ui_icons['LEGION'], 1)],
        default='274'
    )

    type:  bpy.props.EnumProperty(
        name='Scene type',
        description='Sets up the UI to work with a specific WoW game format',
        items=[
            ('M2', 'M2', 'M2 model',  ui_icons['WOW_STUDIO_M2'], 0),
            ('WMO', 'WMO', 'World Map Object (WMO)', ui_icons['WOW_STUDIO_WMO'], 1)
            ]
    )

    game_path:  bpy.props.StringProperty(
        name='Game path',
        description='A path to the model in WoW filesystem.'
    )


def register_wow_scene_properties():
    bpy.types.Scene.wow_scene = bpy.props.PointerProperty(type=WowScenePropertyGroup)


def unregister_wow_scene_properties():
    del bpy.types.Scene.wow_scene


def render_top_bar(self, context):
    if context.region.alignment == 'TOP':
        return

    layout = self.layout
    row = layout.row(align=True)
    row.label(text='WoW Scene:')
    row.prop(context.scene.wow_scene, 'version', text='')
    row.prop(context.scene.wow_scene, 'type', text='')
    row.operator("scene.reload_wow_filesystem", text="", icon_value=ui_icons['WOW_STUDIO_RELOAD'])


def render_viewport_toggles_left(self, context):
    layout = self.layout
    row = layout.row(align=True)
    row.operator("wow.toggle_image_alpha", icon='NODE_TEXTURE', text='')


menu_import_wmo = lambda self, ctx: self.layout.operator("import_mesh.wmo", text="WoW WMO (.wmo)")
menu_export_wmo = lambda self, ctx: self.layout.operator("export_mesh.wmo", text="WoW WMO (.wmo)")
menu_import_m2 = lambda self, ctx: self.layout.operator("import_mesh.m2", text="WoW M2 (.m2)")
menu_export_m2 = lambda self, ctx: self.layout.operator("export_mesh.m2", text="WoW M2 (.m2)")


def register():
    register_wow_scene_properties()
    bpy.types.TOPBAR_HT_upper_bar.append(render_top_bar)
    bpy.types.VIEW3D_HT_header.append(render_viewport_toggles_left)
    bpy.types.TOPBAR_MT_file_import.append(menu_import_wmo)
    bpy.types.TOPBAR_MT_file_import.append(menu_import_m2)
    bpy.types.TOPBAR_MT_file_export.append(menu_export_wmo)
    bpy.types.TOPBAR_MT_file_export.append(menu_export_m2)


def unregister():
    unregister_wow_scene_properties()
    bpy.types.TOPBAR_MT_file_import.remove(menu_import_wmo)
    bpy.types.TOPBAR_MT_file_import.remove(menu_import_m2)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export_wmo)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export_m2)
    bpy.types.TOPBAR_HT_upper_bar.remove(render_top_bar)
    bpy.types.VIEW3D_HT_header.append(render_viewport_toggles_left)

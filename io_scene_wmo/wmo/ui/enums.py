from ... import ui_icons

__reload_order_index__ = -1

shader_enum = [
    ('0', "Diffuse", ""), ('1', "Specular", ""), ('2', "Metal", ""),
    ('3', "Env", ""), ('4', "Opaque", ""), ('5', "EnvMetal", ""),
    ('6', "TwoLayerDiffuse", ""), ('7', "TwoLayerEnvMetal", ""), ('8', "TwoLayerTerrain", ""),
    ('9', "DiffuseEmissive", ""), ('10', "Tangent", ""), ('11', "MaskedEnvMetal", ""),
    ('12', "EnvMetalEmissive", ""), ('13', "TwoLayerDiffuseOpaque", ""), ('14', "TwoLayerDiffuseEmissive", "")
]

terrain_type_enum = [
    ('0', "Dirt", ""), ('1', "Metallic", ""), ('2', "Stone", ""),
    ('3', "Snow", ""), ('4', "Wood", ""), ('5', "Grass", ""),
    ('6', "Leaves", ""), ('7', "Sand", ""), ('8', "Soggy", ""),
    ('9', "Dusty Grass", ""), ('10', "None", ""), ('11', "Water", ""),
    ('12', "Unknown", ""),('13', "Unknown", ""),
]

blending_enum = [
    ('0', "Blend_Opaque", ""), ('1', "Blend_AlphaKey", ""), ('2', "Blend_Alpha", ""),
    ('3', "Blend_Add", ""), ('4', "Blend_Mod", ""), ('5', "Blend_Mod2x", ""),
    ('6', "Blend_ModAdd", ""), ('7', "Blend_InvSrcAlphaAdd", ""), ('8', "Blend_InvSrcAlphaOpaque", ""),
    ('9', "Blend_SrcAlphaOpaque", ""), ('10', "Blend_NoAlphaAdd", ""), ('11', "Blend_ConstantAlpha", "")
]

material_flag_enum = [
    ("1", "Unlit", "Disable lighting", 'SNAP_VOLUME', 0x1),
    ("2", "Unfogged", "Disable fog", ui_icons['MAT_UNFOGGED'], 0x2),
    ("4", "Two-sided", "Render from both sides", 'MOD_UVPROJECT', 0x4),
    ("8", "Exterior light", "Ignore local WMO lighting, use world lighting instead", ui_icons['MAT_EXT_LIGHT'], 0x8),
    ("16", "Night Glow", "Used for windows to glow at nighttime", ui_icons['MAT_NIGHT_GLOW'], 0x10),
    ("32", "Window", "Unknown, used for windows", ui_icons['MAT_WINDOW'], 0x20),
    ("64", "Clamp_S", "Force texture to use clamp _s adressing", 'SPACE3', 0x40),
    ("128", "Clamp_T", "Force texture to use clamp _t adressing", 'SPACE2', 0x80)
]

group_flag_enum = [
    ('0', "Vertex color", "Check if you need vertex color in this group", 'COLOR', 0x1),
    ('1', "No local lighting", "Use world-defined lighting in a group", 'LAMP_HEMI', 0x2),
    ('2', "Always draw", "Always draw the model. Disable portal-based geometry culling", 'BBOX', 0x4),
    ('3', "Mounts allowed", "Allow mounts in this indoor group", ui_icons['WOW_STUDIO_MOUNT'], 0x8),
    ('4', "Use Skybox", "Display WMO skybox in this indoor group", 'SURFACE_NSPHERE', 0x10)
]

place_type_enum = [('8', "Outdoor", "", 'OBJECT_DATA', 0), ('8192', "Indoor", "", 'MOD_SUBSURF', 1)]

liquid_type_enum = [
    ('0', "No liquid", ""), ('1', "Water", ""), ('2', "Ocean", ""),
    ('3', "Magma", ""), ('4', "Slime", ""), ('5', "Slow Water", ""),
    ('6', "Slow Ocean", ""), ('7', "Slow Magma", ""), ('8', "Slow Slime", ""),
    ('9', "Fast Water", ""), ('10', "Fast Ocean", ""), ('11', "Fast Magma", ""),
    ('12', "Fast Slime", ""), ('13', "WMO Water", ""), ('14', "WMO Ocean", ""),
    ('15', "Green Lava", ""), ('17', "WMO Water - Interior", ""), ('19', "WMO Magma", ""),
    ('20', "WMO Slime", ""), ('21', "Naxxramas - Slime", ""), ('41', "Coilfang Raid - Water", ""),
    ('61', "Hyjal Past - Water", ""), ('81', "Lake Wintergrasp - Water", ""), ('100', "Basic Procedural Water", ""),
    ('121', "CoA Black - Magma", ""), ('141', "Chamber Magma", ""), ('181', "Orange Slime", "")
]

portal_dir_alg_enum = [
    ("0", "Auto", "", 'MONKEY', 0),
    ("1", "Positive", "", 'ADD', 1),
    ("2", "Negative", "", 'REMOVE', 2)
]

root_flags_enum = [
    ("0", "No Auto Attenuation", "Do not attenuate light on vertices based on distance from portal", 'MOD_MIRROR', 0x1),
    ("1", "Do Not Use Lightmap", "", 'LAMP_SUN', 0x2),
    ("2", "Unified rendering", "Use ambient lighting inside indoor groups", 'PMARKER_ACT', 0x4)
]

light_type_enum = [
    ('0', "Omni", ""), ('1', "Spot", ""),
    ('2', "Direct", ""), ('3', "Ambient", "")
]

import bpy


class VIEW3D_PT_SidePanel(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "addon-name"
    bl_label = "addon-name"

    def draw(self, context):

        layout = self.layout
        layout.operator("object.import_assets")

bl_info = {
    "name": "Hello World!",
    "author": "gmcky139",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Hello World Tab",
    "description": "Test",
    "support": "COMMUNITY",
    "warning": "",
    "doc_url": "https://github.com/gmcky139/blender-addon-devcontainer",
    "tracker_url": "https://github.com/gmcky139/blender-addon-devcontainer/issues",
    "category": "",
}

import bpy

class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Hello World Panel"
    bl_idname = "VIEW3D_PT_hello_world"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Hello World'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello World!")

def register():
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    register()
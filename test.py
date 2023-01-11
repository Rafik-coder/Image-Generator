# from kivy.lang import Builder
# from kivy.uix.scrollview import ScrollView
# from kivymd.app import MDApp
# from kivymd.effects.fadingedge.fadingedge import FadingEdgeEffect
# from kivymd.uix.list import OneLineListItem
# KV = '''
# MDScreen:
#     FadeScrollView:
#         fade_height: self.height / 5
#         fade_color: root.md_bg_color
        
#         MDList:
#             id: container
#     '''

# class FadeScrollView(FadingEdgeEffect, ScrollView):
#     pass
# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):
#         for i in range(20):
#             self.root.ids.container.add_widget(
#             OneLineListItem(text=f"Single-line item {i}")
#         )

# Test().run()


# from kivy.animation import Animation
# from kivy.lang import Builder
# from kivy.uix.behaviors import ButtonBehavior
# from kivymd.app import MDApp
# from kivymd.uix.behaviors import RotateBehavior
# from kivymd.uix.boxlayout import MDBoxLayout

# KV = '''
# MDScreen:
#     RotateBox:
#         size_hint: .5, .5
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.change_rotate(self)
#         md_bg_color: "red"
# '''

# class RotateBox(ButtonBehavior, RotateBehavior, MDBoxLayout):
#     pass


# class Test(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def change_rotate(self, instance_button: RotateBox) -> None:
#         Animation(rotate_value_angle=360, d=30).start(instance_button)

# Test().run()

# from . import images

# print(images)

from pathlib import Path
import os


folder_dir = "images"
folders = [d for d in os.listdir(folder_dir) if os.path.isdir(os.path.join(folder_dir, d))]
# for file in folders:
#     print(file)

for folder in folders:
    # print(folder)
    files = [f for f in os.listdir("images/" + str(folder)) if os.path.isfile(os.path.join("images/" + str(folder), f))]

    for file in files:
        print(file)

# files_dir = f"images{}"



# for file in files:
#     print(file)

# with open("images", "r") as im:
#     print(im.read())
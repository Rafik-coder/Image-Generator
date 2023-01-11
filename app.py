from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.effects.fadingedge.fadingedge import FadingEdgeEffect
from kivymd.uix.list import OneLineListItem
from main import send
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
import os
from kivymd.uix.imagelist.imagelist import MDSmartTile, SmartTileImage



# class LoadImage(AsyncImage):
#     Loader.loading_image = "loader.gif"


class Generated(FadingEdgeEffect, ScrollView):
    pass


class ImageMaker(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("app.kv")
        self.show_imgs = self.screen.ids.generated

        self.imgs = []

        # self.show_imgs.add_widget(
        #     MDLabel(text="Hey")
        # )

        self.dialog = MDDialog(
            type="custom",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=self.close,
                ),
            ]
        )

        

    def view_img(self, *args):
        print("self.show_imgs.source")

    def generate(self, *args):
        promt = self.screen.ids.promt.text

        # try:
            # print(promt)
        request = send(promt)
        print(request)

        if request == "failed" or request == None:
            self.dialog.text = "[color=#ff0000]Please Check Your Connection and Try Again[/color]"
            self.dialog.title = "Connection Error"
            self.dialog.buttons=MDFlatButton(text="RETRY", on_release=self.generate,)
            
            self.dialog.open()


            # self.show_imgs.ids.generated_imgs.add_widget(
            #     MDIconButton(
            #         icon="download",
            #         theme_icon_color="Custom",
            #         color=[1, 1, 1, 1],
            #         post_hint={"center_x": .5, "center_y": .5},
            #         halign="center"
            #     )
            # )

        else:    
            folder_dir = "images/"
            folders = [d for d in os.listdir(folder_dir) if os.path.isdir(os.path.join(folder_dir, d))]
            
            # imgs = self.screen.ids.imgs_generated

            for folder in folders:
                # print(folder)
                files = [f for f in os.listdir(folder_dir + str(folder)) if os.path.isfile(os.path.join("images/" + str(folder), f))]

                for file in files:
                    print(folder + str(file))
                    # imgs.source = f"images/{folder}/{str(file)}"
                    # self.imgs

                    self.show_imgs.add_widget(
                        SmartTileImage(
                            id="generated_imgs",
                            radius=[24],
                            # box_radius=[0, 0, 24, 24],
                            # lines=2,
                            source= f"images/{folder}/{str(file)}",
                            pos_hint={"center_x": .5, "center_y": .5},
                            size_hint= [None, None],
                            size= ["200dp", "200dp"],
                            on_release=self.view_img,
                        )
                    )

    def note(self):
        self.dialog.text = """
        Please Input clear and precise 
        description of the image you want, Your Input 
        determins the images that should be generated for you.

        """
        self.dialog.open()

    def close(self, *args):
        self.dialog.dismiss()

    def build(self):
        return self.screen


if __name__=="__main__":
    app = ImageMaker()
    app.run()

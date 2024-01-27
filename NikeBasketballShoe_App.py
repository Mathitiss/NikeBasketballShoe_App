import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

kivy.require('1.9.0')

Builder.load_string("""
<Welcome>:
    canvas:
        Color:
            rgba: 0, 0, 0, 0
        Rectangle:
            size: self.size
        
    Image:
        source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Nike_small_white.png'
        pos: 0, 200

    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Button_store_1.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Button_store_2.png'
        size_hint: None, None
        size: 285, 60
        center_x: root.width / 2
        y: 110
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.transition.duration = 3
            root.manager.current = 'Athletes'

    Image:
        source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\NBA_logo_small.png'
        size_hint: None, None
        x: 290
        y: -10
            
<Athletes>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
            
    Label:
        markup: True
        text: 'ATHLETES'
        font_size: 48
        color: 0, 0, 0
        font_name: r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Black.otf'
        pos: 0, 285

    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\LBJ BUTTON 1.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\LBJ BUTTON 2.png'
        size_hint: None, None
        size: 320, 140
        center_x: root.width / 2
        y: 430
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.transition.duration = 3
            root.manager.current = 'Lebron'
            
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\KD BUTTON 1.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\KD BUTTON 2.png'
        size_hint: None, None
        size: 320, 140
        center_x: root.width / 2
        y: 250
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.transition.duration = 3
            root.manager.current = 'Kevin'

    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\ANTE BUTTON 1.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\ANTE BUTTON 2.png'
        size_hint: None, None
        size: 320, 140
        center_x: root.width / 2
        y: 70
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.transition.duration = 3
            root.manager.current = 'Ante'
            
    Image:
        source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\COLLAB logos.png'
        size_hint: None, None
        x: 138
        y: -15
        
<Lebron>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

    Carousel:
        direction: 'bottom'
        
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\BronScr.png'
            size_hint: None, None
            size: 375, 645
            
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\BronScr2.png'
            size_hint: None, None
            size: 375, 645           
                      
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\BronScr3.png'
            size_hint: None, None
            size: 375, 645

            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron 20 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron 20 Button.png'
                size_hint: None, None
                size: 375, 179
                center_x: root.width / 2
                y: 400
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_20'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron NXXT Gen Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron NXXT Gen Button.png'
                size_hint: None, None
                size: 375, 201
                center_x: root.width / 2
                y: 70
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_NXXT_Gen'
                    
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\BronScr4.png'
            size_hint: None, None
            size: 375, 645

            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 7 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 7 Button.png'
                size_hint: None, None
                size: 375, 185
                center_x: root.width / 2
                y: 400
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_Witness_7'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 7 Team Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 7 Team Button.png'
                size_hint: None, None
                size: 375, 190
                center_x: root.width / 2
                y: 70
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_Witness_7_Team'
                    
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\BronScr5.png'
            size_hint: None, None
            size: 375, 645

            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 6 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 6 Button.png'
                size_hint: None, None
                size: 375, 205
                center_x: root.width / 2
                y: 400
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_Witness_6'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 6 Team Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\LBJ\\LeBron Witness 6 Team Button.png'
                size_hint: None, None
                size: 375, 212
                center_x: root.width / 2
                y: 70
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'LeBron_Witness_6_Team'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                size_hint: None, None
                size: 25, 25
                x: 340
                y: 10
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Athletes'
                                    
<Kevin>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

    Carousel:
        direction: 'bottom'
        
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\KDscr.png'
            size_hint: None, None
            size: 375, 645
            
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\KDscr 2.png'
            size_hint: None, None
            size: 375, 645            
                 
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\KDscr 3.png'
            size_hint: None, None
            size: 375, 645
            
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\KD 15 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\KD 15 Button.png'
                size_hint: None, None
                size: 315, 163
                center_x: root.width / 2
                y: 480
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'KD_15'
                      
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\Trey 5 X Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\Trey 5 X Button.png'
                size_hint: None, None
                size: 315, 160
                center_x: root.width / 2
                y: 260
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Trey_5_X'
            
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\Trey 15 IX.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\KD\\Trey 15 IX.png'
                size_hint: None, None
                size: 315, 144
                center_x: root.width / 2
                y: 45
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Trey_15_IX'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                size_hint: None, None
                size: 25, 25
                x: 340
                y: 10
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Athletes'            
            
<Ante>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

    Carousel:
        direction: 'bottom'
        
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\AnteScr.png'
            size_hint: None, None
            size: 375, 645
            pos: self.pos
            
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\AnteScr2.png'
            size_hint: None, None
            size: 375, 645
                      
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\AnteScr3.png'
            size_hint: None, None
            size: 375, 645

            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Immortality 2 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Immortality 2 Button.png'
                size_hint: None, None
                size: 375, 190
                center_x: root.width / 2
                y: 400
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Immortality_2'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Immortality Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Immortality Button.png'
                size_hint: None, None
                size: 375, 208
                center_x: root.width / 2
                y: 70
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Immortality'
            
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\AnteScr4.png'
            size_hint: None, None
            size: 375, 645            
            
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Freak 4 Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Freak 4 Button.png'
                size_hint: None, None
                size: 375, 189
                center_x: root.width / 2
                y: 400
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Freak_4'
                    
            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Freak 4 Team Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Shoe\\ANTE\\Freak 4 Team Button.png'
                size_hint: None, None
                size: 375, 201
                center_x: root.width / 2
                y: 70
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Freak_4_Team'                

            Button:
                background_normal: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                background_down: r'C:\\Users\\egorm\\PycharmProjects\\NikeBasketballShoe\\images\\Leave_Button.png'
                size_hint: None, None
                size: 25, 25
                x: 340
                y: 10
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'Athletes'
<KD_15>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
            


<Trey_5_X>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<Trey_15_IX>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
            
<Immortality_2>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<Immortality>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<Freak_4>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size 
            
<Freak_4_Team>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size   
            
<LeBron_NXXT_Gen>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<LeBron_20>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<LeBron_Witness_7>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
            
<LeBron_Witness_7_Team>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<LeBron_Witness_6>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size

<LeBron_Witness_6_Team>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size                                        
""")

screen_manager = ScreenManager()

class Welcome(Screen):
    def __init__(self, **kwargs):
        super(Welcome, self).__init__(**kwargs)

        # Создаем Label
        label1 = Label(text='WELCOME', font_size=40, pos=(0, 70), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        label2 = Label(text='WELCOME', font_size=40, pos=(0, 38), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')
        label3 = Label(text='WELCOME', font_size=40, pos=(0, 6), font_name=r'C:\\Users\\egorm\\PycharmProjects\\Cold_Shower\\Font\\Inter-Thin.otf')

        # Добавляем Label
        self.add_widget(label1)
        self.add_widget(label2)
        self.add_widget(label3)

        # Скрываем Label
        label1.opacity = 0
        label2.opacity = 0
        label3.opacity = 0

        # Создаем анимацию
        anim1 = Animation(opacity=1, duration=3)
        anim2 = Animation(opacity=1, duration=3)
        anim3 = Animation(opacity=1, duration=3)

        # Запускаем анимацию
        anim1.start(label1)
        anim1.bind(on_complete=lambda *x: anim2.start(label2))
        anim2.bind(on_complete=lambda *x: anim3.start(label3))

class Athletes(Screen):
    pass
class Lebron(Screen):
    pass
class Kevin(Screen):
    pass
class Ante(Screen):
    pass


class KD_15(Screen):
    pass
class Trey_5_X(Screen):
    pass
class Trey_15_IX(Screen):
    pass


class Immortality_2(Screen):
    pass
class Immortality(Screen):
    pass
class Freak_4(Screen):
    pass
class Freak_4_Team(Screen):
    pass


class LeBron_NXXT_Gen(Screen):
    pass
class LeBron_20(Screen):
    pass
class LeBron_Witness_7(Screen):
    pass
class LeBron_Witness_7_Team(Screen):
    pass
class LeBron_Witness_6(Screen):
    pass
class LeBron_Witness_6_Team(Screen):
    pass

screen_manager.add_widget(Welcome(name="Welcome"))
screen_manager.add_widget(Athletes(name="Athletes"))
screen_manager.add_widget(Lebron(name="Lebron"))
screen_manager.add_widget(Kevin(name="Kevin"))
screen_manager.add_widget(Ante(name="Ante"))

screen_manager.add_widget(KD_15(name="KD_15"))
screen_manager.add_widget(Trey_5_X(name="Trey_5_X"))
screen_manager.add_widget(Trey_15_IX(name="Trey_15_IX"))

screen_manager.add_widget(Immortality_2(name="Immortality_2"))
screen_manager.add_widget(Immortality(name="Immortality"))
screen_manager.add_widget(Freak_4(name="Freak_4"))
screen_manager.add_widget(Freak_4_Team(name="Freak_4_Team"))

screen_manager.add_widget(LeBron_NXXT_Gen(name="LeBron_NXXT_Gen"))
screen_manager.add_widget(LeBron_20(name="LeBron_20"))
screen_manager.add_widget(LeBron_Witness_7(name="LeBron_Witness_7"))
screen_manager.add_widget(LeBron_Witness_7_Team(name="LeBron_Witness_7_Team"))
screen_manager.add_widget(LeBron_Witness_6(name="LeBron_Witness_6"))
screen_manager.add_widget(LeBron_Witness_6_Team(name="LeBron_Witness_6_Team"))

class NikeShoe(App):
    def build(self):
        Window.size = (375, 645)
        screen_manager.current = 'Welcome'
        return screen_manager

NikeShoe().run()
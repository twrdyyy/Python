import pyglet
from pyglet.window import key, mouse

if __name__ == '__main__':

    window = pyglet.window.Window()

    @window.event
    def on_key_press(symbol, modifiers):
        print('A key was pressed')
        if symbol == key.A:
            print("'A' was pressed")
        elif symbol == key.LEFT:
            print("The left arrow was pressed")
        elif symbol == key.ENTER:
            print("ENTER was pressed")

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed')


    #window.push_handlers(pyglet.window.event.WindowEventLogger())


    @window.event
    def on_draw():
        window.clear()

    pyglet.app.run()
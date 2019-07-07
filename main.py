import math
import sys

import sdl2
import sdl2.ext

from curves_drawer import CurvesDrawer

DEFAULT_WINDOW_SIZE = (420, 420)

COLOR_WHITE = sdl2.ext.Color(r=255, g=255, b=255, a=255)

STEP = 0.001
CISSOID_PARAMS = {'a': 100, 't_interval': (-5, 5)}
FOLIUM_PARAMS = {'a': 100, 't_intervals': [(-0.5, 20), (-20, -2)]}
CARDIOID_PARAMS = {'a': 90, 't_interval': (0, 2 * math.pi)}
SNAIL_PARAMS = {'a': 140, 'l': 50, 't_interval': (0, 2 * math.pi)}
EPICYCLOID_PARAMS = {'a': 30, 'b': 90, 't_interval': (0, 2 * math.pi)}
SPIRAL_PARAMS = {'a': 0.1, 'phi_interval': (0, 6 * math.pi)}


def main():
    selected_curve = sys.argv[1]

    sdl2.ext.init()
    window = sdl2.ext.Window(
        title='Higher-Order Curves',
        size=DEFAULT_WINDOW_SIZE,
        flags=sdl2.video.SDL_WINDOW_RESIZABLE
    )
    sdl2.SDL_SetWindowMinimumSize(window.window, DEFAULT_WINDOW_SIZE[0] // 2, DEFAULT_WINDOW_SIZE[1] // 2)
    window.show()

    renderer = sdl2.ext.Renderer(window)
    drawer = CurvesDrawer(window, DEFAULT_WINDOW_SIZE, renderer)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_WINDOWEVENT:
                renderer.clear(COLOR_WHITE)
                if selected_curve == 'cissoid':
                    drawer.draw_cissoid(CISSOID_PARAMS['a'], CISSOID_PARAMS['t_interval'], STEP)
                elif selected_curve == 'folium':
                    drawer.draw_folium(FOLIUM_PARAMS['a'], FOLIUM_PARAMS['t_intervals'], STEP)
                elif selected_curve == 'cardioid':
                    drawer.draw_cardioid(CARDIOID_PARAMS['a'], CARDIOID_PARAMS['t_interval'], STEP)
                elif selected_curve == 'snail':
                    drawer.draw_snail(SNAIL_PARAMS['a'], SNAIL_PARAMS['l'], SNAIL_PARAMS['t_interval'], STEP)
                elif selected_curve == 'epicycloid':
                    drawer.draw_epicycloid(EPICYCLOID_PARAMS['a'], EPICYCLOID_PARAMS['b'],
                                           EPICYCLOID_PARAMS['t_interval'], STEP)
                elif selected_curve == 'spiral':
                    drawer.draw_spiral(SPIRAL_PARAMS['a'], SPIRAL_PARAMS['phi_interval'], STEP)
                renderer.present()

    sdl2.ext.quit()
    return 0


if __name__ == '__main__':
    sys.exit(main())

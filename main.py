import pygame

from buffalo import utils
import menu

def main():
    
    while not utils.end:
        utils.scene.logic()
        utils.scene.update()
        utils.scene.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

if __name__ == "__main__":
    
    if not utils.init(
            caption="Heistboys",
            fullscreen=True       
    ):
        print('buffalo.utils failed to initialize')
        pygame.quit()
        exit()
    
    utils.set_scene( menu.Menu() )
    
    main()
    
    pygame.quit()

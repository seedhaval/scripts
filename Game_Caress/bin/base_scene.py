import cfg
from helper import ResizableImage, get_card_file
import pygame
import calc


class BaseScene:
    def __init__(self, gvar):
        self.gvar = gvar
        menu_top = cfg.screen_height - 125
        self.bigpart = ResizableImage(get_card_file("selopt"), 0, 0,
                                      cfg.screen_width,
                                      cfg.screen_height - 150, gvar)
        self.actor = ResizableImage(get_card_file("actor"), 0, menu_top, 100,
                                    100, gvar)
        self.actee = ResizableImage(get_card_file("actee"), 125, menu_top, 100,
                                    100, gvar)
        self.part = ResizableImage(get_card_file("part"), 250, menu_top, 100,
                                   100, gvar)
        self.action = ResizableImage(get_card_file("action"), 375, menu_top,
                                     100,
                                     100, gvar)
        self.create_buttons()
        self.set_animation_vars()

    def set_animation_vars(self):
        self.points = []
        self.animating = False
        self.polygon_path = []
        self.current_point = 0
        self.blue_circle_pos = None

    def create_buttons(self):
        menu_top = cfg.screen_height - 125
        font = pygame.font.Font(None, 36)
        self.go_button = pygame.Rect(500, menu_top, 100, 100)
        self.stop_button = pygame.Rect(625, menu_top, 100, 100)
        self.go_text = font.render("Go", True, (0, 0, 0))
        self.stop_text = font.render("Stop", True, (0, 0, 0))

    def show_animation(self):
        for point in self.points:
            pygame.draw.circle(self.gvar["screen"], cfg.RED, point, 10)
        if self.animating and self.polygon_path:
            start = self.polygon_path[self.current_point]
            end = self.polygon_path[
                (self.current_point + 1) % len(self.polygon_path)]
            self.blue_circle_pos = calc.calculate_movement(
                self.blue_circle_pos or start, end, cfg.SPEED, self.gvar["dt"])

            if calc.distance(self.blue_circle_pos, end) < 1:
                self.current_point = (self.current_point + 1) % len(
                    self.polygon_path)
                self.blue_circle_pos = end

            pygame.draw.circle(self.gvar["screen"], cfg.BLUE, (
                int(self.blue_circle_pos[0]), int(self.blue_circle_pos[1])), 10)

    def show_buttons(self):
        white = (255, 255, 255)
        screen = self.gvar["screen"]
        pygame.draw.rect(screen, white, self.go_button)
        pygame.draw.rect(screen, white, self.stop_button)
        screen.blit(self.go_text, (self.go_button.x + 25, self.go_button.y + 5))
        screen.blit(self.stop_text, (self.stop_button.x + 15,
                                     self.stop_button.y + 5))

    def show(self):
        self.gvar["screen"].fill((0, 0, 0))
        self.bigpart.show()
        self.actor.show()
        self.actee.show()
        self.part.show()
        self.action.show()
        self.show_buttons()
        self.show_animation()
        pygame.display.flip()

    def check_click(self, event):
        if self.actor.check_if_point_contains(event.pos):
            self.gvar["char_mode_obj"] = self.actor
            self.gvar["current_scene"] = "sel_char"
        elif self.actee.check_if_point_contains(event.pos):
            self.gvar["char_mode_obj"] = self.actee
            self.gvar["current_scene"] = "sel_char"
        elif self.action.check_if_point_contains(event.pos):
            self.gvar["carousal_mode_obj"] = [self.action]
            self.gvar["current_scene"] = "sel_action"
        elif self.part.check_if_point_contains(event.pos):
            self.gvar["carousal_mode_obj"] = [self.part, self.bigpart]
            self.gvar["current_scene"] = "sel_part"
        elif (self.bigpart.check_if_point_contains(event.pos) and not
        self.animating):
            self.points.append(event.pos)
        elif self.go_button.collidepoint(event.pos) and self.points:
            self.animating = True
            self.polygon_path = self.points[:]
            self.points.clear()
            self.blue_circle_pos = None
            self.current_point = 0
        elif self.stop_button.collidepoint(event.pos):
            self.animating = False
            self.blue_circle_pos = None
            self.polygon_path = []

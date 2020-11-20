from __future__ import print_function
import pygame
import os


class Slicer(object):
    def __init__(
        self,
        screen,
        font_size=10,
        spacing=4,
        background_color=(255, 255, 255),
        header_color=(125, 175, 255)
    ):
        font_file = pygame.font.get_default_font()
        self.font = pygame.font.Font(font_file, font_size)
        self.square_size = {}
        self.square_pos = {}
        self.font_size = font_size
        self.screen = screen
        self.background_color = background_color
        self.header_color = header_color

    def start(self, path):
        self.draw_background(path)

        self.square_size = {
            path: list(self.screen.get_size())  # whole window
        }

        self.square_pos = {
            path: [0, 0]  # top left
        }

    def draw_background(self, path):
        self.screen.fill(self.background_color)
        text = self.font.render(path, True, self.header_color)
        text_width = text.get_width()
        screen_width = self.screen.get_width()
        self.screen.blit(text, ((screen_width - text_width) / 2, 2))

    def draw_level(
        self,
        root,
        root_size,
        directory_sizes,
        file_sizes,
        spacing=4,
        square_color=(200, 225, 255),
        font_color=(0, 0, 0),
        border_color=(0, 0, 0),
    ):
        # folders which would be smaller than this won't be drawn
        min_square_size = (2 * spacing + 3 * self.font_size, 3 * spacing + self.font_size)

        if root not in self.square_size:
            # need to know the details of the root directory to be able to draw in it
            return
        elif root not in self.square_pos:
            return

        # the position to draw the next square
        pos = self.square_pos[root]
        pos[0] += spacing
        pos[1] += self.font_size + 2 * spacing  # leave room for text

        horizontal = self.square_size[root][0] > self.square_size[root][1]

        for relpath, size in directory_sizes + file_sizes:
            fullpath = os.path.join(root, relpath)
            self.square_size[fullpath] = self.square_size[root][:]  # copy the size of the parent directory

            # work out the dimensions of the square (and store in dictionaries for later use)
            if horizontal:
                (self.square_size[fullpath])[0] = int(round((self.square_size[fullpath][0] - spacing) * (float(size) / float(root_size)))) - spacing  # use the foldersize to scale the remaining width
                (self.square_size[fullpath])[1] -= (self.font_size + 3 * spacing)  # the height is smaller than the parent due to spacing

                if self.square_size[fullpath][0] < min_square_size[0] or self.square_size[fullpath][1] < min_square_size[1]:  # too small
                    del self.square_size[fullpath]  # don't draw this directory
                    continue
                self.square_pos[fullpath] = pos[:]
                pos[0] = pos[0] + (self.square_size[fullpath])[0] + spacing  # the next square is to the right of this one
            else:
                (self.square_size[fullpath])[0] -= 2 * spacing
                (self.square_size[fullpath])[1] = int(round((self.square_size[fullpath][1] - self.font_size - (2 * spacing)) * (float(size) / float(root_size)))) - spacing  # scale the width, but subtract for spacing
                if self.square_size[fullpath][0] < min_square_size[0] or self.square_size[fullpath][1] < min_square_size[1]:  # too small
                    del self.square_size[fullpath]  # don't draw this directory
                    continue
                self.square_pos[fullpath] = pos[:]
                pos[1] = pos[1] + (self.square_size[fullpath])[1] + spacing  # the next square is to the right of this one

            # draw the square
            surface = pygame.Surface(tuple(self.square_size[fullpath]))
            surface.fill(square_color)
            pygame.draw.rect(surface, border_color, (0, 0, self.square_size[fullpath][0], self.square_size[fullpath][1]), 1)
            text = self.font.render(relpath, True, font_color)  # write the directory name
            surface.blit(text, (spacing, spacing))
            self.screen.blit(surface, tuple(self.square_pos[fullpath]))


def slice_and_dice(folder_size, directory, screen, fontsize=10):
    slicer = Slicer(screen)
    slicer.start(directory)
    pygame.display.flip()
    for root, dirs, files in os.walk(directory, topdown=True):
        directory_sizes = []
        file_sizes = []
        for filename in dirs:
            full_path = os.path.join(root, filename)
            size = folder_size[full_path]
            directory_sizes.append((filename, size))
        for filename in files:
            full_path = os.path.join(root, filename)
            try:
                size = folder_size[full_path]
            except KeyError:
                continue
            file_sizes.append((filename, size))

        slicer.draw_level(root, folder_size[root], directory_sizes, file_sizes)
    pygame.display.flip()

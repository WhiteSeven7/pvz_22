class DrawComponent:
    def __init__(self, image, pos):
        self.image = image
        self.rect = self.image.get_rect(center=pos)

    def move(self, new_pos):
        self.rect.center = new_pos

    def update(self, surface):
        surface.blit(self.image, self.rect)


class AnimationComponent:
    def __init__(self, images, pos):
        self.images = images
        self.image = images.get(0, None)
        self.rect = self.image.get_rect(center=pos)

    def move(self, new_pos):
        self.rect.center = new_pos

    def update(self, surface, index):
        surface.blit(self)

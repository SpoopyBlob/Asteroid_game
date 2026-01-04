import pygame

class Assets():
    def __init__(self):
        """player"""
        player = pygame.image.load("asteroid_game/assets/Ship_4.png")
        self.player = pygame.transform.scale(player, (80, 80))
        self.player_rect = self.player.get_rect()

        """shot"""
        shot = pygame.image.load("asteroid_game/assets/Shot.png")
        self.shot = pygame.transform.scale(shot, (60, 60))
        self.shot_rect = self.shot.get_rect()
        

        """asteroid"""
        self.asteroid_images = self.load_asteroid_imgs()
        self.asteroid_rects = self.load_asteroid_rects()
        self.asteroid_masks = self.load_asteroid_masks()

        #masks

    
    def load_asteroid_imgs(self):
        asteroid_sheet = pygame.image.load("asteroid_game/assets/asteroids.png")
        
        asteroid_images = []
        for row in range(7):
            for col in range(7):
                if row == 7 and col > 6:
                    break
                rect = pygame.Rect(col * 128, row * 128, 128, 128)
                image = asteroid_sheet.subsurface(rect)
                image = pygame.transform.scale(image, (110, 110))
                smaller_image = pygame.transform.scale(image, (70, 70))
                larger_image = pygame.transform.scale(image, (150, 150))
                asteroid_images.append((smaller_image, image, larger_image))

        return tuple(asteroid_images)
    
    def load_asteroid_rects(self):
        asteroid_rects = []

        for tup in self.asteroid_images:
            new_tup = []
            for img in tup:
                new_tup.append(img.get_rect())
            asteroid_rects.append(tuple(new_tup))

        return tuple(asteroid_rects)
    
    def load_asteroid_masks(self):
        asteroid_masks = []

        for tup in self.asteroid_images:
            new_tup = []
            for asteroid in tup:
                new_tup.append(pygame.mask.from_surface(asteroid))
            asteroid_masks.append(tuple(new_tup))
        
        return tuple(asteroid_masks)

    def get_asteroid_img(self, sprite_id):
        idx, size_idx = self.ast_id_to_index(sprite_id)
        return self.asteroid_images[idx][size_idx]
    
    def get_asteroid_rect(self, sprite_id):
        idx, size_idx = self.ast_id_to_index(sprite_id)
        return self.asteroid_rects[idx][size_idx]
    
    def get_asteroid_mask(self, sprite_id):
        idx, size_idx = self.ast_id_to_index(sprite_id)
        return self.asteroid_masks[idx][size_idx]

    def ast_id_to_index(self, sprite_id):
        split_id = sprite_id.split("_")
        idx = int(split_id[0])
        size_idx = int(split_id[1]) - 1
        return idx, size_idx

    def get_img(self, sprite_id):
        if "spaceship" in sprite_id:
            return self.player
        elif "shot" in sprite_id:
            return self.shot
        elif "asteroid" in sprite_id:
            return self.get_asteroid_img(sprite_id)

    def get_rect(self, sprite_id):
        if "spaceship" in sprite_id:
            return self.player_rect
        elif "shot" in sprite_id:
            return self.shot_rect
        elif "asteroid" in sprite_id:
            return self.get_asteroid_rect(sprite_id)
        
    
        



        

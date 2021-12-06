
class MAIN:
    def draw_score(self):
        score_text = str(len(self.snake.body) - "snake-starting-length")
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,position)
        
        #high score requires rest of code

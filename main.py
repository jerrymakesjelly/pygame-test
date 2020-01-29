import pygame
import framework
import sprites.ball

class StateMachine(object):
    HIT_TOP = pygame.USEREVENT + 1
    HIT_BOTTOM = pygame.USEREVENT + 2
    HIT_LEFT = pygame.USEREVENT + 3
    HIT_RIGHT = pygame.USEREVENT + 4

    def __init__(self, screen):
        self.screen = screen
        self.ball = sprites.ball.Ball(pygame.sprite.Group())
    
    def custom_events(self):
        return {
            self.HIT_TOP: lambda: self.ball.rect.top < 0,
            self.HIT_BOTTOM: lambda: self.ball.rect.bottom > self.screen.get_size()[1],
            self.HIT_LEFT: lambda: self.ball.rect.left < 0,
            self.HIT_RIGHT: lambda: self.ball.rect.right > self.screen.get_size()[0],
        }
    
    def transition(self):
        return {
            self.state_1: {
                self.HIT_TOP: self.state_2,
                self.HIT_RIGHT: self.state_3,
            },
            self.state_2: {
                self.HIT_BOTTOM: self.state_1,
                self.HIT_RIGHT: self.state_4,
            },
            self.state_3: {
                self.HIT_LEFT: self.state_1,
                self.HIT_TOP: self.state_4,
            },
            self.state_4: {
                self.HIT_BOTTOM: self.state_3,
                self.HIT_LEFT: self.state_2,
            }
        }

    def state_1(self):
        '''Move bottom-right'''
        self.screen.fill(pygame.Color("black"))
        self.ball.rect = self.ball.rect.move([1, -1])
        self.screen.blit(self.ball.image, self.ball.rect)
    
    def state_2(self):
        '''Move top-right'''
        self.screen.fill(pygame.Color("black"))
        self.ball.rect = self.ball.rect.move([1, 1])
        self.screen.blit(self.ball.image, self.ball.rect)

    def state_3(self):
        '''Move bottom-left'''
        self.screen.fill(pygame.Color("black"))
        self.ball.rect = self.ball.rect.move([-1, -1])
        self.screen.blit(self.ball.image, self.ball.rect)
    
    def state_4(self):
        '''Move top-left'''
        self.screen.fill(pygame.Color("black"))
        self.ball.rect = self.ball.rect.move([-1, 1])
        self.screen.blit(self.ball.image, self.ball.rect)

if __name__ == '__main__':
    screen = pygame.display.set_mode((640, 480))
    dfa = StateMachine(screen)
    g = framework.Game(screen, dfa, dfa.state_1)
    g.run()
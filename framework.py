import pygame

class Game(object):
    def __init__(self, screen, states, start_state):
        self.screen = screen
        self.dfa = states
        self.state = start_state
        self.running = False
    
    def event_loop(self):
        for e in self.dfa.custom_events():
            if self.dfa.custom_events()[e]():
                pygame.event.post(pygame.event.Event(e))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type in self.dfa.transition()[self.state]:
                self.state = self.dfa.transition()[self.state][event.type]
                print('Receive event '+str(event.type)+', transit to state '+str(hex(id(self.state))))
    
    def run(self):
        self.running = True
        while self.running:
            self.event_loop()
            self.state()
            pygame.display.flip()

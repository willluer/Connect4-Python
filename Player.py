class Player:
    def __init__(self,player_id):
        self.player_id = player_id

    def get_next_move(self,state):
        '''
        Input: Board state (numpy array)
        Output: Column choice
        '''
        raise NotImplementedError()

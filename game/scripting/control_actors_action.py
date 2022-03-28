import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the player.
    
    The responsibility of ControlActorsAction is to get the direction and move the frog.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)
        self._new_game = False
        self._last_direction = 'w'

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # Frog movement
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            if self._last_direction != 'a':
                self._last_direction = 'a'
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            if self._last_direction != 'd':
                self._last_direction = 'd'
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            if self._last_direction != 'w':
                self._last_direction = 'w'
                
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            if self._last_direction != 's':
                self._last_direction = 's'
        
        frog = cast.get_first_actor("frog")
        frog.turn_head(self._direction)

        # Signal new game
        if self._keyboard_service.is_key_down('n'):
            collision = script.get_first_action("check")
            collision.start_new_game()
            all_messages = cast.get_actors("messages")
            for message in all_messages:
                cast.remove_actor("messages", message)
            frog.__init__()
            all_obstacles = cast.get_actors("obstacles")
            for obstacle in all_obstacles:
                obstacle.__init__()
            all_prizes = cast.get_actors("prizes")
            for prize in all_prizes:
                prize.__init__()
            self._direction = Point(0, -constants.CELL_SIZE)
            self._new_game = False
            self._last_direction = 'w'

import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Frog(Actor):
    """
    A long Cycle with a trailing tail.
    
    The responsibility of cycle is to move itself and avoid other cycle tails.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        """Constructs a new Cycle.
        
        Args:
            None.
        """
        super().__init__()
        self._velocity = Point(0, -constants.CELL_SIZE)
        self.is_game_over = False
        self._segments = []

    def get_segments(self):
        """Gets the cycle's segment list.
        
        Returns:
            string: The cycle's segment list.
        """
        return self._segments

    def move_next(self):
        """Moves the cycle to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            None.
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets the cycle's head segment.
        
        Returns:
            string: The cycle's head segment.
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """
        Increases the cycle's segment list by one
        
        Args:
            int: The length of the cycle's segment list.
        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
        
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self.get_color())
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Changes the direction of the cycles by changing the velocity so the head moves in a different direction.
        
        Returns:
            Point: The cycle's velocity.
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """
        Builds the cycle's segment list.
        
        Based on the CYCLE_LENGTH constant

        """
        x = self.get_cycle_x_start()
        y = self.get_cycle_y_start()
    
        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            color = self.get_color()
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
    
    def get_cycle_x_start(self):
        """Gets the cycle's start position x value.
        
        Returns:
            int: The cycle's start position x value.
        """
        return(int(constants.CELL_SIZE * (constants.COLUMNS / 6)))

    def get_cycle_y_start(self):
        """Gets the cycle's start position y value.
        
        Returns:
            int: The cycle's start position y value.
        """
        return(int(constants.CELL_SIZE * (constants.ROWS / 2)))
    
    def get_color(self):
        """Gets the cycle's color.
        
        Returns:
            color: The cycle's color (r, g, b).
        """
        return(self._color)

    def set_game_over(self):
        """
        Sets the cycle's game over value so that it turns white and no longer scores points.
        
        """
        self.is_game_over = True
        self._color = constants.WHITE
  
    def is_game_over(self):
        """
        Gets the cycle's game over value (boolean).
        
        Returns:
            boolean: The cycles's game over value.
        """
        return(self.is_game_over)
  

        
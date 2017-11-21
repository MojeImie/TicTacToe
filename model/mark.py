class Mark:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

    free = []
    all_cross = []
    all_circle = []

    @classmethod
    def delete(cls):
        cls.free = []    
        cls.all_circle = []
        cls.all_cross = []

    def __init__(self, number):
        if not isinstance(number, int):
            raise ValueError('Invalid type!')

        self.number = number
        self.cross = False
        self.circle = False
        
        Mark.free.append(self)

    def active_circle(self):
        self.circle = True
        Mark.all_circle.append(self)
        Mark.all_circle = sorted(Mark.all_circle, key=lambda mark: mark.number) 

    def active_cross(self):
        self.cross = True
        Mark.all_cross.append(self)
        Mark.all_cross = sorted(Mark.all_cross, key=lambda mark: mark.number) 
        
    def __str__(self):
        mark = str(self.number)
        if self.cross:
            mark = Mark.BLUE+'X'+Mark.END
        elif self.circle:
            mark = Mark.GREEN+'O'+Mark.END
        return mark
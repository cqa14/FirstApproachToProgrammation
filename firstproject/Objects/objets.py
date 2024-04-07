
from obj import Object
from obj import Cube

object1 = Object("Prout", 3)
object2 = Object("Jelly", 15)

object1.set_name(":)")
object1.get_another_name(object2)

cube1 = Cube(":-)", 4, True)
cube1.is_cubic()

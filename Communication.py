from networktables import NetworkTables

vision_table = None


def init():
    NetworkTables.initialize(server="10.29.15.2")
    sd = NetworkTables.getTable("SmartDashboard")

    global vision_table
    vision_table = sd.getSubTable("JetPanda")


def update_tables(best_target):
    vision_table.putNumber("angle", best_target.angle)
    vision_table.putNumber("distance", best_target.distance)

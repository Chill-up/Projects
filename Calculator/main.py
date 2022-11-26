import controller
import model
import view

model.init_first()
while True:
    if model.init_ops():
        break
    model.init_second()
    controller.operation()
    view.print_total()
    model.first = model.total



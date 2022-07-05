class App:
  def __init__(self, room):
    self.room = room

if __name__ == '__main__':
  import argparse
  import keybow

  keybow.setup(keybow.MINI)

  parser = argparse.ArgumentParser(description='Keybow remote for hue lights')
  parser.add_argument('--room', metavar='r', required=True, type=str, help='The name of the room for hue-mote to control')

  args = parser.parse_args()

  app = App(args.room)

  @keybow.on()
  def handle_key(index, state):
    if state:
        keybow.set_led(index, 255, 0, 0)
    else:
        keybow.set_led(index, 0, 0, 0)

  while True:
    keybow.show()

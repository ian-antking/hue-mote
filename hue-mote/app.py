class App:
  def __init__(self, room):
    self.room = room

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Keybow remote for hue lights')
  parser.add_argument('--room', metavar='r', required=True, type=str, help='The name of the room for hue-mote to control')

  args = parser.parse_args()

  app = App(args.room)

  print(app.room)
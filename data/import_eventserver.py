"""
Import sample data for similar product engine
"""

import predictionio
import argparse
import random

DATA_DELIMITER = "::"
SEED = 3

def import_events(client, file):
  f = open(file, 'r')
  random.seed(SEED)
  count = 0
  print client.get_status()
  print "Importing data..."

  # each user randomly viewed 10 items
  for line in f:
    data = line.rstrip('\n').split(DATA_DELIMITER)
    client.create_event(
      event="view",
      entity_type="user",
      entity_id=data[0],
      target_entity_type="item",
      target_entity_id=data[1]
    )
    count += 1

  print "%s events are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for similar product engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/sample_data.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)

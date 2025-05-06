"""
You’re fetching data from an API and expect each record to have these fields:

EXPECTED_FIELDS = ["id", "title", "body", "userId"]

Write a Python function that:

1. Takes a list of JSON objects (list[dict])
2. Validates each row has all expected fields
3. If a row is valid, keep it
4. If a row is invalid (missing any field), log it and skip it

"""

logging.basicConfig(filename='invalid_rows.log', level = logging.WARNING)


def data_validation(data):

  valid_rows = []
  for row in data:
    if all(field in row for field in EXPECTED_FIELDS):
      valid_rows.append(row)
    else:
      logging.warning(f"Row does not match schema: {row}") 
  return valid_rows

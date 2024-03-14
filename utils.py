import requests

def run_query(item_name):
    """
    Fetch item information from the Tarkov API

    Args:
        item_name (str): Name of the item

    Returns:
        dict: JSON response data from the API
    """
    headers = {"Content-Type": "application/json"}
    query = """
    {
      items(name: "%s") {
        name
        lastLowPrice
        avg24hPrice
        usedInTasks {
          name
          kappaRequired
          trader {
            name
          }
        }
      }
    }
    """ % item_name
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))
import requests, json

# Generate Data for ETL 

def gen_data():

    try:

        api_url = "https://randomuser.me/api/?results=10"

        response = requests.get(api_url).json()

        with open('sample.json', 'w') as api_data:
            api_data.write(json.dumps(response, indent=4))

    except Exception as err:

        print(f"Error During API Data Write : {err}")


def write_to_db(src_file, src_db, tar_db=None):

    # src_db = MySQL

    # tar_db = Postgres

    # load json into a Database / File 

# gen_data()
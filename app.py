from chalice import Chalice
import gspread

gc = gspread.service_account(filename='chalicelib/credentials.json')

app = Chalice(app_name='hanzi-wrapper')

def convert_array_to_dicts(header_keys, data_arrays):
    response_data = []
    for array in data_arrays:
        x = {}
        index = 0
        for header in header_keys:
            x[header] = array[index]
            index += 1
        response_data.append(x)

    return response_data


def get_rows(title, tab):
    # Open the Google Sheet by its title
    sheet_title = title
    sheet = gc.open(sheet_title)
    worksheet_title = tab
    worksheet = sheet.worksheet(worksheet_title)
    data = worksheet.get_all_values()
    header_keys = data[0]
    data_arrays = data[1:]
    response = convert_array_to_dicts(header_keys, data_arrays)
    return response

@app.route('/sheet/{title}/{tab}')
def index(title, tab):
    return get_rows(title, tab)

@app.route('/')
def index():
    return "hello"
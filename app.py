from chalice import Chalice
import gspread

gc = gspread.service_account(filename='chalicelib/credentials.json')

app = Chalice(app_name='hanzi-wrapper')

def get_rows(title, tab):
    # Open the Google Sheet by its title
    sheet_title = title
    sheet = gc.open(sheet_title)
    worksheet_title = tab
    worksheet = sheet.worksheet(worksheet_title)
    data = worksheet.get_all_values()
    return data

@app.route('/sheet/{title}/{tab}')
def index(title, tab):
    return get_rows(title, tab)

@app.route('/')
def index():
    return "hello"
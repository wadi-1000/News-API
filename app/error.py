from flask import render_template
from app import app
@app.errohandler(404)
def four_Ow_four(error):
    '''
    Function to display 404 error page
    '''
    return render_template('fourOwfour.html'),404
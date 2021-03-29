import os
from app import app
from flask import Flask,flash,request,redirect,send_file,render_template
from convert_file import converted_file

@app.route('/file_downloads/')
def file_downloads():
    try:
        return render_template('downloads.html')
    except Exception as e:
        return str(e)


@app.route('/files-return/')
def files_return():
    try:
        return send_file('/Users/muhammadaliamin/Documents/send_files/output1.pdf', as_attachment=True, attachment_filename='')
    except Exception as e:
        return str(e)

app.run(debug=True)
"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask.helpers import send_from_directory
from flask import render_template, request, redirect, url_for, flash, session, abort
import os
from app.models import UserProp
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import PropertyForm
from flask import render_template, request, redirect, url_for



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/property',methods=['POST','GET'])
def property():
    form=PropertyForm()
    if request.method=='POST' and form.validate_on_submit():
        title=form.title.data
        bedroom_num=form.bedroom_num.data
        bathroom_num=form.bathroom_num.data
        location=form.location.data
        price=form.price.data
        types=form.types.data
        desciption=form.desciption.data

        photo=request.files['photo']
        filename=secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

         

        propert= UserProp(title, bedroom_num, bathroom_num, location,price,types,desciption,filename)
        db.session.add(propert)
        db.session.commit()

        flash('Property Added Successfully', 'success')
        return redirect(url_for('properties'))
    
    return render_template('property.html', form=form)

@app.route('/upload/<filename>')
def myimage(filename):
    root_dir=os.getcwd()
    return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']),filename)

@app.route('/properties')
def properties():
    prop= UserProp.query.all()
    return render_template('properties.html',prop=prop)

@app.route('/property/<propertyid>')
def propertyid(propertyid):
    propertyid=UserProp.query.get(propertyid)
    return render_template('propertyid.html', property=propertyid)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")

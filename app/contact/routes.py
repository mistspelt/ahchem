from app.contact.sendemail import send_contact_email
from flask import render_template, redirect, url_for, flash
from app.contact import bp
from app.contact.forms import ContactForm

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        send_contact_email(name, email, subject, message)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('contact/contact.html', form=form)
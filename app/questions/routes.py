from flask import render_template, url_for, redirect, flash
from flask_login import current_user
from app.questions import bp
from app import db
from app.models import Unit, Topic, Question
from app.questions.questions import getunits, gettopics, getallquestions, getquestion, getunitname, gettopicname, getmarkingpath, getquestionpath, recordmarks, getmarks, gettopicattempts
from app.questions.forms import RecordMarksForm

@bp.route('/units')
def units():
    # returns all units in the database
    units = getunits()
    return render_template('questions/units.html', units=units)

@bp.route('/units/<int:unit_id>/topics')
def topics(unit_id):
    # Get all topics for the unit
    topics = gettopics(unit_id)
    unit_name = getunitname(unit_id)

    # Fetch topic attempts if the user is logged in
    topic_attempts = {}
    if not current_user.is_anonymous:
        topic_attempts = gettopicattempts(current_user.id, unit_id)

    return render_template(
        'questions/topics.html',
        topics=topics,
        unit_name=unit_name,
        unit_id=unit_id,
        topic_attempts=topic_attempts
    )

@bp.route('/units/<int:unit_id>/topics/<int:topic_id>/questions')
def questions(unit_id, topic_id):
    # get all questions in the database for a given topic
    questions = getallquestions(topic_id)
    unit_name = getunitname(unit_id)
    topic_name = gettopicname(topic_id)

    # Check if the user is logged in and fetch attempt data
    attempts = {}
    if not current_user.is_anonymous:
        for question in questions:
            attempt = getmarks(current_user.id, question.id)
            attempts[question.id] = attempt.score if attempt else None

    return render_template('questions/questions.html', questions=questions, unit_name=unit_name, topic_name=topic_name, unit_id=unit_id, topic_id=topic_id, attempts=attempts)

@bp.route('/units/<int:unit_id>/topics/<int:topic_id>/questions/<int:question_id>', methods=['GET', 'POST'])
def question(unit_id, topic_id, question_id):
    # get a question in the database
    question = getquestion(question_id)
    unit_name = getunitname(unit_id)
    topic_name = gettopicname(topic_id)
    question_path = getquestionpath(question_id)
    marking_path = getmarkingpath(question_id)
    form = RecordMarksForm()

    if form.validate_on_submit():
        score = form.marks.data
        if score < 0 or score > question.max_marks:
            flash(f'Score must be between 0 and {question.max_marks} for this question.', 'danger')
            return redirect(url_for('questions.question', unit_id=unit_id, topic_id=topic_id, question_id=question_id))
        # record the marks in the database
        recordmarks(current_user.id, question.id, score)
        flash('Marks recorded successfully!', 'success')
        return redirect(url_for('questions.question', unit_id=unit_id, topic_id=topic_id, question_id=question_id))
    
    if not current_user.is_anonymous:
        attempt = getmarks(current_user.id, question.id)
        return render_template('questions/view_question.html', question=question, unit_name=unit_name, topic_name=topic_name, unit_id=unit_id, topic_id=topic_id, question_path=question_path, marking_path=marking_path, form=form, attempt=attempt)
    
    return render_template('questions/view_question.html', question=question, unit_name=unit_name, topic_name=topic_name, unit_id=unit_id, topic_id=topic_id, question_path=question_path, marking_path=marking_path, form=form)


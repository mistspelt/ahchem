from app import db
from app.models import Unit, Topic, Question, User, Attempt
from sqlalchemy import func

def getunits():
    # fetches all units in the database
    units = Unit.query.all()
    return units

def gettopics(unit_id):
    # fetches all topics in the database for a given unit
    topics = Topic.query.filter_by(unit_id=unit_id).all()
    return topics

def getallquestions(topic_id):
    # fetches all questions in the database for a given topic
    questions = Question.query.filter_by(topic_id=topic_id).all()
    return questions

def getquestion(question_id):
    # fetches a question in the database for a given question id
    question = Question.query.filter_by(id=question_id).first()
    return question

def getunitname(unit_id):
    # fetches the name of the unit for a given unit id
    unit = Unit.query.filter_by(id=unit_id).first()
    return unit.name if unit else None

def gettopicname(topic_id):
    # fetches the name of the topic for a given topic id
    topic = Topic.query.filter_by(id=topic_id).first()
    return topic.name if topic else None

def getquestionpath(question_id):
    # returns the path to the question for a given question id
    q = Question.query.filter_by(id=question_id).first()
    path = f'{q.year}_{q.section}_{q.question_number}.png'
    return path if q else None

def getmarkingpath(question_id):
    # returns the path to the marking scheme for a given question id
    q = Question.query.filter_by(id=question_id).first()
    if q is None:
        return None
    if q.section == '1':
        return None
    path = f'{q.year}_{q.section}_{q.question_number}_mi.png'
    return path

def recordmarks(user_id, question_id, score):
    # records the marks for a given user and question
    attempt = Attempt.query.filter_by(user_id=user_id, question_id=question_id).first()
    if attempt:
        attempt.score = score
        db.session.commit()
    else:
        attempt = Attempt(user_id=user_id, question_id=question_id, score=score)
        db.session.add(attempt)
        db.session.commit()

def getmarks(user_id, question_id):
    # fetches the marks for a given user and question
    attempt = Attempt.query.filter_by(user_id=user_id, question_id=question_id).first()
    return attempt if attempt else None

def gettopicattempts(user_id, unit_id):
    # fetches total questions and attempted questions for each topic in a unit
    results = (
        db.session.query(
            Topic.id.label('topic_id'),
            func.count(Question.id).label('total_questions'),
            func.count(func.nullif(Attempt.id, None)).label('attempted_questions')
        )
        .join(Question, Question.topic_id == Topic.id)
        .outerjoin(Attempt, (Attempt.question_id == Question.id) & (Attempt.user_id == user_id))
        .filter(Topic.unit_id == unit_id)
        .group_by(Topic.id)
        .all()
    )

    # convert results into a dictionary
    topic_attempts = {
        result.topic_id: {
            'total': result.total_questions,
            'attempted': result.attempted_questions
        }
        for result in results
    }

    return topic_attempts

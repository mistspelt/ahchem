from app import create_app, db
from app.models import User, Question, Topic, Unit, oAuth, Attempt

app = create_app()

# sets up the database with initial topic, unit, and question data
# and clears any existing data in the database
# currently only contains data for the 2014 paper

def setup_db(db, app):
    with app.app_context():
        topics = db.session.query(Topic).all()
        units = db.session.query(Unit).all()
        questions = db.session.query(Question).all()
        attempts = db.session.query(Attempt).all()
        for attempt in attempts:
            db.session.delete(attempt)
        for question in questions:
            db.session.delete(question)
        for topic in topics:
            db.session.delete(topic)
        for unit in units:
            db.session.delete(unit)
        db.session.commit()

        # adding units ====
        db.session.add(Unit(name='Inorganic Chemistry')) # id 1
        db.session.add(Unit(name='Physical Chemistry')) # id 2
        db.session.add(Unit(name='Organic Chemistry')) # id 3
        db.session.add(Unit(name='Researching Chemistry')) # id 4

        # adding topics ====
        # for inorganic chem:
        db.session.add(Topic(name='Electromagnetic Radiation and Atomic Spectra', unit_id=1)) # id 1
        db.session.add(Topic(name='Atomic Orbitals, Electron Configurations and the Periodic Table', unit_id=1)) # id 2
        db.session.add(Topic(name='Transition Metals', unit_id=1))

        # for physical chem:
        db.session.add(Topic(name='Chemical Equilibrium', unit_id=2))
        db.session.add(Topic(name='Reaction Feasibility', unit_id=2))
        db.session.add(Topic(name='Kinetics', unit_id=2))

        # for organic chem:
        db.session.add(Topic(name='Molecular Orbitals', unit_id=3))
        db.session.add(Topic(name='Synthesis', unit_id=3))
        db.session.add(Topic(name='Stereochemistry', unit_id=3))
        db.session.add(Topic(name='Experimental Determination of Structure', unit_id=3))
        db.session.add(Topic(name='Pharmaceutical Chemistry', unit_id=3))

        # for researching chem:
        db.session.add(Topic(name='Stoichiometric Calculations', unit_id=4))
        db.session.add(Topic(name='Gravimetric Analysis', unit_id=4))
        db.session.add(Topic(name='Volumetric Analysis', unit_id=4))
        db.session.add(Topic(name='Practical Skills', unit_id=4))
        
        # 2014 SECTION 1

        db.session.add(Question(topic_id=2, mi='B', question_number=1, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='C', question_number=2, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='C', question_number=3, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=1, mi='D', question_number=4, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='D', question_number=5, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=1, mi='B', question_number=6, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=1, mi='C', question_number=7, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='A', question_number=8, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='A', question_number=9, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=2, mi='C', question_number=10, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=3, mi='D', question_number=11, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=6, mi='B', question_number=13, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=6, mi='B', question_number=14, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=7, mi='B', question_number=15, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=9, mi='D', question_number=16, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=9, mi='A', question_number=17, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='B', question_number=18, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='C', question_number=19, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='B', question_number=20, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='C', question_number=21, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='D', question_number=22, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='B', question_number=23, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='A', question_number=24, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=8, mi='A', question_number=25, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=10, mi='D', question_number=26, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=10, mi='C', question_number=27, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=10, mi='D', question_number=28, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=10, mi='A', question_number=29, year=2014, max_marks=1, section='1'))
        db.session.add(Question(topic_id=11, mi='A', question_number=30, year=2014, max_marks=1, section='1'))

        # 2014 SECTION 2

        db.session.add(Question(question_number=2,sub_question='a',subsub_question='',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=2,sub_question='b',subsub_question='',max_marks=2,year=2014,section='2',topic_id=13))
        db.session.add(Question(question_number=2,sub_question='c',subsub_question='',max_marks=2,year=2014,section='2',topic_id=14))
        db.session.add(Question(question_number=2,sub_question='d',subsub_question='',max_marks=1,year=2014,section='2',topic_id=15))
        db.session.add(Question(question_number=3,sub_question='a',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=5))
        db.session.add(Question(question_number=3,sub_question='a',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=5))
        db.session.add(Question(question_number=3,sub_question='b',subsub_question='',max_marks=2,year=2014,section='2',topic_id=5))
        db.session.add(Question(question_number=5,sub_question='a',subsub_question='',max_marks=1,year=2014,section='2',topic_id=4))
        db.session.add(Question(question_number=5,sub_question='b',subsub_question='',max_marks=1,year=2014,section='2',topic_id=15))
        db.session.add(Question(question_number=5,sub_question='c',subsub_question='',max_marks=3,year=2014,section='2',topic_id=4))
        db.session.add(Question(question_number=6,sub_question='a',subsub_question='',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=6,sub_question='b',subsub_question='',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=6,sub_question='c',subsub_question='',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=7,sub_question='a',subsub_question='',max_marks=1,year=2014,section='2',topic_id=11))
        db.session.add(Question(question_number=7,sub_question='b',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=12))
        db.session.add(Question(question_number=7,sub_question='b',subsub_question='ii',max_marks=3,year=2014,section='2',topic_id=12))
        db.session.add(Question(question_number=8,sub_question='a',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=10))
        db.session.add(Question(question_number=8,sub_question='a',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=15))
        db.session.add(Question(question_number=8,sub_question='b',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=8,sub_question='b',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=8,sub_question='b',subsub_question='iii',max_marks=1,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=9,sub_question='a',subsub_question='',max_marks=1,year=2014,section='2',topic_id=9))
        db.session.add(Question(question_number=9,sub_question='b',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=10))
        db.session.add(Question(question_number=9,sub_question='b',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=10))
        db.session.add(Question(question_number=9,sub_question='b',subsub_question='iii',max_marks=2,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=11,sub_question='a',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=6))
        db.session.add(Question(question_number=11,sub_question='a',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=6))
        db.session.add(Question(question_number=11,sub_question=' b',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=6))
        db.session.add(Question(question_number=11,sub_question=' b',subsub_question='ii',max_marks=2,year=2014,section='2',topic_id=6))
        db.session.add(Question(question_number=11,sub_question='c',subsub_question='',max_marks=3,year=2014,section='2',topic_id=8))
        db.session.add(Question(question_number=11,sub_question='d',subsub_question='',max_marks=1,year=2014,section='2',topic_id=9))
        db.session.add(Question(question_number=12,sub_question='a',subsub_question='i',max_marks=2,year=2014,section='2',topic_id=13))
        db.session.add(Question(question_number=12,sub_question='a',subsub_question='ii',max_marks=1,year=2014,section='2',topic_id=13))
        db.session.add(Question(question_number=12,sub_question='b',subsub_question='',max_marks=2,year=2014,section='2',topic_id=13))
        db.session.add(Question(question_number=13,sub_question='a',subsub_question='i',max_marks=1,year=2014,section='2',topic_id=4))
        db.session.add(Question(question_number=13,sub_question='a',subsub_question='ii',max_marks=3,year=2014,section='2',topic_id=4))
        db.session.add(Question(question_number=13,sub_question='b',subsub_question='',max_marks=2,year=2014,section='2',topic_id=4))

        db.session.commit()


from app import create_app, db
from app.models import Unit, Topic, Question
from sqlalchemy.exc import IntegrityError

app = create_app()

NEW_UNITS = [
    {"name": "Inorganic Chemistry"},
    {"name": "Physical Chemistry"},
    {"name": "Organic Chemistry"},
    {"name": "Researching Chemistry"},
]

NEW_TOPICS = [
    {"name": "Electromagnetic Radiation and Atomic Spectra", "unit_name": "Inorganic Chemistry"},
    {"name": "Atomic Orbitals, Electron Configurations and the Periodic Table", "unit_name": "Inorganic Chemistry"},
    {"name": "Transition Metals", "unit_name": "Inorganic Chemistry"},
    {"name": "Chemical Equilibrium", "unit_name": "Physical Chemistry"},
    {"name": "Reaction Feasibility", "unit_name": "Physical Chemistry"},
    {"name": "Kinetics", "unit_name": "Physical Chemistry"},
    {"name": "Molecular Orbitals", "unit_name": "Organic Chemistry"},
    {"name": "Synthesis", "unit_name": "Organic Chemistry"},
    {"name": "Stereochemistry", "unit_name": "Organic Chemistry"},
    {"name": "Experimental Determination of Structure", "unit_name": "Organic Chemistry"},
    {"name": "Pharmaceutical Chemistry", "unit_name": "Organic Chemistry"},
    {"name": "Stoichiometric Calculations", "unit_name": "Researching Chemistry"},
    {"name": "Gravimetric Analysis", "unit_name": "Researching Chemistry"},
    {"name": "Volumetric Analysis", "unit_name": "Researching Chemistry"},
    {"name": "Practical Skills", "unit_name": "Researching Chemistry"},
]


NEW_QUESTIONS = [
    # 2014 SECTION 1
    {"year":2014, "question_number":1, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":2, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":3, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":4, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2014, "question_number":5, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":6, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2014, "question_number":7, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2014, "question_number":8, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":9, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":10, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2014, "question_number":11, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2014, "question_number":13, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2014, "question_number":14, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2014, "question_number":15, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2014, "question_number":16, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2014, "question_number":17, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2014, "question_number":18, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":19, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":20, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":21, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":22, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":23, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":24, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":25, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2014, "question_number":26, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":27, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":28, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":29, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":30, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},

    # 2014 SECTION 2
    {"year":2014, "question_number":2, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":2, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2014, "question_number":2, "sub_question":"c", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Volumetric Analysis"},
    {"year":2014, "question_number":2, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2014, "question_number":3, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2014, "question_number":3, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2014, "question_number":3, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2014, "question_number":5, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2014, "question_number":5, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2014, "question_number":5, "sub_question":"c", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2014, "question_number":6, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":6, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":6, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":7, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2014, "question_number":7, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2014, "question_number":7, "sub_question":"b", "subsub_question":"ii", "max_marks":3, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2014, "question_number":8, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":8, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2014, "question_number":8, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":8, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":8, "sub_question":"b", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":9, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2014, "question_number":9, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":9, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2014, "question_number":9, "sub_question":"b", "subsub_question":"iii", "max_marks":2, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":11, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2014, "question_number":11, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2014, "question_number":11, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2014, "question_number":11, "sub_question":"b", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2014, "question_number":11, "sub_question":"c", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Synthesis"},
    {"year":2014, "question_number":11, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2014, "question_number":12, "sub_question":"a", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2014, "question_number":12, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2014, "question_number":12, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2014, "question_number":13, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2014, "question_number":13, "sub_question":"a", "subsub_question":"ii", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2014, "question_number":13, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Chemical Equilibrium"},

    # 2015 SECTION 1
    {"year":2015, "question_number":1, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2015, "question_number":2, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2015, "question_number":3, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":4, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":5, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":6, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":7, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":8, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":9, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":10, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2015, "question_number":11, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2015, "question_number":12, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2015, "question_number":13, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2015, "question_number":14, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2015, "question_number":15, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2015, "question_number":16, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2015, "question_number":17, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2015, "question_number":18, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2015, "question_number":19, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2015, "question_number":20, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2015, "question_number":21, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2015, "question_number":22, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2015, "question_number":23, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2015, "question_number":24, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2015, "question_number":25, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2015, "question_number":26, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2015, "question_number":27, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2015, "question_number":28, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Gravimetric Analysis"},
    {"year":2015, "question_number":29, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Gravimetric Analysis"},
    {"year":2015, "question_number":30, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},

    # 2015 SECTION 2
    {"year":2015, "question_number":1, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":1, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":1, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":1, "sub_question":"b", "subsub_question":"i", "max_marks":3, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2015, "question_number":1, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2015, "question_number":2, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2015, "question_number":2, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2015, "question_number":2, "sub_question":"c", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2015, "question_number":3, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":3, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":3, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":3, "sub_question":"b", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":3, "sub_question":"b", "subsub_question":"iv", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":3, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2015, "question_number":4, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":4, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2015, "question_number":4, "sub_question":"c", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2015, "question_number":4, "sub_question":"d", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Practical Skills"},
    {"year":2015, "question_number":4, "sub_question":"e", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2015, "question_number":5, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":5, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":5, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":5, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transition Metals"},
    {"year":2015, "question_number":6, "sub_question":"a", "subsub_question":"i", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2015, "question_number":6, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2015, "question_number":6, "sub_question":"b", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2015, "question_number":6, "sub_question":"b", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2015, "question_number":8, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":8, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":8, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":8, "sub_question":"c", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":8, "sub_question":"c", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":9, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2015, "question_number":9, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2015, "question_number":9, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2015, "question_number":9, "sub_question":"d", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":9, "sub_question":"d", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":9, "sub_question":"e", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2015, "question_number":10, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":10, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":10, "sub_question":"c", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":10, "sub_question":"c", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":10, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":10, "sub_question":"e", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2015, "question_number":10, "sub_question":"f", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":11, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":11, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2015, "question_number":12, "sub_question":"a", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2015, "question_number":12, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2015, "question_number":12, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},

    # 2016 SECTION 1
    {"year":2016, "question_number":1, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2016, "question_number":2, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":4, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":5, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Transition Metals"},
    {"year":2016, "question_number":6, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":7, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":8, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":9, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2016, "question_number":10, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2016, "question_number":11, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2016, "question_number":12, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2016, "question_number":13, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2016, "question_number":14, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2016, "question_number":15, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":16, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":17, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":18, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":19, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":20, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":21, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":22, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":23, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2016, "question_number":24, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2016, "question_number":25, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2016, "question_number":26, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2016, "question_number":27, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2016, "question_number":28, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2016, "question_number":29, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2016, "question_number":30, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},

    # 2016 SECTION 2
    {"year":2016, "question_number":1, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2016, "question_number":1, "sub_question":"a", "subsub_question":"ii", "max_marks":3, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2016, "question_number":1, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2016, "question_number":2, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":2, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":2, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "sub_question":"a", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":3, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2016, "question_number":4, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":4, "sub_question":"a", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":4, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":4, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":4, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":4, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":5, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":5, "sub_question":"b", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":5, "sub_question":"b", "subsub_question":"ii", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":6, "sub_question":"a", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2016, "question_number":6, "sub_question":"b", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2016, "question_number":6, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2016, "question_number":6, "sub_question":"b", "subsub_question":"iii", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2016, "question_number":7, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2016, "question_number":7, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2016, "question_number":7, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2016, "question_number":7, "sub_question":"b", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2016, "question_number":7, "sub_question":"c", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Synthesis"},
    {"year":2016, "question_number":8, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2016, "question_number":8, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2016, "question_number":8, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2016, "question_number":8, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2016, "question_number":8, "sub_question":"e", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2016, "question_number":9, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2016, "question_number":9, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2016, "question_number":9, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2016, "question_number":9, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2016, "question_number":9, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2016, "question_number":9, "sub_question":"b", "subsub_question":"iii", "max_marks":2, "section":"2", "topic_name":"Practical Skills"},
    {"year":2016, "question_number":9, "sub_question":"b", "subsub_question":"iv", "max_marks":2, "section":"2", "topic_name":"Practical Skills"},
    {"year":2016, "question_number":9, "sub_question":"b", "subsub_question":"v", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2016, "question_number":10, "sub_question":"a", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2016, "question_number":10, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2016, "question_number":10, "sub_question":"c", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2016, "question_number":10, "sub_question":"c", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2016, "question_number":10, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},

    # 2017 SECTION 1
    {"year":2017, "question_number":1, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":2, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":3, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":4, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":5, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":6, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":7, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":8, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2017, "question_number":9, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2017, "question_number":10, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2017, "question_number":11, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2017, "question_number":12, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2017, "question_number":13, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2017, "question_number":14, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2017, "question_number":15, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2017, "question_number":16, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2017, "question_number":17, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2017, "question_number":18, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2017, "question_number":19, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":20, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":21, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2017, "question_number":22, "mi":"D ", "max_marks":1, "section":"1", "topic_name":"Gravimetric Analysis"},
    {"year":2017, "question_number":23, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":24, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":25, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":26, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":27, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Volumetric Analysis"},
    {"year":2017, "question_number":28, "mi":"C ", "max_marks":1, "section":"1", "topic_name":"Stoichiometric Calculations"},
    {"year":2017, "question_number":29, "mi":"B ", "max_marks":1, "section":"1", "topic_name":"Stoichiometric Calculations"},
    {"year":2017, "question_number":30, "mi":"A ", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},

    # 2017 SECTION 2
    {"year":2017, "question_number":1, "sub_question":"a", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2017, "question_number":1, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2017, "question_number":1, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2017, "question_number":2, "sub_question":"a", "subsub_question":"i", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":2, "sub_question":"a", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":2, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":2, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":3, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2017, "question_number":3, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2017, "question_number":3, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2017, "question_number":4, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":4, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":4, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2017, "question_number":4, "sub_question":"b", "subsub_question":"iiA", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2017, "question_number":4, "sub_question":"b", "subsub_question":"iiB", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2017, "question_number":5, "sub_question":"", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2017, "question_number":6, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":6, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2017, "question_number":6, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":6, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2017, "question_number":6, "sub_question":"b", "subsub_question":"iiiA", "max_marks":1, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2017, "question_number":6, "sub_question":"b", "subsub_question":"iiiB", "max_marks":2, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2017, "question_number":6, "sub_question":"b", "subsub_question":"iiiC", "max_marks":1, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2017, "question_number":7, "sub_question":"a", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":7, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":7, "sub_question":"b", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Gravimetric Analysis"},
    {"year":2017, "question_number":8, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":8, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":8, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2017, "question_number":8, "sub_question":"c", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2017, "question_number":8, "sub_question":"c", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2017, "question_number":8, "sub_question":"d", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2017, "question_number":8, "sub_question":"d", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Pharmaceutical Chemistry"},
    {"year":2017, "question_number":9, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2017, "question_number":9, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2017, "question_number":9, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2017, "question_number":9, "sub_question":"c", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Synthesis"},
    {"year":2017, "question_number":9, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2017, "question_number":10, "sub_question":"a", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Volumetric Analysis"},
    {"year":2017, "question_number":10, "sub_question":"a", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Volumetric Analysis"},
    {"year":2017, "question_number":10, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Volumetric Analysis"},
    {"year":2017, "question_number":10, "sub_question":"b", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Volumetric Analysis"},
    {"year":2017, "question_number":11, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":11, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2017, "question_number":11, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":11, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2017, "question_number":11, "sub_question":"c", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Experimental Determination of Structure"},

    # 2018 SECTION 1
    {"year":2018, "question_number":1, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2018, "question_number":2, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":3, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":4, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":5, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":6, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":7, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":8, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":9, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":10, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":11, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":12, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":13, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Reaction Feasibility"},
    {"year":2018, "question_number":14, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Kinetics"},
    {"year":2018, "question_number":15, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Molecular Orbitals"},
    {"year":2018, "question_number":16, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":17, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Stereochemistry"},
    {"year":2018, "question_number":18, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2018, "question_number":19, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Synthesis"},
    {"year":2018, "question_number":20, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2018, "question_number":21, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2018, "question_number":22, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2018, "question_number":23, "mi":"A", "max_marks":1, "section":"1", "topic_name":"Experimental Determination of Structure"},
    {"year":2018, "question_number":24, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":25, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":26, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":27, "mi":"B", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":28, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Gravimetric Analysis"},
    {"year":2018, "question_number":29, "mi":"D", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":30, "mi":"C", "max_marks":1, "section":"1", "topic_name":"Practical Skills"},

    # 2018 SECTION 2
    {"year":2018, "question_number":1, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2018, "question_number":1, "sub_question":"a", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2018, "question_number":1, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Electromagnetic Radiation and Atomic Spectra"},
    {"year":2018, "question_number":1, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":1, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":2, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":2, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":2, "sub_question":"b", "subsub_question":"i", "max_marks":3, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":2, "sub_question":"b", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Chemical Equilibrium"},
    {"year":2018, "question_number":3, "sub_question":"a", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":3, "sub_question":"b", "subsub_question":"i", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":3, "sub_question":"b", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":3, "sub_question":"c", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":4, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":4, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2018, "question_number":4, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stereochemistry"},
    {"year":2018, "question_number":4, "sub_question":"d", "subsub_question":"iA", "max_marks":1, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2018, "question_number":4, "sub_question":"d", "subsub_question":"iB", "max_marks":3, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2018, "question_number":4, "sub_question":"d", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Reaction Feasibility"},
    {"year":2018, "question_number":5, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2018, "question_number":5, "sub_question":"b", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2018, "question_number":5, "sub_question":"c", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Molecular Orbitals"},
    {"year":2018, "question_number":6, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":6, "sub_question":"b", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":6, "sub_question":"b", "subsub_question":"iiA", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":6, "sub_question":"b", "subsub_question":"iiB", "max_marks":1, "section":"2", "topic_name":"Transiton Metals"},
    {"year":2018, "question_number":6, "sub_question":"c", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":6, "sub_question":"c", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":7, "sub_question":"a", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":7, "sub_question":"a", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":7, "sub_question":"a", "subsub_question":"iii", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":7, "sub_question":"a", "subsub_question":"iv", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":7, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":7, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":8, "sub_question":"a", "subsub_question":"", "max_marks":2, "section":"2", "topic_name":"Stoichiometric Calculations"},
    {"year":2018, "question_number":8, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":8, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":8, "sub_question":"d", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":9, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":9, "sub_question":"b", "subsub_question":"", "max_marks":3, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":9, "sub_question":"c", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"},
    {"year":2018, "question_number":9, "sub_question":"d", "subsub_question":"i", "max_marks":1, "section":"2", "topic_name":"Kinetics"},
    {"year":2018, "question_number":9, "sub_question":"d", "subsub_question":"ii", "max_marks":2, "section":"2", "topic_name":"Kinetics"},
    {"year":2018, "question_number":10, "sub_question":"a", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Synthesis"},
    {"year":2018, "question_number":10, "sub_question":"b", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Atomic Orbitals, Electron Configurations and the Periodic Table"},
    {"year":2018, "question_number":10, "sub_question":"c", "subsub_question":"iA", "max_marks":2, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":10, "sub_question":"c", "subsub_question":"iB", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":10, "sub_question":"c", "subsub_question":"ii", "max_marks":1, "section":"2", "topic_name":"Practical Skills"},
    {"year":2018, "question_number":10, "sub_question":"d", "subsub_question":"", "max_marks":1, "section":"2", "topic_name":"Experimental Determination of Structure"}
]

def get_or_create_unit(session, name):
    u = session.query(Unit).filter_by(name=name).first()
    if u:
        return u, False
    u = Unit(name=name)
    session.add(u)
    session.flush()
    return u, True

def get_or_create_topic(session, name, unit):
    t = session.query(Topic).filter_by(name=name, unit_id=unit.id).first()
    if t:
        return t, False
    t = Topic(name=name, unit_id=unit.id)
    session.add(t)
    session.flush()
    return t, True

def question_exists(session, q):
    # Uniqueness check using year + question_number + sub_question + subsub_question
    qry = session.query(Question).filter_by(year=q["year"], question_number=q["question_number"])
    if "sub_question" in q:
        qry = qry.filter_by(sub_question=q.get("sub_question"))
    if "subsub_question" in q:
        qry = qry.filter_by(subsub_question=q.get("subsub_question"))
    return qry.first() is not None

def create_question(session, q, topic):
    fields = {
        "year": q["year"],
        "question_number": q["question_number"],
        "topic_id": topic.id,
        "mi": q.get("mi"),
        "max_marks": q.get("max_marks"),
        "section": q.get("section"),
        "sub_question": q.get("sub_question"),
        "subsub_question": q.get("subsub_question"),
    }
    # Remove None values to respect non-nullable columns and defaults
    fields = {k: v for k, v in fields.items() if v is not None}
    question = Question(**fields)
    session.add(question)

def migrate(dry_run=True):
    created = {"units": 0, "topics": 0, "questions": 0}
    with app.app_context():
        try:
            # ensure units
            for u in NEW_UNITS:
                _, added = get_or_create_unit(db.session, u["name"])
                if added:
                    created["units"] += 1

            # ensure topics
            units = {u.name: u for u in Unit.query.all()}
            for t in NEW_TOPICS:
                unit_name = t["unit_name"]
                unit = units.get(unit_name)
                if not unit:
                    unit, added_unit = get_or_create_unit(db.session, unit_name)
                    units[unit_name] = unit
                    if added_unit:
                        created["units"] += 1
                topic, added_topic = get_or_create_topic(db.session, t["name"], unit)
                if added_topic:
                    created["topics"] += 1

            # preload topics map
            topics_by_name = {t.name: t for t in Topic.query.all()}

            # insert questions if missing
            for q in NEW_QUESTIONS:
                if question_exists(db.session, q):
                    continue
                topic = topics_by_name.get(q["topic_name"])
                if not topic:
                    default_unit = Unit.query.first()
                    if not default_unit:
                        raise RuntimeError("No Unit exists to attach topic to. Create Units first.")
                    topic, added = get_or_create_topic(db.session, q["topic_name"], default_unit)
                    topics_by_name[topic.name] = topic
                    if added:
                        created["topics"] += 1
                create_question(db.session, q, topic)
                created["questions"] += 1

            if dry_run:
                db.session.rollback()
                print("Dry run complete. Would create:", created)
            else:
                db.session.commit()
                print("Migration applied. Created:", created)

        except IntegrityError as e:
            db.session.rollback()
            print("IntegrityError:", e)
        except Exception as e:
            db.session.rollback()
            print("Unexpected error:", e)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="data migration for Units/Topics/Questions")
    parser.add_argument("--apply", action="store_true", help="apply changes to the database (default is dry run)")
    args = parser.parse_args()

    if args.apply:
        print("running migration: APPLYING changes to the database")
        migrate(dry_run=False)
    else:
        print("running migration: DRY RUN (no DB changes). Use --apply to commit.")
        migrate(dry_run=True)
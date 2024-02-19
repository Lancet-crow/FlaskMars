import datetime

from data import db_session
from data.jobs import Jobs

def main():
    db_session.global_init('db/mars_explorer.db')
    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = "deployment of residential modules 1 and 2"
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.date.today()
    jobs.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()

if __name__ == "__main__":
    main()

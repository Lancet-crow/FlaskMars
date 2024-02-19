from data import db_session
from data.users import User

db_name = input()
db_session.global_init(db_name)
db_sess = db_session.create_session()
for user in db_sess.query(User).filter(User.address == "module_1"):
    print(user)

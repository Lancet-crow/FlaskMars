db_name = input()
global_init(db_name)
db_sess = create_session()
for user in db_sess.query(User).filter(User.age <= 18):
    print(user.__repr__())

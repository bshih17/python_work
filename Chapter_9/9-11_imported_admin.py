from user_privilieges_admin import User, Privileges, Admin

admin_privileges = ['can add post', 'can delete post', 'can ban user', 'can lock thread',]

admin = Admin('Jimmy', 'Neutron', 'ThinkThinkThink BrainBlast', 9, admin_privileges)

admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()

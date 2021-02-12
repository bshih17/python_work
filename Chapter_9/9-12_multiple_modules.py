from privileges_admin import Privileges, Admin

admin_privileges = [
	'invoke the ban hammer', 'remove post', 'moderate thread', 'suspend account', 'execute justice'
]

admin = Admin('James Isaac', 'Neutron', 'JimmyNeutron', 14, admin_privileges)

admin.greet_user()
admin.describe_user()
admin.privileges.show_privileges()
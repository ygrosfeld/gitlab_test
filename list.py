my_fruits = ['apple', 'banana', 'lime']
print(len(my_fruits))

user_inputs = [True, 'hi!', ')', '10.5']
print(len(user_inputs))

posts_ids = [151, 245, 762, 167]

print(posts_ids)
print(len(posts_ids))
print(posts_ids[0])
print(posts_ids[1])
print(posts_ids[-1])

posts_ids[0]=555
posts_ids[2]=666
del posts_ids[-1]
print(len(posts_ids))
print(posts_ids)

users= [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bod'
    }
]

print(len(users))

print(users[1]['user_id'])
print(users[0]['user_name'])
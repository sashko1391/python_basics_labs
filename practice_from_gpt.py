tasks = ['read chapter 4', 'practice zsh commands', 'write python loop']
tasks.append('configure codespaces')
tasks.remove('practice zsh commands')

user_profile = {
    'username': ['dev_student'],
    'current_chapter': [4],
    'is_ready_for_functions': [False]
}

user_profile['is_ready_for_functions'] = True

print(tasks)
print(user_profile)


# vulnerable code
import sys

print("sample python")
print(os.path.abspath(__file__))

os.system('dir')

input_location = 'C:\uptycs\githubquery\gitquery_arun\gittest\sample.py'
split_list = os.path.split(input_location)
print("split list: {}".format(split_list))
AWS_CREDENTIALS = { 'key': 'djekjdkejde', 'secret': 'dncndmncdmncd' }

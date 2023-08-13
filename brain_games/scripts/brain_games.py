#!/usr/bin/env python3
import sys
sys.path.append('d:\\Github\\python-project-49\\brain_games')
from cli import welcome_user
def greetings():
    print('Welcome to the Brain Games!')
    welcome_user()

def main():
    greetings()
    
    

if __name__=='__main__':
    main()
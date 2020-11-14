# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le
# © 2020

# Version
__version__ = "1.0.0"

# Regex define
'''
email có dạng: <phần trước ký tự @> + ký tự @ + <phần sau ký tự @>
'''
email_regex_pattern = '[\w\.-]+@[\w\.-]+'

'''
website có dạng: http + kí tự[s]::// [wwww] hoặc gì đó + [.] domain
'''
website_regex_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
phone_regex_pattern = '[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

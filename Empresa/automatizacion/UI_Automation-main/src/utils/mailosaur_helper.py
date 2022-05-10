import time

from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria, MailosaurException
from datetime import datetime
from datetime import timedelta


class Mailosaur(MailosaurClient):

    def __init__(self, sign_up_email):
        self.__api_key = 'Sa5kjBBwcWTqpbfP'
        self.__server_id = "ttgfqh9d"
        self.__server_domain_login = "ttgfqh9d.mailosaur.net"
        super().__init__(self.__api_key)
        self.sign_up_email = sign_up_email
        self.messages_from_all_time = datetime.now().astimezone() - timedelta(minutes=99999)

    def get_return_code(self):
        """Returns a magic code from the letter."""
        criteria = self.create_search_criteria()
        email = self.messages.get(self.__server_id, criteria)
        users_magic_code = email.subject[27:-1]
        return users_magic_code

    def get_id(self):
        """Returns ID of the letter."""
        criteria = self.create_search_criteria()
        email = self.messages.get(self.__server_id, criteria, received_after=self.messages_from_all_time)
        return email.id

    def delete_letter(self):
        """Deletes the letter"""
        mail_id = self.get_id()
        self.messages.delete(mail_id)

    def delete_all_letters(self):
        """Deletes all letters"""
        self.messages.delete_all(self.__server_id)

    def create_search_criteria(self):
        """Creates search criteria. Helper method."""
        criteria = SearchCriteria()
        criteria.sent_to = self.sign_up_email
        return criteria

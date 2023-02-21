import sys

from datetime import datetime

from database import DatabaseManager
from typing import Dict,Any
from dataclasses import dataclass

db = DatabaseManager('database.db')

class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id' : 'integer primary key autoincrement',
            'title' : 'text not null',
            'url' : 'text not null',
            'notes' : 'text',
            'date_added' : 'text not null',
        })


class AddBookmarkCommand:
    def execute(self, data : Dict[str,str]) -> str:
        data['date_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks',data)
        return 'Bookmark added'


@dataclass
class ListBookmarksCommand:
    order_by: str = 'date_added'

    def execute(self):
        return db.select('bookmarks',order_by=self.order_by).fetchall()

class DeleteBookmarkCommand:
    def execute(self,data):
        db.delete('bookmarks',{'id':data})
        return 'Bookmark deleted'


class QuitCommand:
    def execute(self):
        sys.exit()

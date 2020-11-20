from collections import defaultdict

class School(object):

  def __init__(self, schoolName):
    self.schoolName = schoolName
    self._db = defaultdict(set)

  @property
  def db(self):
    return self._db

  def add(self, name, grade):
    self.db[grade].add(name)

  def grade(self, grade):
    return self.db[grade]

  def sort(self):
    return [(grade, tuple(sorted(self.db[grade]))) for grade in sorted(self.db)]

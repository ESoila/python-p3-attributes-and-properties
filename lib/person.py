#!/usr/bin/env python3

approved_jobs = [
    "Software Engineer", "Data Scientist", "Product Manager", "Designer",
    "Teacher", "Doctor", "Nurse", "Mechanic", "Sales", "ITC"
]

class Person:
    def __init__(self, name="Default", job="Unemployed"):
        self._name = None
        self._job = None

        self.name = name
        if self._name:
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
